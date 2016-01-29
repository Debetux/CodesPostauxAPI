import csv
import os
import time
from models import City
from app import db


City.create_table(True)
i = 0
data_source = []
print(City.delete().execute())
with open('cp.csv', 'r', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')

    for row in spamreader:
        data_source.append(
            {
                "insee": row[0],
                "name": row[1],
                "postal_code": row[2],
                "label": row[3]
            }
        )
        i += 1

        if len(data_source) > 100:
            print('+1')
            with db.atomic():
                City.insert_many(data_source).execute()
            data_source = []
            time.sleep(0.02)
