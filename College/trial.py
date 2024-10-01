import tkinter
from PIL import Image, ImageTk
import customtkinter as tk  # type: ignore
import os
import datetime
import qrcode

tk.set_default_color_theme("dark-blue")
tk.set_appearance_mode("dark")


class App(tk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.windims = (1500, 770)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_coordinate = int((self.screen_width / 2) - (self.windims[0] / 2))
        y_coordinate = int((self.screen_height / 2) - (self.windims[1] / 2)) - 35

        self.geometry(f"{self.windims[0]}x{self.windims[1]}+{x_coordinate}+{y_coordinate}")
        self.resizable(False, False)
        self.title("Budgeting App")

        icon_path = ImageTk.PhotoImage(file=os.path.join("College", "assets", "icon.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, icon_path)

        self.widgets()

    def widgets(self) -> None:
        credit_button = tk.CTkButton(self, text="Get Total Amount Credited", width=200, height=50, corner_radius=7, command=self.open_credit_window)
        credit_button.place(x=650, y=200)

        debit_button = tk.CTkButton(self, text="Get Total Amount Debited", width=200, height=50, command=self.open_debit_window)
        debit_button.place(x=650, y=300)

        generate_receipt_button = tk.CTkButton(self, text="Generate Receipt", width=200, height=50, command=self.open_receipt_window)
        generate_receipt_button.place(x=650, y=400)

        qr_button = tk.CTkButton(self, text="Generate QR Code", width=200, height=50, command=self.open_qr_window)
        qr_button.place(x=650, y=500)

        transaction_history_button = tk.CTkButton(self, text="Transaction History", width=200, height=50, command=self.open_transaction_history_window)
        transaction_history_button.place(x=650, y=600)

    def open_credit_window(self):
        window = CreditWindow(self)
        self.wait_window(window)

    def open_debit_window(self):
        window = DebitWindow(self)
        self.wait_window(window)

    def open_receipt_window(self):
        window = ReceiptWindow(self)
        self.wait_window(window)

    def open_qr_window(self):
        window = QRWindow(self)
        self.wait_window(window)

    def open_transaction_history_window(self):
        window = TransactionHistoryWindow(self)
        self.wait_window(window)


class BaseToplevel(tk.CTkToplevel):
    def __init__(self, master, title, geometry):
        super().__init__(master)
        self.title(title)
        d1 = geometry[:3]
        d2 = geometry[4:]

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_coordinate = int((self.screen_width / 2) - (int(d1) / 2)) + 100
        y_coordinate = int((self.screen_height / 2) - (int(d2) / 2)) - 35

        self.geometry(f"{d1}x{d2}+{x_coordinate}+{y_coordinate}")

        self.grab_set()
        self.transient(master)

        self.lift()
        self.focus_force()


class CreditWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Get Total Amount Credited", "600x600")
        self.master = master
        self.widgets()

    def widgets(self):
        tk.CTkLabel(self, text="From Date").place(x = 250, y = 7)
        self.from_date_day = self.create_date_dropdown(100, 30)
        self.from_date_month = self.create_month_dropdown(250, 30)
        self.from_date_year = self.create_year_dropdown(400, 30)

        tk.CTkLabel(self, text="To Date").place(x = 250, y = 60)
        self.to_date_day = self.create_date_dropdown(100, 90)
        self.to_date_month = self.create_month_dropdown(250, 90)
        self.to_date_year = self.create_year_dropdown(400, 90)

        self.name = tk.CTkEntry(self, placeholder_text="Person's Name", width=400, height=30)
        self.name.place(x = 110, y = 140)

        self.phone = tk.CTkEntry(self, placeholder_text="Phone Number", width=400, height=30)
        self.phone.place(x = 110, y = 190)

        self.account = tk.CTkEntry(self, placeholder_text="Account Number", width=400, height=30)
        self.account.place(x = 110, y = 240)

        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID", width=400, height=30)
        self.transaction_id.place(x = 110, y = 290)

        submit_button = tk.CTkButton(self, text="Submit", command=self.submit)
        submit_button.place(x = 265, y = 340)

        self.result_text = tk.CTkTextbox(self, width=435, height=150)
        self.result_text.place(x = 100, y = 380)

    def create_date_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(1, 32)])
        dropdown.place(x =  x1, y = y1)

        return dropdown

    def create_month_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        dropdown.place(x = x1,  y = y1)

        return dropdown

    def create_year_dropdown(self, x1, y1):
        current_year = datetime.datetime.now().year
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(current_year - 10, current_year + 1)])
        dropdown.place(x = x1, y = y1)
        return dropdown

    def submit(self):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", "Total credited amounts logic goes here.")


class DebitWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Get Total Amount Debited", "600x600")
        self.master = master
        self.widgets()

    def widgets(self):
        tk.CTkLabel(self, text="From Date").place(x = 250, y = 7)
        self.from_date_day = self.create_date_dropdown(100, 30)
        self.from_date_month = self.create_month_dropdown(250, 30)
        self.from_date_year = self.create_year_dropdown(400, 30)

        tk.CTkLabel(self, text="To Date").place(x = 250, y = 60)
        self.to_date_day = self.create_date_dropdown(100, 90)
        self.to_date_month = self.create_month_dropdown(250, 90)
        self.to_date_year = self.create_year_dropdown(400, 90)

        self.name = tk.CTkEntry(self, placeholder_text="Person's Name", width=400, height=30)
        self.name.place(x = 110, y = 140)

        self.phone = tk.CTkEntry(self, placeholder_text="Phone Number", width=400, height=30)
        self.phone.place(x = 110, y = 190)

        self.account = tk.CTkEntry(self, placeholder_text="Account Number", width=400, height=30)
        self.account.place(x = 110, y = 240)

        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID", width=400, height=30)
        self.transaction_id.place(x = 110, y = 290)

        submit_button = tk.CTkButton(self, text="Submit", command=self.submit)
        submit_button.place(x = 265, y = 340)

        self.result_text = tk.CTkTextbox(self, width=435, height=150)
        self.result_text.place(x = 100, y = 380)

    def create_date_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(1, 32)])
        dropdown.place(x =  x1, y = y1)

        return dropdown

    def create_month_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        dropdown.place(x = x1,  y = y1)

        return dropdown

    def create_year_dropdown(self, x1, y1):
        current_year = datetime.datetime.now().year
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(current_year - 10, current_year + 1)])
        dropdown.place(x = x1, y = y1)
        return dropdown

    def submit(self):
        self.result_text.delete("1.0", "end")
        # Here you would add the logic to calculate total debited amounts based on the selected date range
        self.result_text.insert("1.0", "Total debited amounts logic goes here.")


class ReceiptWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Generate Receipt", "600x600")
        self.master = master
        self.widgets()


    def widgets(self):
        tk.CTkLabel(self, text="Date").place(x = 250, y = 60)
        self.to_date_day = self.create_date_dropdown(100, 90)
        self.to_date_month = self.create_month_dropdown(250, 90)
        self.to_date_year = self.create_year_dropdown(400, 90)

        self.transaction_type = tk.CTkOptionMenu(self, values=["Credit", "Debit"])
        self.transaction_type.place(x = 110, y = 190)

        self.amount = tk.CTkEntry(self, placeholder_text="Amount", width=400, height=30)
        self.amount.place(x = 110, y = 240)

        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID", width=400, height=30)
        self.transaction_id.place(x = 110, y = 290)

        submit_button = tk.CTkButton(self, text="Submit", command=self.generate_receipt)
        submit_button.place(x = 265, y = 340)

        self.receipt_text = tk.CTkTextbox(self, width=435, height=150)
        self.receipt_text.place(x = 100, y = 380)

    def generate_receipt(self):
        def get_date():
            day = self.to_date_day.get()  
            month = self.to_date_month.get()
            year = self.to_date_year.get()  

            month_mapping = {
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
            }

            month_number = month_mapping[month]
            
            date_string = f"{year}-{month_number:02d}-{day.zfill(2)}" 

            date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            day_name = date.strftime('%A')

            return date_string, day_name

        receipt = f"""
        Under 25 Club BNMIT
        ------------------
        Receipt No: {datetime.datetime.now().strftime('%Y%m%d%H%M%S')}
        Date: {get_date()[0]}
        Day: {get_date()[1]}
        
        Transaction Type: {self.transaction_type.get()}
        Amount: ₹{self.amount.get()}
        
        Details: {self.transaction_id.get()}
        
        Thank you for your transaction.
        """
        self.receipt_text.delete("1.0", "end")
        self.receipt_text.insert("1.0", receipt)

    def create_date_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(1, 32)])
        dropdown.place(x =  x1, y = y1)

        return dropdown

    def create_month_dropdown(self, x1, y1):
        dropdown = tk.CTkOptionMenu(self, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        dropdown.place(x = x1,  y = y1)

        return dropdown

    def create_year_dropdown(self, x1, y1):
        current_year = datetime.datetime.now().year
        dropdown = tk.CTkOptionMenu(self, values=[str(i) for i in range(current_year - 10, current_year + 1)])
        dropdown.place(x = x1, y = y1)
        return dropdown


class QRWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Generate QR Code", "700x700")
        self.widgets()

    def widgets(self):
        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID or Name", width = 400, height = 30)
        self.transaction_id.pack(pady=15)

        generate_button = tk.CTkButton(self, text="Generate QR Code", command=self.generate_qr)
        generate_button.pack(pady=20)

        self.qr_image = tk.CTkLabel(self, text="")
        self.qr_image.pack(pady=10)

    def generate_qr(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"Payment verified: {self.transaction_id.get()}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        photo = ImageTk.PhotoImage(img)  
        
        self.qr_image.configure(image=photo)
        self.qr_image.image = photo  


class TransactionHistoryWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Transaction History", "600x400")
        self.transaction_data = self.get_transaction_data()
        self.widgets()

    def get_transaction_data(self):
        return [("Alice", "C"), ("Bob", "D"), ("Charlie", "C"), ("David", "D")]

    def widgets(self):
        self.result_text = tk.CTkTextbox(self, width=350, height=200)
        self.result_text.pack(pady=15)

        python_list = [f"'{name}' for {type_}" for name, type_ in self.transaction_data]
        
        self.result_text.insert("end", "Transaction History: \n")
        for idx, (name, type_) in enumerate(self.transaction_data, start=1):
            self.result_text.insert("end", f"{idx}. {name} - {'Credit' if type_ == 'C' else 'Debit'}\n")

        return python_list


if __name__ == "__main__":
    app = App()
    app.mainloop()
