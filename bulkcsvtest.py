import csv
from testapp import WelcomeGetSN, IncludeText
from time import sleep
from barcode.writer import ImageWriter
from InquirerPy import prompt


WelcomeGetSN()
print("BULK MODE SELECTED")
print("Only values in the first column of your csv file will be read")
print("Enter the PATH the your cvs file")
pathcsv = input()

IncludeText()
includeText = input()


barcodes = []
with open(pathcsv, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        barcodes.append(row[0])


IncluTextBool = False
if includeText == "y":
    IncluTextBool = True
    print("Text included with barcode")

else:
    print("No Text with barcode")
    
sleep(0.25)
print()
print("Please choose the type of barcodes you wish create")
questions = [ {
        'type': 'list',
        'name': 'user_option',
        'message': 'Please choose the type of barcode you wish create',
        'choices': ["Code 39", "Code 128", "PZN7 (aka: PZN)", "EAN-13", "EAN-8", "JAN", "ISBN-13", "ISBN-10", "ISSN", "UPC-A", "EAN14", "GS1-128"]}
    ]
    
choice = prompt(questions)


barcodeType = choice.get("user_option")
if barcodeType == "Code 39":
    from barcode import Code39
    codeObj = Code39

if barcodeType == "Code 128":
    from barcode import Code128
    codeObj = Code128

if barcodeType == "PZN7 (aka: PZN)":
    from barcode import PZN
    codeObj = PZN

if barcodeType == "EAN-13":
    from barcode import EAN13
    codeObj = EAN13

if barcodeType == "EAN-8":
    from barcode import EAN8
    codeObj = EAN8

if barcodeType == "JAN":
    from barcode import JAN
    codeObj = JAN

if barcodeType == "ISBN-13":
    from barcode import ISBN13
    codeObj = ISBN13

if barcodeType == "ISBN-10":
    from barcode import ISBN10
    codeObj = ISBN10

if barcodeType == "ISSN":
    from barcode import ISSN
    codeObj = ISSN

if barcodeType == "UPC-A":
    from barcode import UPCA
    codeObj = UPCA

if barcodeType == "EAN14":
    from barcode import EAN14
    codeObj = EAN14

if barcodeType == "GS1-128":
    from barcode import Gs1_128
    codeObj = Gs1_128

for barcode in barcodes:

    my_code = codeObj(barcode, writer=ImageWriter())

    my_code.save(barcodeType + "_" + barcode + "_barcode", 
    {"module_height": 7, 
    "font_size": 5, 
    "text_distance": 1.7, 
    "quiet_zone": 2, 
    "dpi": 200, 
    "write_text": IncluTextBool})
