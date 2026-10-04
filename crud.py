ticket_number=1
tickets=[]
def create_ticket():
    global ticket_number

    ticket_id=f"Inc-{ticket_number:03d}"

    employee_details= {
        "ticket_id": ticket_id,
        "employee name": input("Enter employee name: "),
        "problem": input("Enter your problem: "),
        "category": input("Enter category: "),
        "priority": input("Enter priority: ")
    }

    print("Ticket created successfully.")
    print("Ticket ID:", ticket_id)
    print(employee_details)
    tickets.append(employee_details)

def view_ticket()    :
    if not tickets:
        print("No ticket found. ")
    else:
        for ticket in tickets:
            print(ticket)    