import re
import pdfplumber
from datetime import datetime

class Parser:
    def __init__(self, pdf_file_path="file3.pdf") -> None:
        self.total_credit = 0
        self.total_debit = 0

        # Adjusted patterns to better match potential formats
        self.credit_pattern = r'CREDIT\s+₹([0-9,]+)\s+on\s+(\d{1,2}/\d{1,2}/\d{4})\s+from\s+([\w\s]+)'
        self.debit_pattern = r'DEBIT\s+₹([0-9,]+)\s+on\s+(\d{1,2}/\d{1,2}/\d{4})\s+received\s+from\s+([\w\s]+)'  
        
        self.pdf_file_path = pdf_file_path  

    def _is_date_in_range(self, date_str, start_date, end_date):
        """Check if the date_str is within the start_date and end_date."""
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return start_date <= date_obj <= end_date

    def credit(self, name=None, start_date=None, end_date=None):
        start_date = datetime.strptime(start_date, '%d/%m/%Y') if start_date else None
        end_date = datetime.strptime(end_date, '%d/%m/%Y') if end_date else None
        
        with pdfplumber.open(self.pdf_file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  # Check if text extraction was successful
                    # Extract credits
                    credits = re.findall(self.credit_pattern, text)
                    for credit, date, person in credits:
                        if (name is None or name.lower() in person.lower()) and \
                           (not start_date or not end_date or self._is_date_in_range(date, start_date, end_date)):
                            self.total_credit += int(credit.replace(",", ""))

    def debit(self, name=None, start_date=None, end_date=None):
        start_date = datetime.strptime(start_date, '%d/%m/%Y') if start_date else None
        end_date = datetime.strptime(end_date, '%d/%m/%Y') if end_date else None
        
        with pdfplumber.open(self.pdf_file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  # Check if text extraction was successful
                    # Extract debits
                    debits = re.findall(self.debit_pattern, text)
                    for debit, date, person in debits:
                        if (name is None or name.lower() in person.lower()) and \
                           (not start_date or not end_date or self._is_date_in_range(date, start_date, end_date)):
                            self.total_debit += int(debit.replace(",", ""))

    def get_total(self):
        return self.total_credit, self.total_debit

    def print_results(self):
        print(f"Total Credit: ₹{self.total_credit}")
        print(f"Total Debit: ₹{self.total_debit}")
        print(f"Net Balance: ₹{self.total_credit - self.total_debit}")

if __name__ == "__main__":
    parser = Parser()
    
    # Example usage
    parser.credit(name="Alice", start_date="01/01/2023", end_date="31/12/2023")  # Replace with desired name and date range
    parser.debit(name="Bob", start_date="01/01/2023", end_date="31/12/2023")      # Replace with desired name and date range
    parser.print_results()
