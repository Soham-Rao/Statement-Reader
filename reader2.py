import re
import pdfplumber

total_credit = 0
total_debit = 0
total_from_mom = 0
total_to_vin = 0

credit_pattern = r'CREDIT\s+₹([0-9,]+)'  
debit_pattern = r'DEBIT\s+₹([0-9,]+)'
name = "Mom"
mom_pattern = rf'Received from {name}\s+CREDIT\s+₹([0-9,]+)'
name = "VINAYAKA CONDIMENTS"
vin_pattern = rf'Paid to {name}\s+DEBIT\s+₹([0-9,]+)'

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

        mom_transactions = re.findall(mom_pattern, text)
        for transaction in mom_transactions:
            total_from_mom += int(transaction.replace(",", ""))

        vin_transactions = re.findall(vin_pattern, text)
        for transaction in vin_transactions:
            total_to_vin += int(transaction.replace(",", ""))

#print(f"Total Credit: ₹{total_credit}")
#print(f"Total Debit: ₹{total_debit}")
print(f"Total Received from Mom: ₹{total_from_mom}")
print(f"Total Paid to Vin: ₹{total_to_vin}")
