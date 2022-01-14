import tkinter as tk
from tkinter import BooleanVar, ttk



class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Expenses")
        self.window.geometry("700x600")
        self.window.resizable(0,0)

        self.username_list = ["a"]
        self.password_list = ["a"]

        self.balace = 90

        self.row_first_column = 99

        self.plus = BooleanVar

        self.start_frame()
        self.window.mainloop()


    def start_frame(self):
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

        self.heading_label = ttk.Label(self.window, text="Log-In", font=("", 25))
        self.heading_label.grid(column=1, row=0, sticky=tk.NS, pady=40)

        self.username = ttk.Label(self.window, text="Username:")
        self.username.grid(column=1, row=1, sticky=tk.W, pady=30)

        self.password = ttk.Label(self.window, text="Password:")
        self.password.grid(column=1, row=2, sticky=tk.W)

        self.entry1 = ttk.Entry(self.window)
        self.entry1.grid(column=1, row=1)

        self.entry2 = ttk.Entry(self.window)
        self.entry2.grid(column=1, row=2)

        self.warning = ttk.Label(self.window, text="")
        self.warning.grid(column=1, row=3, sticky= tk.NS, pady=10)

        self.button1 = ttk.Button(self.window, text="Submit", command= self.check_data)
        self.button1.grid(column=1, row=4, sticky=tk.NS)


    def check_data(self):
        username_check = self.entry1.get()
        password_check = self.entry2.get()
        

        if username_check in self.username_list and password_check in self.password_list:
            self.main_frame()
    
        else:
            self.warning.configure(text="Incorrect data! Try again")
            self.entry2.delete(0, tk.END)
            

    def main_frame(self):
        self.username.destroy()
        self.password.destroy()
        self.entry1.destroy()
        self.entry2.destroy()
        self.warning.destroy()
        self.button1.destroy()

        self.heading_label.configure(text="Finance", font=("", 25))

        #First Column
        self.sub_heading1 = ttk.Label(self.window, text="Overview", font=("", 15))
        self.sub_heading1.grid(column=0, sticky=tk.NS, row=1, pady=20)

        self.balance_label = ttk.Label(self.window, text=f"{self.balace}$")
        self.balance_label.grid(column=0, row=2, pady=5, sticky=tk.S)


        #Second Column
        self.sub_heading2 = ttk.Label(self.window, text="Add", font=("", 15))
        self.sub_heading2.grid(column=1, sticky=tk.NS, row=1, pady=20)

        self.add_balance = ttk.Entry(self.window, width=5)
        self.add_balance.grid(column=1, row=2, pady=20, sticky=tk.NS)

        self.add_button = ttk.Button(self.window, text="Add",width=3, command= self.entry_add_balance)
        self.add_button.grid(column=1, row=3, pady=10, sticky=tk.NS)


        #Third Column
        self.sub_heading3 = ttk.Label(self.window, text="Minus", font=("", 15))
        self.sub_heading3.grid(column=2, sticky=tk.NS, row=1, pady=20)

        self.minus_balance = ttk.Entry(self.window, width=5)
        self.minus_balance.grid(column=2, row=2, pady=20, sticky=tk.NS)

        self.minus_button = ttk.Button(self.window, text="Minus",width=4, command= self.entry_minus_balance)
        self.minus_button.grid(column=2, row=3, pady=10, sticky=tk.NS)


    def entry_add_balance(self):
        addjust_balance_user = int(self.add_balance.get())
        self.add_balance.delete(0, tk.END)
        
        self.balace += addjust_balance_user

        self.balance_label.configure(text=f"{self.balace}$")
        
        self.plus = True
        self.changes_label(addjust_balance_user)
        

    def entry_minus_balance(self):
        minus_balance_user = int(self.minus_balance.get())
        self.minus_balance.delete(0, tk.END)
        
        self.balace -= minus_balance_user

        self.balance_label.configure(text=f"{self.balace}$")
        
        self.plus = False
        self.changes_label(minus_balance_user)

        
    def changes_label(self, input):
        self.row_first_column -= 1

        if self.plus:
            new_add_label = ttk.Label(self.window, text=f"+{input}$")
            new_add_label.grid(column=0, row=self.row_first_column,padx=15, sticky=tk.E)

        else:
            new_add_label = ttk.Label(self.window, text=f"-{input}$")
            new_add_label.grid(column=0, row=self.row_first_column,padx=15, sticky=tk.E)


app = App()