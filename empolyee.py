empolyee = []

def add_empolyee():
  name = input("enter name :")
  id = input("enter id :")
  empolyee.append({"name":name,"id":id})       
  print("empolyee added successfully!\n")   

def display_empolyee():
    if not empolyee:
        print("no record found\n")
    else:
       for e in empolyee:
              print(f"name: {e['name']}, id: {e['id']}")      
    print()  
def search_empolyee():
    id = input("enter id to serach:")
    for e in empolyee:
        if e["id"] == id:
            print(f"found: {e}")
            return
    print("empolyee not found\n")   

def delete_empolyee():
    id = input("enter id to delete:")
    for e in empolyee:
        if e["id"] == id:
            empolyee.remove(e)
            print("deleted successfully\n")
            return
        print("empolyee not found\n")
while True:
            print("1.add empolyee:")
            print("2.display empolyee:")
            print("3.search empolyee:")
            print("4.delete empolyee:")
            print("5.exit:")
           
            choice = input("enter choice:")
             
            if choice == "1":
                 add_empolyee()
            elif choice =="2":
                 display_empolyee()     
            elif choice == "3":
                 search_empolyee
            elif choice == "4":
                 delete_empolyee
            elif choice == "5":
                 break
            else:
                 print("invalid choice\n")     










