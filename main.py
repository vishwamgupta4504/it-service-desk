from crud import create_ticket, view_ticket

def show_menu():
    print("=================")
    print("1. Create tickets")
    print("2. view tickets")
    print("3. Search tickets")
    print("4. Manage assets")
    print("5. Reports")
    print("6. Exit")

while True:
    show_menu()    

    choice=int(input("Enter your choice number:- "))

    if choice==1:
        print("create ticket selected")
        create_ticket()
    elif choice==2:
        print("View ticket selected")
        view_ticket()
    elif choice==3    :
        print("Search ticket selected")
    elif choice==4    :
        print("Manage asset selected")
    elif choice==5    :
        print("Reports selected")
    elif choice==6    :
        print("Thanks for visit it-service-desk!!!")
        break
    else:
        print("invalid choice: please try again.")