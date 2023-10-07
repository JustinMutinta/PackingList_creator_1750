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
print(db_object.return_rand_record())

# db_object.set_object_details()
# print(db_object.nsn, db_object.nomenclature, db_object.unit_of_issue)

# for num in range(2,10):
#     db_object.set_object_details()
#     output_string = f"insert into product (item_id, nsn, nomenclature, unit_of_issue) values ({num}, '{db_object.nsn}', '{db_object.nomenclature}', '{db_object.unit_of_issue}')"
#     conn.execute(output_string)
#     conn.commit()
#     print(f"{db_object.nomenclature} was entered")

conn.close()

for num in range(3, 30):
    print(db_object.return_sql_string_for_table_entry(num))
