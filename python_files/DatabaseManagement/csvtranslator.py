import csv
import random


class csv_translator:
    nsn = ""
    nomenclature = ""
    unit_of_issue = ""

    def return_20_records(self):
        record_return = []
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for num in range(20):
                add_record = next(csv_reader)[0], next(csv_reader)[2], next(csv_reader)[5]
                record_return.append(add_record)

        return record_return

    def return_rand_record(self):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)
            return rows[num][0], rows[num][2], rows[num][5]

    def set_object_details(self):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)

            self.nsn = rows[num][0]
            self.nomenclature = rows[num][2]
            self.unit_of_issue = rows[num][5]

    def return_sql_string_for_table_entry(self, item_id):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)

            return f"insert into product (item_id, nsn, nomenclature, unit_of_issue) values ({item_id}, '{rows[num][0]}', '{rows[num][2]}', '{rows[num][5]}')"
