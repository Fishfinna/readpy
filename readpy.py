from pypdf import PdfReader
import requests
import os
import json

api_key_env_var = "API_KEY"
env_file_path = ".env"
speaker = "62e8c3581ffadc3ff72832aa"  # Kim Baker
speakerStyle = "62e8c5a8d25ca640d831a525"  # narrative


def main():
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as env_file:
            env_contents = env_file.read()
            api_key = [
                i.split(f"{api_key_env_var}=")[1]
                for i in env_contents.split("\n")
                if f"{api_key_env_var}=" in i
            ][0]
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
            print(
                "file not found! please make sure the pdf file exists in your current directory and try again."
            )

    reader = PdfReader(pdf_file_name)
    pdf_text = "".join(
        [page.extract_text().replace("\n", " ") for page in reader.pages]
    )

    # curl -X 'POST' \

    #   'https://api.genny.lovo.ai/api/v1/tts' \
    #   -H 'accept: application/json' \
    #   -H 'X-API-KEY: bc2e66ed-3013-4f4c-90b2-a4bd3c0cc08e' \
    #   -H 'Content-Type: application/json' \
    #   -d '{
    #   "speaker": "62e8c3581ffadc3ff72832aa",
    #   "speakerStyle": "62e8c5a8d25ca640d831a525",
    #   "text": "Sample text for testing Text to Speech API"
    # }'

    url = "https://api.genny.lovo.ai/api/v1/tts"
    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }

    data = {
        "speaker": "62e8c3581ffadc3ff72832aa",
        "speakerStyle": "62e8c5a8d25ca640d831a525",
        "text": pdf_text,
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code not in ["201", "200"]:
        json_response = response.json()
        print(json_response)
    else:
        print("Request failed with status code:", response.status_code)


if __name__ == "__main__":
    main()
