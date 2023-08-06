from pypdf import PdfReader
import os

def main(): 
    pdf_file = ""
    while not pdf_file:
        input_file = input("Please enter the name of your PDF file: ").lower()

        # make sure it is a PDF file
        if os.path.splitext(input_file)[1] != ".pdf":
            input_file = input_file + ".pdf"


        # check to make sure the file exists
        if os.path.isfile(f"{os.getcwd()}\\{input_file}"):
            pdf_file = input_file
            print("file found!")
        else:
            print("file not found! please make sure the pdf file exists in your current directory and try again.")

    reader = PdfReader(pdf_file)
    for page in reader.pages:
        print(page.extract_text())

        #TODO: add the text to speech

if __name__ == "__main__":
    main()