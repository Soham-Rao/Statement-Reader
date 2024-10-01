import tkinter
from PIL import Image, ImageTk 
import customtkinter as tk #type: ignore
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
        x_coordinate = int((self.screen_width/2)-(self.windims[0]/2))
        y_coordinate = int((self.screen_height/2)-(self.windims[1]/2))-35

        self.geometry(f"{self.windims[0]}x{self.windims[1]}+{x_coordinate}+{y_coordinate}")
        self.resizable(False, False)
        self.title("Budgeting App")

        icon_path = ImageTk.PhotoImage(file = os.path.join("College", "assets", "icon.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, icon_path)
    
        #self.images()
        self.widgets()

    def images(self) -> None:
        
        global bg_img
        
        canvas = tk.CTkCanvas(self, width = self.windims[0]*2, height = self.windims[1]*2, bd=0, highlightthickness=0)
        canvas.place(x = 0, y = 0)        
        
        bg_img = Image.open(os.path.join("College", "assets", "bg.png"))
        bg_img = ImageTk.PhotoImage(bg_img.resize((self.windims[0]*2, self.windims[1]*2)))
        canvas.create_image(0, 0, image=bg_img, anchor='nw')


    def widgets(self) -> None:
        credit_button = tk.CTkButton(self, text="Get Total Amount Credited", width = 200, height = 50, corner_radius = 7, command=self.open_credit_window)
        credit_button.place(x=650, y=200)

        debit_button = tk.CTkButton(self, text="Get Total Amount Debited", width = 200, height = 50, command=self.open_debit_window)
        debit_button.place(x = 650, y = 300)

        generate_receipt_button = tk.CTkButton(self, text="Generate Receipt", width = 200, height = 50, command=self.open_receipt_window)
        generate_receipt_button.place(x = 650, y = 400)

        qr_button = tk.CTkButton(self, text="Generate QR Code", width = 200, height = 50, command=self.open_qr_window)
        qr_button.place(x = 650, y = 500)

        Transaction_History_button = tk.CTkButton(self, text="Transaction History", width = 200, height = 50, command=self.open_transaction_history_window)
        Transaction_History_button.place(x = 650, y = 600)

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
        x_coordinate = int((self.screen_width/2)-(int(d1)/2))+100
        y_coordinate = int((self.screen_height/2)-(int(d2)/2))-35

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
        self.date_range = tk.CTkEntry(self, placeholder_text="Date Range (YYYY-MM-DD to YYYY-MM-DD)", width = 400, height = 30)
        self.date_range.pack(pady=15)

        self.name = tk.CTkEntry(self, placeholder_text="Person's Name", width = 400, height = 30)
        self.name.pack(pady=15)

        self.phone = tk.CTkEntry(self, placeholder_text="Phone Number", width = 400, height = 30)
        self.phone.pack(pady=15)

        self.account = tk.CTkEntry(self, placeholder_text="Account Number", width = 400, height = 30)
        self.account.pack(pady=15)

        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID", width = 400, height = 30)
        self.transaction_id.pack(pady=15)

        submit_button = tk.CTkButton(self, text="Submit", command=self.submit)
        submit_button.pack(pady=20)

        self.result_text = tk.CTkTextbox(self, width=350, height=150)
        self.result_text.pack(pady=10)

    def submit(self):        
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", "HALO")

class DebitWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Get Total Amount Debited", "600x600")
        self.master = master
        self.widgets()

    def widgets(self):
        self.date_range = tk.CTkEntry(self, placeholder_text="Date Range (YYYY-MM-DD to YYYY-MM-DD)", width = 400, height = 30)
        self.date_range.pack(pady=15)

        self.name = tk.CTkEntry(self, placeholder_text="Person's Name", width = 400, height = 30)
        self.name.pack(pady=15)

        self.phone = tk.CTkEntry(self, placeholder_text="Phone Number", width = 400, height = 30)
        self.phone.pack(pady=15)

        self.account = tk.CTkEntry(self, placeholder_text="Account Number", width = 400, height = 30)
        self.account.pack(pady=15)

        self.transaction_id = tk.CTkEntry(self, placeholder_text="Transaction ID", width = 400, height = 30)
        self.transaction_id.pack(pady=15)

        submit_button = tk.CTkButton(self, text="Submit", command=self.submit)
        submit_button.pack(pady=20)

        self.result_text = tk.CTkTextbox(self, width=350, height=150)
        self.result_text.pack(pady=10)

    def submit(self):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", "BYEEEEE")

class ReceiptWindow(BaseToplevel):
    def __init__(self, master):
        super().__init__(master, "Generate Receipt", "500x700")
        self.widgets()

    def widgets(self):
        self.transaction_type = tk.CTkOptionMenu(self, values=["Credit", "Debit"])
        self.transaction_type.pack(pady=15)

        self.amount = tk.CTkEntry(self, placeholder_text="Amount", width = 400, height = 30)
        self.amount.pack(pady=15)

        self.date = tk.CTkEntry(self, placeholder_text="Date (YYYY-MM-DD)", width = 400, height = 30)
        self.date.pack(pady=15)

        self.transaction_details = tk.CTkEntry(self, placeholder_text="Transaction Details", width = 400, height = 30)
        self.transaction_details.pack(pady=15)

        generate_button = tk.CTkButton(self, text="Generate Receipt", command=self.generate_receipt)
        generate_button.pack(pady=20)

        self.receipt_text = tk.CTkTextbox(self, width=350, height=300)
        self.receipt_text.pack(pady=10)

    def generate_receipt(self):
        receipt = f"""
        Under 25 Club BNMIT
        ------------------
        Receipt No: {datetime.datetime.now().strftime('%Y%m%d%H%M%S')}
        Date: {self.date.get()}
        Day: {datetime.datetime.strptime(self.date.get(), '%Y-%m-%d').strftime('%A')}
        
        Transaction Type: {self.transaction_type.get()}
        Amount: ₹{self.amount.get()}
        
        Details: {self.transaction_details.get()}
        
        Thank you for your transaction.
        """
        self.receipt_text.delete("1.0", "end")
        self.receipt_text.insert("1.0", receipt)

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

#__main__#
def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()