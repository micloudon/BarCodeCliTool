from pick import pick
from barcode.writer import ImageWriter
import sys
  


def main():


    print("enter the serial number you wish to turn into a barcode")
    barcodeNumber = input()

    print()
    print("Do you wish to include text with your barcode:")
    print("y or n")
    includeText = input()

    title = "Please choose the type of barcode you wish create"
    options = ["Code 39", "Code 128", "PZN7 (aka: PZN)", "EAN-13", "EAN-8", "JAN", "ISBN-13", "ISBN-10", "ISSN", "UPC-A", "EAN14", "GS1-128", "EXIT"]
    option, index = pick(options, title, indicator="=>", default_index=2)


    
    
    if option == options[0]:
        from barcode import Code39
        my_code = Code39(barcodeNumber, writer=ImageWriter())

    if option == options[1]:
        from barcode import Code128
        my_code = Code128(barcodeNumber, writer=ImageWriter())

    if option == options[2]:
        from barcode import PZN
        my_code = PZN(barcodeNumber, writer=ImageWriter())

    if option == options[3]:
        from barcode import EAN13
        my_code = EAN13(barcodeNumber, writer=ImageWriter())

    if option == options[4]:
        from barcode import EAN8
        my_code = EAN8(barcodeNumber, writer=ImageWriter())

    if option == options[5]:
        from barcode import JAN
        my_code = JAN(barcodeNumber, writer=ImageWriter())

    if option == options[6]:
        from barcode import ISBN13
        my_code = ISBN13(barcodeNumber, writer=ImageWriter())

    if option == options[7]:
        from barcode import ISBN10
        my_code = ISBN10(barcodeNumber, writer=ImageWriter())

    if option == options[8]:
        from barcode import ISSN
        my_code = ISSN(barcodeNumber, writer=ImageWriter())

    if option == options[9]:
        from barcode import UPCA
        my_code = UPCA(barcodeNumber, writer=ImageWriter())

    if option == options[10]:
        from barcode import EAN14
        my_code = EAN14(barcodeNumber, writer=ImageWriter())

    if option == options[11]:
        from barcode import Gs1_128
        my_code = Gs1_128(barcodeNumber, writer=ImageWriter())

    if option == options[12]:
        return

    IncluTextBool = False
    if includeText == "y":
        IncluTextBool = True
    
    # Our barcode is ready. Let's save it.
    my_code.save(option + "_" + barcodeNumber + "_barcode", 
    {"module_height": 7, 
    "font_size": 5, 
    "text_distance": 1.7, 
    "quiet_zone": 2, 
    "dpi": 200, 
    "write_text": IncluTextBool})


if __name__ == "__main__":
    main()