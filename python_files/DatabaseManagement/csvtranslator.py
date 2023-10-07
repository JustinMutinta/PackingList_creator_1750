import csv


class csv_translator:


    def return_20_records(self):
        record_return = []
        with open('nsn-extract.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for num in range(20):
                add_record = next(csv_reader)[0], next(csv_reader)[2], next(csv_reader)[5]
                record_return.append(add_record)

        return record_return
