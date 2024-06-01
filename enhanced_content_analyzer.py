
import os
from typing import Union
import pandas as pd
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
from docx import Document

class EnhancedContentAnalyzer:
    def __init__(self):
        pass

    def extract_text_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return text

    def extract_text_docx(self, file_path: str) -> str:
        doc = Document(file_path)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    def extract_text_xlsx(self, file_path: str) -> Union[str, None]:
        try:
            df = pd.read_excel(file_path)
            return df.to_csv(index=False)
        except Exception as e:
            return None

    def extract_text_image(self, file_path: str) -> str:
        text = pytesseract.image_to_string(Image.open(file_path))
        return text

    # Placeholder for extract_text method that determines file type and calls the appropriate extraction method
    def extract_text(self, file_path: str) -> str:
        # Determine file extension and call the respective method
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.pdf':
            return self.extract_text_pdf(file_path)
        elif file_extension.lower() in ['.doc', '.docx']:
            return self.extract_text_docx(file_path)
        elif file_extension.lower() in ['.xls', '.xlsx']:
            return self.extract_text_xlsx(file_path)
        elif file_extension.lower() in ['.jpg', '.jpeg', '.png', '.tiff']:
            return self.extract_text_image(file_path)
        else:
            return "Unsupported file type."

def main():
    analyzer = EnhancedContentAnalyzer()
    # Example usage
    file_path = "/path/to/file"
    print(analyzer.extract_text(file_path))

if __name__ == "__main__":
    main()
