from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    address = CharField()

def setup():
    db.drop_tables([Contact])
    db.create_tables([Contact])
    william = Contact(name='William', phone='703-829-5768', address='5311 Manorfield RD, Rockville, MD 20853')
    william.save()
    satan = Contact(name='Satan', phone='703-555-1212', address='666 Hell RD, Death Valley, California')
    satan.save()
    print("Seeding contacts to start with.")

def header():
    print("\033[1;32;40mName\t\tPhone Number\t\tAddress\033[1;37;40m")
    
def show_menu():
    menu = input("\nPlease choose one of the follow:\n0. Seed Data (deletes previous data)\n1. Show Contact List\n2. Find Contact by First Name\n3. Add a new contact\n4. Exit\n")
    print("")
    if menu == "0":
        setup()
        show_menu()
    elif menu == "1":
        header()
        data = Contact.select()
        for contact in data:
            print(f"{contact.name}\t\t{contact.phone}\t\t{contact.address}")
        show_menu()
    elif menu == "2":
        first_name = input("What is the first name of the person you're looking for?\n")
        header()
        data = Contact.select().where(Contact.name % f"%{first_name}%") # Can search for part of word
        for contact in data:
            print(f"{contact.name}\t\t{contact.phone}\t\t{contact.address}")
        show_menu()
    elif menu == "3":
        first_name = input("What is the first name of the person you want to add?\n")
        phone_number = input("Phone number?\n")
        address = input("Phone number?\n")
        new = Contact(name = first_name, phone= phone_number, address = address)
        new.save()
        print("Your new contact is saved")
        show_menu()
    elif menu == "4":
        quit()
    else:
        print("Please enter in a correct menu option.")
        show_menu()

show_menu()