import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import db

# Create the main window
root = ctk.CTk()
root.title("ATM Simulator")
root.geometry("600x400")

# Load background image
bg_image = ctk.CTkImage(Image.open("img.png"), size=(600, 400))
bg_label = ctk.CTkLabel(root, text="", image=bg_image)
bg_label.grid(row=0, column=0, rowspan=7, columnspan=3, sticky="nsew")

# Create input fields
id_label = ctk.CTkLabel(root, text="Account ID:", font=("Arial", 12))
id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
id_entry = ctk.CTkEntry(root, font=("Arial", 12))
id_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = ctk.CTkLabel(root, text="Name:", font=("Arial", 12))
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = ctk.CTkEntry(root, font=("Arial", 12))
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Function to create a new account
def create_account():
    id = id_entry.get()
    name = name_entry.get()
    initial_balance = ctk.CTkInputDialog(text="Enter the initial balance:", title="Create Account").get_input()
    if initial_balance and initial_balance.replace('.', '', 1).isdigit() and float(initial_balance) >= 0:
        account_id = db.add_account(int(id), name, float(initial_balance))
        if account_id is not None:
            messagebox.showinfo("Success", f"Account created for {name} with an initial balance of ${float(initial_balance):.2f}. Your account ID is {account_id}.")
        else:
            messagebox.showerror("Error", "Error creating account.")
    else:
        messagebox.showerror("Error", "Invalid initial balance.")

# Function to remove an account
def remove_account():
    account_id = id_entry.get()
    name = name_entry.get()
    if account_id.isdigit() and db.remove_account(int(account_id), name):
        messagebox.showinfo("Success", f"Account for {name} has been removed.")
    else:
        messagebox.showerror("Error", "Account not found.")

# Function to check balance
def check_balance():
    account_id = id_entry.get()
    name = name_entry.get()
    if account_id.isdigit():
        balance = db.get_balance(int(account_id), name)
        if balance is not None:
            messagebox.showinfo("Balance", f"Your balance is: ${balance:.2f}")
        else:
            messagebox.showerror("Error", "Account not found.")
    else:
        messagebox.showerror("Error", "Invalid account ID.")

# Function to deposit money
def deposit():
    account_id = id_entry.get()
    name = name_entry.get()
    amount = ctk.CTkInputDialog(text="Enter the amount to deposit:", title="Deposit").get_input()
    if account_id.isdigit() and amount and amount.replace('.', '', 1).isdigit() and float(amount) > 0:
        if db.update_balance(int(account_id), name, float(amount)):
            messagebox.showinfo("Success", f"${float(amount):.2f} deposited successfully.")
        else:
            messagebox.showerror("Error", "Account not found.")
    else:
        messagebox.showerror("Error", "Invalid input.")

# Function to withdraw money
def withdraw():
    account_id = id_entry.get()
    name = name_entry.get()
    if account_id.isdigit():
        balance = db.get_balance(int(account_id), name)
        if balance is not None:
            amount = ctk.CTkInputDialog(text="Enter the amount to withdraw:", title="Withdraw").get_input()
            if amount and amount.replace('.', '', 1).isdigit() and float(amount) > 0 and float(amount) <= balance:
                if db.update_balance(int(account_id), name, -float(amount)):
                    messagebox.showinfo("Success", f"${float(amount):.2f} withdrawn successfully.")
                else:
                    messagebox.showerror("Error", "Account not found.")
            else:
                messagebox.showerror("Error", "Invalid amount or insufficient balance.")
        else:
            messagebox.showerror("Error", "Account not found.")
    else:
        messagebox.showerror("Error", "Invalid account ID.")

# Create buttons
create_account_button = ctk.CTkButton(root, text="Create Account", command=create_account, font=("Arial", 12))
create_account_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

remove_account_button = ctk.CTkButton(root, text="Remove Account", command=remove_account, font=("Arial", 12))
remove_account_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

balance_button = ctk.CTkButton(root, text="Check Balance", command=check_balance, font=("Arial", 12))
balance_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

deposit_button = ctk.CTkButton(root, text="Deposit", command=deposit, font=("Arial", 12))
deposit_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

withdraw_button = ctk.CTkButton(root, text="Withdraw", command=withdraw, font=("Arial", 12))
withdraw_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

# Create the table if it doesn't exist
db.create_table()

# Start the main loop
root.mainloop()
