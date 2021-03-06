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
    satan = Contact(name='John', phone='703-555-1212', address='555 Pike RD, Red Oak, California')
    satan.save()
    print("Seeding contacts to start with.")

def header():
    print("\n\033[1;32;40mName\t\tPhone Number\t\tAddress\033[1;37;40m")
    
def menu_switch():
    menu = input("\nPlease choose one of the follow:\n1. Show Contact List\n2. Find Contact by First Name\n3. Add a new contact\n4. Exit\n5. Seed Data (deletes previous data)\n")
    if menu.isdigit() == False: 
        menu = 0

    def Reset():
        setup()
    
    def Show_List():
        header()
        data = Contact.select()
        for contact in data:
            print(f"{contact.name}\t\t{contact.phone}\t\t{contact.address}")
    
    def Find_Name():
        first_name = input("\nWhat is the first name of the person you're looking for?\n")
        header()
        data = Contact.select().where(Contact.name % f"%{first_name}%") # Can search for part of word
        for contact in data:
            print(f"{contact.name}\t\t{contact.phone}\t\t{contact.address}")

    def Add_New():
        first_name = input("What is the first name of the person you want to add?\n")
        phone_number = input("Phone number?\n")
        address = input("Address?\n")
        new = Contact(name = first_name, phone= phone_number, address = address)
        new.save()
        print("Your new contact is saved")

    def End():
        quit()
    
    def default():
        print("\nYou have input an incorrect option")

    dict = {
        1: Show_List,
        2: Find_Name,
        3: Add_New,
        4: End,
        5: Reset
    }

    dict.get(int(menu), default)()
    menu_switch()

menu_switch()