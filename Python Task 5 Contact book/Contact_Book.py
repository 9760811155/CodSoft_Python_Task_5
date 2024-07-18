import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:", fg="blue", font=("Arial", 12))
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=30, fg="black", bg="lightgray")
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone Number:", fg="blue", font=("Arial", 12))
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=30, fg="black", bg="lightgray")
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:", fg="blue", font=("Arial", 12))
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=30, fg="black", bg="lightgray")
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:", fg="blue", font=("Arial", 12))
        self.address_label.pack()
        self.address_entry = tk.Entry(root, width=30, fg="black", bg="lightgray")
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, fg="white", bg="green")
        self.add_button.pack()

        self.search_label = tk.Label(root, text="Search:", fg="blue", font=("Arial", 12))
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=30, fg="black", bg="lightgray")
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_contact, fg="white", bg="blue")
        self.search_button.pack()

        self.contacts_listbox = tk.Listbox(root, width=40, fg="black", bg="lightgray")
        self.contacts_listbox.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, fg="white", bg="orange")
        self.update_button.pack()
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, fg="white", bg="red")
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Name and phone number are required")

    def search_contact(self):
        search_term = self.search_entry.get()
        results = [name for name in self.contacts if search_term in name or search_term in self.contacts[name]["phone"]]
        self.contacts_listbox.delete(0, tk.END)
        for result in results:
            self.contacts_listbox.insert(tk.END, f"{result} - {self.contacts[result]['phone']}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.contacts_listbox.get(selected_index)
            name = name.split(" - ")[0]
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            self.contacts_listbox.delete(selected_index)
            self.contacts_listbox.insert(selected_index, f"{name} - {self.contacts[name]['phone']}")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.contacts_listbox.get(selected_index)
            name = name.split(" - ")[0]
            del self.contacts[name]
            self.contacts_listbox.delete(selected_index)

root = tk.Tk()
root.title("Contact Book")
root.configure(background="lightblue")
contact_book = ContactBook(root)
root.mainloop()