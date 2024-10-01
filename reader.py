import re
import pdfplumber

total_credit = 0
total_debit = 0

credit_pattern = r'CREDIT\s+₹([0-9,]+)'  
debit_pattern = r'DEBIT\s+₹([0-9,]+)'

pdf_file_path = "file3.pdf"  

with pdfplumber.open(pdf_file_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()

        credits = re.findall(credit_pattern, text)
        for credit in credits:
            total_credit += int(credit.replace(",", ""))

        debits = re.findall(debit_pattern, text)
        for debit in debits:
            total_debit += int(debit.replace(",", ""))

print(f"Total Credit: ₹{total_credit}")
print(f"Total Debit: ₹{total_debit}")

print(total_debit - total_credit)