ticket_number=1
tickets=[]
assets=[]

def create_ticket():
    global ticket_number

    ticket_id=f"Inc-{ticket_number:03d}"

    employee_details= {
        "ticket_id": ticket_id,
        "employee name": input("Enter employee name: "),
        "problem": input("Enter your problem: "),
        "category": input("Enter category: "),
        "priority": input("Enter priority: "),
        "status": "open"
    }

    print("Ticket created successfully.")
    print("Ticket ID:", ticket_id)
    print(employee_details)
    tickets.append(employee_details)
    ticket_number+=1

def view_ticket():
    if not tickets:
        print("No ticket found. ")
    else:
        for ticket in tickets:
            print(ticket)    


def search_ticket():
    Enter_id=input("Enter ticket id: ")

    for ticket in tickets:
        if Enter_id == ticket["ticket_id"]:
            print("Ticket found")
            print(ticket)
            break
    else:
        print("No ticket found.")    

def manage_assets():
    asset={
        "asset_it":input("Enter asset id: "),
        "asset_type": input("Enter asset type: "),
        "brand": input("Enter brand: "),
        "serial_number": input("Enter serial number: "),
        "assigned_to": input("Enter Assigned employee: "),
        "status": input("Enter status: ")
    }

    assets.append(asset)
    print("Asset edited successfully")