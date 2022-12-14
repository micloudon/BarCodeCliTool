from time import sleep
from barcode.writer import ImageWriter
from bulkmode import bulkSn

# check for bulk, say if bulk then run the bulk script
def Welcome():
    print()
    print('\033[1m' + "------------------------------------------------------------------------------" + '\033[0m')
    print('\033[1m' + "Hello my name is Barcode Generator CLI Tool, you can call me BGCT if you like" + '\033[0m')
    print('\033[1m' + "------------------------------------------------------------------------------" + '\033[0m')
    print()


def singleSn():  
    
    print("Enter the serial number you wish to turn into a barcode")
    barcodeNumber = input()

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
    

    barcodeType = input()
    # barcode number needs to be loop of values
    # once barcode type is selected a loop needs to assign the code a save it the ifs and the save need to looped
    # barcodeType = choice.get("barcode_type")
    if barcodeType == "1":
        from barcode import Code39
        my_code = Code39(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "2":
        from barcode import Code128
        my_code = Code128(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "3":
        from barcode import PZN
        my_code = PZN(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "4":
        from barcode import EAN13
        my_code = EAN13(barcodeNumber, writer=ImageWriter())
    elif barcodeType == "5":
        from barcode import EAN8
        my_code = EAN8(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "6":
        from barcode import JAN
        my_code = JAN(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "7":
        from barcode import ISBN13
        my_code = ISBN13(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "8":
        from barcode import ISBN10
        my_code = ISBN10(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "9":
        from barcode import ISSN
        my_code = ISSN(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "10":
        from barcode import UPCA
        my_code = UPCA(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "11":
        from barcode import EAN14
        my_code = EAN14(barcodeNumber, writer=ImageWriter())

    elif barcodeType == "12":
        from barcode import Gs1_128
        my_code = Gs1_128(barcodeNumber, writer=ImageWriter())

    # Our barcode is ready. Let's save it.
    my_code.save(barcodeType + "_" + barcodeNumber + "_barcode", 
    {"module_height": 7, 
    "font_size": 5, 
    "text_distance": 1.7, 
    "quiet_zone": 2, 
    "dpi": 200, 
    "write_text": IncluTextBool})

    print("Barcode " + barcodeNumber + " Generated")


def main():
    Welcome()

    print("Please choose the type of barcode you wish create. Enter number for choice")
    print("1: single")
    print("2: BULK")
    mode = input()

    if mode == "1":
        singleSn()

    elif mode == "2":
        bulkSn()


if __name__ == "__main__":
    main()