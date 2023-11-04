import csv
import random


# Create class
class csv_translator:
    # Create variables
    nsn = ""
    nomenclature = ""
    unit_of_issue = ""

    # Returns 20 random records from the csv file
    def return_20_records(self):
        record_return = []
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for num in range(20):
                add_record = next(csv_reader)[0], next(csv_reader)[2], next(csv_reader)[5]
                record_return.append(add_record)

        return record_return

    # Returns one random record from the csv file
    def return_rand_record(self):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)
            return rows[num][0], rows[num][2], rows[num][5]

    # Sets one object variables
    def set_object_details(self):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)

            self.nsn = rows[num][0]
            self.nomenclature = rows[num][2]
            self.unit_of_issue = rows[num][5]

    # Returns a string you can use to enter the record into the datbase
    def return_sql_string_for_table_entry(self, item_id):
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num = random.randint(1, 10365)
            rows = list(csv_reader)

            return f"insert into product (item_id, nsn, nomenclature, unit_of_issue) values ({item_id}, '{rows[num][0]}', '{rows[num][2]}', '{rows[num][5]}')"
