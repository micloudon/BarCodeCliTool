import csv
from time import sleep
from barcode.writer import ImageWriter


def barCodeType():
    sleep(0.25)
    print()
    print("Please choose the type of barcode you wish to create.  Enter number for choice")

    print("1: Code 39") 
    print("2: Code 128") 
    print("3: PZN7 (aka: PZN)") 
    print("4: EAN-13") 
    print("5: EAN-8") 
    print("6: JAN") 
    print("7: ISBN-13")
    print("8: ISBN-10") 
    print("9: ISSN") 
    print("10: UPC-A") 
    print("11: EAN14") 
    print("12: GS1-128")



def bulkSn():
    print("BULK MODE SELECTED")
    print()
    print("Only values in the first column of your csv file will be read")
    print()
    print("Enter the PATH to your cvs file")
    pathcsv = input()

    barcodes = []
    with open(pathcsv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            barcodes.append(row[0])


    print()
    print("Do you wish to include text with your barcode:")
    print("y or n")

    includeText = input()


    IncluTextBool = False
    if includeText == "y":
        IncluTextBool = True
        print("Text included with barcode")

    else:
        print("No Text with barcode")
        
    barCodeType()

    

    barcodeType = input()
    if barcodeType == "1":
        from barcode import Code39
        codeObj = Code39

    if barcodeType == "2":
        from barcode import Code128
        codeObj = Code128

    if barcodeType == "3":
        from barcode import PZN
        codeObj = PZN

    if barcodeType == "4":
        from barcode import EAN13
        codeObj = EAN13

    if barcodeType == "5":
        from barcode import EAN8
        codeObj = EAN8

    if barcodeType == "6":
        from barcode import JAN
        codeObj = JAN

    if barcodeType == "7":
        from barcode import ISBN13
        codeObj = ISBN13

    if barcodeType == "8":
        from barcode import ISBN10
        codeObj = ISBN10

    if barcodeType == "9":
        from barcode import ISSN
        codeObj = ISSN

    if barcodeType == "10":
        from barcode import UPCA
        codeObj = UPCA

    if barcodeType == "11":
        from barcode import EAN14
        codeObj = EAN14

    if barcodeType == "12":
        from barcode import Gs1_128
        codeObj = Gs1_128

    print("Are you sure you want to generate " + str(len(barcodes)) + " barcodes?")
    print("y or n")
    finalCheck = input()

    if finalCheck == "y":
        i = 0
        for barcode in barcodes:
            i += 1
            my_code = codeObj(barcode, writer=ImageWriter())

            my_code.save(str(i) + "_" + barcodeType + "_" + barcode + "_barcode", 
            {"module_height": 7, 
            "font_size": 5, 
            "text_distance": 1.7, 
            "quiet_zone": 2, 
            "dpi": 200, 
            "write_text": IncluTextBool})

    else:
        return