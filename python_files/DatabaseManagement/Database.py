import sqlite3

conn = sqlite3.connect('PackingListCreator.db')

print("Created Database successfully")

conn.execute("""
        CREATE TABLE PRODUCT
        (item_id INT Primary KEY NOT NULL,
        nsn            TEXT NOT NULL,
        nomenclature   TEXT NOT NULL,
        unit_of_issue  CHAR(2));
        """)

print("Table created successfully")