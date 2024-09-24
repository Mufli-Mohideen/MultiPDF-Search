import PyPDF2
import os

def search_pdfs(directory, search_term):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, "rb") as pdf_file:
                        reader = PyPDF2.PdfReader(pdf_file)
                        for page in reader.pages:
                            if search_term.lower() in page.extract_text().lower():
                                print(f"'{search_term}' found in {filename}")
                except Exception as e:
                    print(f"Could not read {filename}: {e}")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

directory = r"C:\Users\Desktop\ss"  # You can replace this with a dynamic path
search_term = "search word"  # Search term can also be replaced

search_pdfs(directory, search_term)
