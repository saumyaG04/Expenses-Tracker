import tkinter as tk
from tkinter import messagebox

# Functions to handle expenses
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))

def update_expense_list(expenses_listbox, expenses):
    expenses_listbox.delete(0, tk.END)
    for expense in expenses:
        expenses_listbox.insert(tk.END, f"Amount: {expense['amount']}, Category: {expense['category']}")

def add_expense_gui(expenses, amount_entry, category_entry, expenses_listbox):
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        if category == "":
            raise ValueError("Category cannot be empty")
        add_expense(expenses, amount, category)
        update_expense_list(expenses_listbox, expenses)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

def show_total_expenses(expenses):
    total = total_expenses(expenses)
    messagebox.showinfo("Total Expenses", f"Total Expenses: {total}")

def filter_expenses_gui(expenses, category_entry, expenses_listbox):
    category = category_entry.get()
    if category == "":
        messagebox.showerror("Input Error", "Category cannot be empty")
        return
    filtered_expenses = filter_expenses_by_category(expenses, category)
    if not filtered_expenses:
        messagebox.showinfo("Filter Result", f"No expenses found for category '{category}'")
    else:
        update_expense_list(expenses_listbox, filtered_expenses)

# Main function to create the UI
def main():
    expenses = []

    root = tk.Tk()
    root.title("Expense Tracker")
    root.geometry("400x400")

    # UI elements
    tk.Label(root, text="Amount").pack(pady=5)
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)

    tk.Label(root, text="Category").pack(pady=5)
    category_entry = tk.Entry(root)
    category_entry.pack(pady=5)

    # Expense listbox
    expenses_listbox = tk.Listbox(root, width=50, height=10)
    expenses_listbox.pack(pady=10)

    # Buttons
    tk.Button(root, text="Add Expense", command=lambda: add_expense_gui(expenses, amount_entry, category_entry, expenses_listbox)).pack(pady=5)
    tk.Button(root, text="Show Total Expenses", command=lambda: show_total_expenses(expenses)).pack(pady=5)
    tk.Button(root, text="Filter by Category", command=lambda: filter_expenses_gui(expenses, category_entry, expenses_listbox)).pack(pady=5)
    tk.Button(root, text="Quit", command=root.quit).pack(pady=10)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()