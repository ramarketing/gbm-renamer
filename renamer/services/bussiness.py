import csv
import os

from config import BASE_DIR
from services.base import (
    BaseEntity, BaseEntityList, BaseService
)
from constants import CSV_FIELDS, CSV_HEADER


class Business(BaseEntity):
    def __str__(self):
        return self.name

    def get_csv_line(self, counter):
        line = []
        for field in CSV_FIELDS:
            if field == 'id':
                value = counter
            elif field and hasattr(self, field):
                value = getattr(self, field)
            else:
                value = ''
            line.append('{}'.format(value))

        return line

    def get_validation_code(self, phone_number):
        data = dict(
            phone_number=phone_number
        )
        return self.service.request(
            'post', pk=self.pk, extra='get-validation-code', data=data
        )

    def report_validation(self):
        return self.service.request(
            'post', pk=self.pk, extra='set-validated', in_raw=True
        )

    def report_success(self):
        return self.service.request(
            'post', pk=self.pk, extra='set-success'
        )


class BusinessList(BaseEntityList):
    entity = Business

    def create_csv(self):
        path = os.path.join(BASE_DIR, 'csv/gbm.csv')
        with open(path, 'w') as file:
            counter = 1
            writer = csv.writer(file)
            writer.writerow(CSV_HEADER)

            for biz in self:
                writer.writerow(biz.get_csv_line(counter))
                counter += 1
        return path

    def get_by_name(self, value):
        return self.get_by('name', value)


class BusinessService(BaseService):
    endpoint = '/renamer/business/'
    entity = Business
    entity_list = BusinessList
