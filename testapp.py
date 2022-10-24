from time import sleep
from barcode.writer import ImageWriter
from InquirerPy import prompt

# check for bulk, say if bulk then run the bulk script
def WelcomeGetSN():
    print("Hello my name is Barcode Generator CLI Tool, you can call me BGCT if you like")
    print()

def IncludeText():
    print()
    print("Do you wish to include text with your barcode:")
    print("y or n")
    

def main():

    WelcomeGetSN()
    print("Enter the serial number you wish to turn into a barcode")
    barcodeNumber = input()

    IncludeText()
    includeText = input()

    IncluTextBool = False
    if includeText == "y":
        IncluTextBool = True
        print("Text included with barcode")

    else:
        print("No Text with barcode")
    
    sleep(0.25)
    print()
    print("Please choose the type of barcode you wish create")
    questions = [ {
        'type': 'list',
        'name': 'user_option',
        'message': 'Please choose the type of barcode you wish create',
        'choices': ["Code 39", "Code 128", "PZN7 (aka: PZN)", "EAN-13", "EAN-8", "JAN", "ISBN-13", "ISBN-10", "ISSN", "UPC-A", "EAN14", "GS1-128"]}
    ]
    
    choice = prompt(questions)

    # barcode number needs to be loop of values
    # once barcode type is selected a loop needs to assign the code a save it the ifs and the save need to looped
    barcodeType = choice.get("user_option")
    if barcodeType == "Code 39":
        from barcode import Code39
        my_code = Code39(barcodeNumber, writer=ImageWriter())

    if barcodeType == "Code 128":
        from barcode import Code128
        my_code = Code128(barcodeNumber, writer=ImageWriter())

    if barcodeType == "PZN7 (aka: PZN)":
        from barcode import PZN
        my_code = PZN(barcodeNumber, writer=ImageWriter())

    if barcodeType == "EAN-13":
        from barcode import EAN13
        my_code = EAN13(barcodeNumber, writer=ImageWriter())
    if barcodeType == "EAN-8":
        from barcode import EAN8
        my_code = EAN8(barcodeNumber, writer=ImageWriter())

    if barcodeType == "JAN":
        from barcode import JAN
        my_code = JAN(barcodeNumber, writer=ImageWriter())

    if barcodeType == "ISBN-13":
        from barcode import ISBN13
        my_code = ISBN13(barcodeNumber, writer=ImageWriter())

    if barcodeType == "ISBN-10":
        from barcode import ISBN10
        my_code = ISBN10(barcodeNumber, writer=ImageWriter())

    if barcodeType == "ISSN":
        from barcode import ISSN
        my_code = ISSN(barcodeNumber, writer=ImageWriter())

    if barcodeType == "UPC-A":
        from barcode import UPCA
        my_code = UPCA(barcodeNumber, writer=ImageWriter())

    if barcodeType == "EAN14":
        from barcode import EAN14
        my_code = EAN14(barcodeNumber, writer=ImageWriter())

    if barcodeType == "GS1-128":
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




if __name__ == "__main__":
    main()