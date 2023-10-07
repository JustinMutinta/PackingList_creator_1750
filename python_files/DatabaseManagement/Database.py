import sqlite3
from csvtranslator import csv_translator

conn = sqlite3.connect('PackingListCreator.db')

print("Created Database successfully")

# conn.execute("""
#         CREATE TABLE PRODUCT
#         (item_id INT Primary KEY NOT NULL,
#         nsn            TEXT NOT NULL,
#         nomenclature   TEXT NOT NULL,
#         unit_of_issue  CHAR(2));
#         """)
#
# print("Table created successfully")

# conn.execute("insert into product (item_id, nsn, nomenclature, unit_of_issue) values (1, '6625-01-234-5678', 'Box', 'EA')")
#
# conn.commit()
# print("Records created successfully")


cursor = conn.execute("select * from product")
print(cursor.fetchall())

db_object = csv_translator()
print(db_object.return_20_records())

conn.close()