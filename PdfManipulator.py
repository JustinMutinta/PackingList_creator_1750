from pypdf import PdfReader, PdfWriter
from datetime import datetime, date


class PdfManipulator:
    def __init__(self, username, container):
        self.username = username
        self.container = container

    now = datetime.now()
    dateTime_string = now.strftime("%m-%d-%Y_%H:%M:%S")
    date_string = now.date()

    fields_be_added_top = {
        "3_END_ITEM": "",
        "PACKED_BY": "",
        "4_DATE": "",
        "page": "1", "pages": "1",
    }

    fields_be_added_bottom = {
        "certname": ""
    }

    fields_be_added_main = {
        "box_1": "", "contents_1": "", "unit_1": "", "init_1": "", "total_1": "",
        "box_2": "", "contents_2": "", "unit_2": "", "init_2": "", "total_2": "",
        "box_3": "", "contents_3": "", "unit_3": "", "init_3": "", "total_3": "",
        "box_4": "", "contents_4": "", "unit_4": "", "init_4": "", "total_4": "",
        "box_5": "", "contents_5": "", "unit_5": "", "init_5": "", "total_5": "",
        "box_6": "", "contents_6": "", "unit_6": "", "init_6": "", "total_6": "",
        "box_7": "", "contents_7": "", "unit_7": "", "init_7": "", "total_7": "",
        "box_8": "", "contents_8": "", "unit_8": "", "init_8": "", "total_8": "",
        "box_9": "", "contents_9": "", "unit_9": "", "init_9": "", "total_9": "",
        "box_10": "", "contents_10": "", "unit_10": "", "init_10": "", "total_10": "",
        "box_11": "", "contents_11": "", "unit_11": "", "init_11": "", "total_11": "",
        "box_12": "", "contents_12": "", "unit_12": "", "init_12": "", "total_12": "",
        "box_13": "", "contents_13": "", "unit_13": "", "init_13": "", "total_13": "",
        "box_14": "", "contents_14": "", "unit_14": "", "init_14": "", "total_14": "",
        "box_15": "", "contents_15": "", "unit_15": "", "init_15": "", "total_15": "",
        "box_16": "", "contents_16": "", "unit_16": "", "init_16": "", "total_16": "",
        "box_17": "", "contents_17": "", "unit_17": "", "init_17": "", "total_17": "",
        "box_18": "", "contents_18": "", "unit_18": "", "init_18": "", "total_18": "",
    }

    pdf_output = ""

    def pdf_creator(self):
        global dateTime_string

        now = datetime.now()
        dateTime_string = now.strftime("%m-%d-%Y_%H:%M:%S")

        reader = PdfReader("1750/Template/DD-FORM-1750.pdf")
        writer = PdfWriter()

        page = reader.pages[0]

        writer.add_page(page)

        fields_to_be_added = {}
        fields_to_be_added.update(self.fields_be_added_top)
        fields_to_be_added.update(self.fields_be_added_main)
        fields_to_be_added.update(self.fields_be_added_bottom)

        writer.update_page_form_field_values(
            writer.pages[0], fields_to_be_added
        )

        try:
            self.pdf_output = f"1750/Output/{dateTime_string}_{self.container}_{self.username}_1750.pdf"
            with open(self.pdf_output, "wb") as output_stream:
                writer.write(output_stream)
        except Exception as e:
            print(e)

    def output_pdf_location(self):
        if self.pdf_output == "":
            return "There is no Output"
        else:
            return self.pdf_output

    def fill_in_pdf(self, test_data):
        global fields_be_added_top
        global fields_be_added_bottom
        global fields_be_added_main

        if len(test_data) == 0:
            pass
        else:
            self.fields_be_added_top.update({
                f"3_END_ITEM": self.container,
                f"PACKED_BY": self.username,
                f"4_DATE": self.date_string,
                "page": "1", "pages": "1",
            })

            self.fields_be_added_bottom.update({
                "certname": self.username
            })

            for value in range(len(test_data) + 1):
                if value == 0:
                    pass
                else:
                    new_content = f"contents_{value}"
                    new_unit_of_issue = f"unit_{value}"
                    new_initial = f"init_{value}"
                    new_total = f"total_{value}"
                    self.fields_be_added_main[new_content] = f"{test_data[value - 1]}"
                    self.fields_be_added_main[new_unit_of_issue] = f"EA"
                    self.fields_be_added_main[new_initial] = 1
                    self.fields_be_added_main[new_total] = 1

            self.pdf_creator()
