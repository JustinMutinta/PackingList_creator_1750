from pypdf import PdfReader, PdfWriter

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
                      "page" : "1",
                      "pages" : "1",
                      "box_1" : "3",
                      "contents_1" : "Contents 1",
                      "unit_1" : "EA",
                      "init_1" : "4",
                      "total_1" : "5"
                      }
)

with open("1750/Output/Test9.pdf", "wb") as output_stream:
    writer.write(output_stream)


# 'box_1': {
#   '/T': 'box_1', '/FT': '/Tx', '/TU': 'a. Box number, line 1.','/AA': {
#       '/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)
#       }
#   },'contents_1': {
#       '/T': 'contents_1', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''
#       },
# 'unit_1': {
#   '/T': 'unit_1', '/FT': '/Tx', '/TU': 'c. Unit of issue.'
#  },
# 'init_1': {
#       '/T': 'init_1', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.','/AA': {
#           '/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}},'spares_1': {
#               '/T': 'spares_1', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.','/AA': {
#                   '/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)
#                 }
#            },
# 'total_1': {
#   '/T': 'total_1', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA':{
#       '/C': IndirectObject(420, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448),'/K': IndirectObject(421, 0, 4346682448)
#     }
#  },
#
#
#  'box_2': {'/T': 'box_2', '/FT': '/Tx', '/TU': 'a. Box number, line 2.','/AA': {
#   '/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)
#   }
# },


# 'contents_2': {'/T': 'contents_2', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''},
# 'unit_2': {'/T': 'unit_2', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, '
# init_2': {'/T': 'init_2', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.',
# '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}},
# 'spares_2': {'/T': 'spares_2', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.',
# '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}},
# 'total_2': {'/T': 'total_2', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0',
# '/AA': {'/C': IndirectObject(400, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}},
# 'box_3': {'/T': 'box_3', '/FT': '/Tx', '/TU': 'a. Box number, line 3.',
# '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}},
# 'contents_3': {'/T': 'contents_3', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''},
# 'unit_3': {'/T': 'unit_3', '/FT': '/Tx', '/TU': 'c. Unit of issue.'},
# 'init_3': {'/T': 'init_3', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.',
# '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}},
# 'spares_3': {'/T': 'spares_3', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.',
# '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}},
# 'total_3': {'/T': 'total_3', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(401, 0, 4346682448),
# '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}},
# 'box_4': {'/T': 'box_4', '/FT': '/Tx', '/TU': 'a. Box number, line 4.', '/AA': {'/F': IndirectObject(407, 0, 4346682448),
# '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_4': {'/T': 'contents_4', '
# /FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''},
# 'unit_4': {'/T': 'unit_4', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_4': {'/T': 'init_4', '/FT': '/Tx',
# '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448),
# '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_4': {'/T': 'spares_4', '/FT': '/Tx',
# '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448),
# '/K': IndirectObject(411, 0, 4346682448)}}, 'total_4': {'/T': 'total_4', '/FT': '/Tx', '/TU': 'f. Total.',
# '/V': '0', '/AA': {'/C': IndirectObject(427, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448),
# '/K': IndirectObject(421, 0, 4346682448)}}, 'box_5': {'/T': 'box_5', '/FT': '/Tx', '/TU': 'a. Box number, line 5.',
# '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_5':
# {'/T': 'contents_5', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''},
# 'unit_5': {'/T': 'unit_5', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_5': {'/T': 'init_5', '/FT': '/Tx', '/TU':
# 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448),
# '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_5': {'/T': 'spares_5', '/FT': '/Tx', '/TU':
# 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '
# /K': IndirectObject(411, 0, 4346682448)}}, 'total_5': {'/T': 'total_5', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0',
# '/AA': {'/C': IndirectObject(398, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}},
# 'contents_6': {'/T': 'contents_6', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''},
# 'unit_6': {'/T': 'unit_6', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_6': {'/T': 'init_6', '/FT': '/Tx', '/TU':
# 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}},
# 'spares_6': {'/T': 'spares_6', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.',
# '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}},
# 'total_6': {'/T': 'total_6', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(422, 0, 4346682448),
# '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_6': {'/T': 'box_6', '/FT': '/Tx', '/TU':
# 'a. Box number, line 6.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}},
# 'init_7': {'/T': 'init_7', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.',
# '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}},
# 'spares_7': {'/T': 'spares_7', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.',
# '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}},
# 'total_7': {'/T': 'total_7', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(403, 0, 4346682448),
# '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}},
# 'box_7': {'/T': 'box_7', '/FT': '/Tx', '/TU': 'a. Box number, line 7.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_7': {'/T': 'contents_7', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_7': {'/T': 'unit_7', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'box_8': {'/T': 'box_8', '/FT': '/Tx', '/TU': 'a. Box number, line 8.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_8': {'/T': 'contents_8', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_8': {'/T': 'unit_8', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_8': {'/T': 'init_8', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_8': {'/T': 'spares_8', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_8': {'/T': 'total_8', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(425, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_9': {'/T': 'box_9', '/FT': '/Tx', '/TU': 'a. Box number, line 9.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_9': {'/T': 'contents_9', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_9': {'/T': 'unit_9', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_9': {'/T': 'init_9', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_9': {'/T': 'spares_9', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_9': {'/T': 'total_9', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(392, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_10': {'/T': 'box_10', '/FT': '/Tx', '/TU': 'a. Box number, line 10.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_10': {'/T': 'contents_10', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_10': {'/T': 'unit_10', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_10': {'/T': 'init_10', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_10': {'/T': 'spares_10', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_10': {'/T': 'total_10', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(426, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_11': {'/T': 'box_11', '/FT': '/Tx', '/TU': 'a. Box number, line 11.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_11': {'/T': 'contents_11', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_11': {'/T': 'unit_11', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_11': {'/T': 'init_11', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_11': {'/T': 'spares_11', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_11': {'/T': 'total_11', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(397, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_12': {'/T': 'box_12', '/FT': '/Tx', '/TU': 'a. Box number, line 12.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_12': {'/T': 'contents_12', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_12': {'/T': 'unit_12', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_12': {'/T': 'init_12', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_12': {'/T': 'spares_12', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_12': {'/T': 'total_12', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(400, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_13': {'/T': 'box_13', '/FT': '/Tx', '/TU': 'a. Box number, line 13.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_13': {'/T': 'contents_13', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_13': {'/T': 'unit_13', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_13': {'/T': 'init_13', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_13': {'/T': 'spares_13', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_13': {'/T': 'total_13', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(396, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_14': {'/T': 'box_14', '/FT': '/Tx', '/TU': 'a. Box number, line 14.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_14': {'/T': 'contents_14', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_14': {'/T': 'unit_14', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_14': {'/T': 'init_14', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_14': {'/T': 'spares_14', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_14': {'/T': 'total_14', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(424, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_15': {'/T': 'box_15', '/FT': '/Tx', '/TU': 'a. Box number, line 15.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_15': {'/T': 'contents_15', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_15': {'/T': 'unit_15', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_15': {'/T': 'init_15', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_15': {'/T': 'spares_15', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_15': {'/T': 'total_15', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(416, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_16': {'/T': 'box_16', '/FT': '/Tx', '/TU': 'a. Box number, line 16.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_16': {'/T': 'contents_16', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_16': {'/T': 'unit_16', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_16': {'/T': 'init_16', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_16': {'/T': 'spares_16', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_16': {'/T': 'total_16', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(395, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_17': {'/T': 'box_17', '/FT': '/Tx', '/TU': 'a. Box number, line 17.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_17': {'/T': 'contents_17', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_17': {'/T': 'unit_17', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_17': {'/T': 'init_17', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_17': {'/T': 'spares_17', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_17': {'/T': 'total_17', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(404, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'box_18': {'/T': 'box_18', '/FT': '/Tx', '/TU': 'a. Box number, line 18.', '/AA': {'/F': IndirectObject(407, 0, 4346682448), '/K': IndirectObject(405, 0, 4346682448)}}, 'contents_18': {'/T': 'contents_18', '/FT': '/Tx', '/TU': 'b. Contents - stock number and nomenclature.', '/Ff': 8392704, '/V': ''}, 'unit_18': {'/T': 'unit_18', '/FT': '/Tx', '/TU': 'c. Unit of issue.'}, 'init_18': {'/T': 'init_18', '/FT': '/Tx', '/TU': 'Quantities required.  d. Initial Operation.', '/AA': {'/F': IndirectObject(412, 0, 4346682448), '/K': IndirectObject(409, 0, 4346682448)}}, 'spares_18': {'/T': 'spares_18', '/FT': '/Tx', '/TU': 'Quantities required: e. Running Spares.', '/AA': {'/F': IndirectObject(408, 0, 4346682448), '/K': IndirectObject(411, 0, 4346682448)}}, 'total_18': {'/T': 'total_18', '/FT': '/Tx', '/TU': 'f. Total.', '/V': '0', '/AA': {'/C': IndirectObject(393, 0, 4346682448), '/F': IndirectObject(417, 0, 4346682448), '/K': IndirectObject(421, 0, 4346682448)}}, 'certname': {'/T': 'certname', '/FT': '/Tx', '/TU': '6. Typed name and title.', '/Ff': 8392704, '/V': ''}, 'certsign': {'/T': 'certsign', '/FT': '/Tx', '/TU': 'Signature.'}, 'Reset': {'/T': 'Reset', '/FT': '/Btn', '/TU': 'Press this Reset button to clear the data from all fields.', '/Ff': 65536,
# '/_States_': ['/Subtype', '/Filter', '/Resources', '/BBox', '/Off']}}