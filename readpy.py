from pypdf import PdfReader
import requests
import os
api_key_env_var = "API_KEY"
env_file_path = ".env"

def main(): 

    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as env_file:
            env_contents = env_file.read()
    else:
        env_contents = ""
    if f"{api_key_env_var}=" not in env_contents:
        api_key = input("No API key found! Please enter your API Lovo AI key:")

        with open(env_file_path, "w") as file:
            file.write(f"{api_key_env_var}={api_key}")
            print("your API key has been stored to {}".format(env_file_path))


    pdf_file_name = ""
    while not pdf_file_name:
        input_file = input("Please enter the name of your PDF file: ").lower()

        # make sure it is a PDF file
        if os.path.splitext(input_file)[1] != ".pdf":
            input_file = input_file + ".pdf"

        if os.path.isfile(f"{os.getcwd()}\\{input_file}"):
            pdf_file_name = input_file
            print("file found!")
        else:
            print("file not found! please make sure the pdf file exists in your current directory and try again.")

    reader = PdfReader(pdf_file_name)
    pdf_text = ("".join([page.extract_text().replace("\n", " ") for page in reader.pages]))
    print(pdf_text)
    

if __name__ == "__main__":
    main()