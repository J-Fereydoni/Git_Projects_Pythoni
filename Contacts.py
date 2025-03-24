import json
Help = """
1:Add
2:Edit
3:DElete
4:Search
5:Show Contact
6:Save & Exit
"""

def add_contact(phone_book, name, phone):
    for contact in phone_book:
        if contact["name"] == name:
            print(f"//Added exit ...//{name}")
            return
    phone_book.append({"name": name, "phone": phone})
    print(f"name {name} Successful Contact")

def edit_contact(phone_book, name, newphone):
    for contact in phone_book:
        if contact["name"] == name:
            contact["phone"] = newphone
            print(f"Replace{contact["phone"] in {newphone}}")
            return
        
    
def delete_contact(phone_book, name):
    for contact in phone_book:
        if contact["name"] == name:
            phone_book.remove(contact)
            print(f"Deleting({name}as phone_book) #{phone_book}")
            return
        
def search_contact(phone_book, name):
    for contact in phone_book:
        if contact["name"].lower() == name.lower():
            print(f"name: {contact["name"]} -- phone: {contact["phone"]}")
            return

def show_contact(phone_book):
    if not phone_book:
        print("Empty File ... Not Available ...")
    for contact in phone_book:
        print(f"[*] naame: {contact["name"]} phone: {contact["phone"]}")    
                
def seve_exit(phone_book):
    with open("Lists.txt", "w") as file:
        json.dump(phone_book, file)
        print(f"Contact Added To File Txt {phone_book}")
        exit()
        return

def load_contact(filename="Lists.txt"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
        
    
def main():
    phone_book = load_contact()
    while True:
        print(Help)
        choice = input("Please Select Number 1_6: ")
        if choice == "1":
            name = input("please Insert Name: ")
            phone = input("please Insert phone: ")
            add_contact (phone_book, name, phone)
        elif choice == "2":
            name = input("please Insert Name: ")
            newphone = input("please Insert phone: ")
            edit_contact (phone_book, name, newphone)
        elif choice == "3":
            name = input("please Insert Name: ")
            delete_contact(phone_book, name)
        elif choice == "4":
            name = input("please Insert Name: ")
            search_contact(phone_book, name)
        elif choice == "5":
            show_contact(phone_book)
        elif choice == "6":
            seve_exit(phone_book)
        else:
            print("Else ...")
            
if __name__ == "__main__":
    main()
            
