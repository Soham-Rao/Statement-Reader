import re
import pdfplumber

class Parser:
    def __init__(self) -> None:

        self.total_credit = 0
        self.total_debit = 0

        self.credit_pattern = r'CREDIT\s+₹([0-9,]+)'  
        self.debit_pattern = r'DEBIT\s+₹([0-9,]+)'

        self.pdf_file_path = "file3.pdf"  

    def credit(self):
        with pdfplumber.open(self.pdf_file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                credits = re.findall(self.credit_pattern, text)
                for credit in credits:
                    self.total_credit += int(credit.replace(",", ""))

    def debit(self):
        with pdfplumber.open(self.pdf_file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                debits = re.findall(self.debit_pattern, text)
                for debit in debits:
                    self.total_debit += int(debit.replace(",", ""))

    def print(self):
        print(f"Total Credit: ₹{self.total_credit}")
        print(f"Total Debit: ₹{self.total_debit}")

        print(self.total_debit - self.total_credit)
        
if __name__ == "__main__":
    parser = Parser()
    parser.print()