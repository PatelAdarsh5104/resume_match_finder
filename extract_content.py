from pypdf import PdfReader
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader


# def extract_webpage_content(url):
#     # Making a GET request
#     r = requests.get(url)

#     # check status code for response received
#     if r.status_code == 200:
#         # Parsing the HTML
#         soup = BeautifulSoup(r.content, 'html.parser')
#         return soup.prettify()
#     else:
#         return None

# Example usage
# url = 'https://jobs.careers.microsoft.com/global/en/job/1795798/Software-Engineer-II'
# webpage_content = extract_webpage_content(url)
# if webpage_content:
#     print(webpage_content)


def extract_pdf_content(pdf_path):
    reader = PdfReader(pdf_path)
    # print(len(reader.pages))
    page = reader.pages[0]
    text = page.extract_text()
    # print(text)
    return text


def extract_webpage_content(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs


from docx import Document
def extract_docx_content(doc):

    doc = Document(doc)

    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
        
    return text