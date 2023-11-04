import sqlite3
from csvtranslator import csv_translator

# creates database if its not available
conn = sqlite3.connect('../../PackingListCreator.db')

print("Created Database successfully")

# To create the table
# conn.execute("""
#         CREATE TABLE PRODUCT
#         (item_id INT Primary KEY NOT NULL,
#         nsn            TEXT NOT NULL,
#         nomenclature   TEXT NOT NULL,
#         unit_of_issue  CHAR(2));
#         """)
#
# print("Table created successfully")

# To add a single manuel entry
# conn.execute("insert into product (item_id, nsn, nomenclature, unit_of_issue) values (1, '6625-01-234-5678', 'Box', 'EA')")
#
# conn.commit()
# print("Records created successfully")

# To print out all contents of the table "products"
cursor = conn.execute("select * from product")
print(cursor.fetchall())


#Print random record from the csv that has all the records
# db_object = csv_translator()
# print(db_object.return_rand_record())

# Prints only the fields we are interested in and cuts out the rest.
# db_object.set_object_details()
# print(db_object.nsn, db_object.nomenclature, db_object.unit_of_issue)


# Adds records to the database from item_id 2 to 10
# for num in range(2,10):
#     db_object.set_object_details()
#     output_string = f"insert into product (item_id, nsn, nomenclature, unit_of_issue) values ({num}, '{db_object.nsn}', '{db_object.nomenclature}', '{db_object.unit_of_issue}')"
#     conn.execute(output_string)
#     conn.commit()
#     print(f"{db_object.nomenclature} was entered")


# Adds randoms records to the database
# for num in range(10, 30):
#     conn.execute(db_object.return_sql_string_for_table_entry(num))
#     conn.commit()


# Always close your database
conn.close()