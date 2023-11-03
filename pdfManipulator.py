from pypdf import PdfReader, PdfWriter
from datetime import datetime


now = datetime.now()

# print(now)
dt_string = now.strftime("%m-%d-%Y_%H:%M:%S")
# print(dt_string)

reader = PdfReader("1750/Template/DD-FORM-1750.pdf")
writer = PdfWriter()


page = reader.pages[0]
fields = reader.get_fields()

# print(fields)

writer.add_page(page)

writer.update_page_form_field_values(
    writer.pages[0], {"3_END_ITEM": "Test NAme",
                      "PACKED_BY": "Test Packed by",
                      "4_DATE": "Today's Date",

                      "page" : "1", "pages" : "1",

                        "box_1" : "3", "contents_1" : "Contents 1", "unit_1" : "EA", "init_1" : "4", "total_1" : "5",
                      "box_2" : "6", "contents_2" : "Contents 2", "unit_2" : "BX", "init_2" : "7", "total_2" : "8",
                        "box_3" : "3", "contents_3" : "Contents 1", "unit_3" : "EA", "init_3" : "4", "total_3" : "5",
                      "box_4" : "6", "contents_4" : "Contents 2", "unit_4" : "BX", "init_4" : "7", "total_4" : "8",
                        "box_5" : "3", "contents_5" : "Contents 1", "unit_5" : "EA", "init_5" : "4", "total_5" : "5",
                      "box_6" : "6", "contents_6" : "Contents 2", "unit_6" : "BX", "init_6" : "7", "total_6" : "8",
                        "box_7" : "3", "contents_7" : "Contents 1", "unit_7" : "EA", "init_7" : "4", "total_7" : "5",
                      "box_8" : "6", "contents_8" : "Contents 2", "unit_8" : "BX", "init_8" : "7", "total_8" : "8",
                        "box_9" : "3", "contents_9" : "Contents 1", "unit_9" : "EA", "init_9" : "4", "total_9" : "5",
                      "box_10" : "6", "contents_10" : "Contents 2", "unit_10" : "BX", "init_10" : "7", "total_10" : "8",
                        "box_11" : "3", "contents_11" : "Contents 1", "unit_11" : "EA", "init_11" : "4", "total_11" : "5",
                      "box_12" : "6", "contents_12" : "Contents 2", "unit_12" : "BX", "init_12" : "7", "total_12" : "8",
                        "box_13" : "3", "contents_13" : "Contents 1", "unit_13" : "EA", "init_13" : "4", "total_13" : "5",
                      "box_14" : "6", "contents_14" : "Contents 2", "unit_14" : "BX", "init_14" : "7", "total_14" : "8",
                        "box_15" : "3", "contents_15" : "Contents 1", "unit_15" : "EA", "init_15" : "4", "total_15" : "5",
                      "box_16" : "6", "contents_16" : "Contents 2", "unit_16" : "BX", "init_16" : "7", "total_16" : "8",
                        "box_17" : "3", "contents_17" : "Contents 1", "unit_17" : "EA", "init_17" : "4", "total_17" : "5",
                      "box_18" : "6", "contents_18" : "Contents 2", "unit_18" : "BX", "init_18" : "7", "total_18" : "8",


                      "certname" : "Person that created this"
                      }
)

username = "Username"
container = "Container"

def print_1750(username, container):
    with open(f"1750/Output/{dt_string}_{container}_{username}_1750.pdf", "wb") as output_stream:
        writer.write(output_stream)


print_1750(username, container)
