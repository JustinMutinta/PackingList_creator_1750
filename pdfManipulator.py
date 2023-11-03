from pypdf import PdfReader, PdfWriter
from datetime import datetime, date


now = datetime.now()
dateTime_string = now.strftime("%m-%d-%Y_%H:%M:%S")
date_string = now.date()

test_data = [
    {"item Number 1", "1234-56-789-1234", "EA"},
    {"item Number 2", "1234-56-789-1234", "EA"},
    {"item Number 3", "1234-56-789-1234", "BX"},
    {"item Number 4", "1234-56-789-1234", "EA"},
    {"item Number 5", "1234-56-789-1234", "KT"},
    {"item Number 6", "1234-56-789-1234", "EA"},
    {"item Number 7", "1234-56-789-1234", "EA"},
]

username = "SPC JOE SNUFFY"
container = "TUFF BOX"

fields_be_added_top = {
    "3_END_ITEM": "",
    "PACKED_BY": "",
    "4_DATE": "",
    "page" : "1", "pages" : "1",
}

fields_be_added_bottom = {
    "certname" : "Person that created this"
}

fields_be_added_main = {
    "box_1" : "", "contents_1" : "", "unit_1" : "", "init_1" : "", "total_1" : "",
    "box_2" : "", "contents_2" : "", "unit_2" : "", "init_2" : "", "total_2" : "",
    "box_3" : "", "contents_3" : "", "unit_3" : "", "init_3" : "", "total_3" : "",
    "box_4" : "", "contents_4" : "", "unit_4" : "", "init_4" : "", "total_4" : "",
    "box_5" : "", "contents_5" : "", "unit_5" : "", "init_5" : "", "total_5" : "",
    "box_6" : "", "contents_6" : "", "unit_6" : "", "init_6" : "", "total_6" : "",
    "box_7" : "", "contents_7" : "", "unit_7" : "", "init_7" : "", "total_7" : "",
    "box_8" : "", "contents_8" : "", "unit_8" : "", "init_8" : "", "total_8" : "",
    "box_9" : "", "contents_9" : "", "unit_9" : "", "init_9" : "", "total_9" : "",
    "box_10" : "", "contents_10" : "", "unit_10" : "", "init_10" : "", "total_10" : "",
    "box_11" : "", "contents_11" : "", "unit_11" : "", "init_11" : "", "total_11" : "",
    "box_12" : "", "contents_12" : "", "unit_12" : "", "init_12" : "", "total_12" : "",
    "box_13" : "", "contents_13" : "", "unit_13" : "", "init_13" : "", "total_13" : "",
    "box_14" : "", "contents_14" : "", "unit_14" : "", "init_14" : "", "total_14" : "",
    "box_15" : "", "contents_15" : "", "unit_15" : "", "init_15" : "", "total_15" : "",
    "box_16" : "", "contents_16" : "", "unit_16" : "", "init_16" : "", "total_16" : "",
    "box_17" : "", "contents_17" : "", "unit_17" : "", "init_17" : "", "total_17" : "",
    "box_18" : "", "contents_18" : "", "unit_18" : "", "init_18" : "", "total_18" : "",
}


def pdf_creator(username, container):
    reader = PdfReader("1750/Template/DD-FORM-1750.pdf")
    writer = PdfWriter()

    page = reader.pages[0]

    writer.add_page(page)

    fields_to_be_added = {}
    fields_to_be_added.update(fields_be_added_top)
    fields_to_be_added.update(fields_be_added_main)
    fields_to_be_added.update(fields_be_added_bottom)

    writer.update_page_form_field_values(
        writer.pages[0], fields_to_be_added
    )

    try:
        with open(f"1750/Output/{dateTime_string}_{container}_{username}_1750.pdf", "wb") as output_stream:
            writer.write(output_stream)
    except Exception as e:
        print(e)







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



def print_1750(username, container):
    with open(f"1750/Output/{dateTime_string}_{container}_{username}_1750.pdf", "wb") as output_stream:
        writer.write(output_stream)


# print_1750(username, container)
pdf_creator(username, container)