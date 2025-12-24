class Contact:
    def __init__(self,name, email, phone_number):
        self.name = name
        self.email = email
        self.phone = phone_number
        
    def diplay_info(self, name , email, phone_number):
        if name != "":
            print(f"Name: {self.name}")
        if email != "":
            print(f"Email: {self.email}")
        if phone_number != "":
            print(f"Phone: {self.phone}")

name, email , phone = input("Enter your name, email, and phone number please use comar to separate your inputs: ").split(",")
user_input = Contact(name, email, phone)
user_input.diplay_info(name, email, phone)