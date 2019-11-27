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
    test = Contact(name='Test', phone='703-555-1212', address='666 Hell RD, Death Valley, California')
    test.save()
    print("Seeding contacts to start with.")
    
def show_menu():
    menu = input("Please choose one of the follow:\n0. Seed Data (deletes previous data)\n1. Show Contact List\n2. Find Contact by First Name\n3. Add a new contact\n4. Exit\n")
    if menu == "0":
        setup()
        show_menu()
    elif menu == "1":
        data = Contact.select()
        for contact in data:
            print(contact.name, contact.phone, contact.address)
        show_menu()

show_menu()
