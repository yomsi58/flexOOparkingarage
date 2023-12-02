#  takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary



class Parking_garage():
    def __init__(self):
        self.parking_spaces = [1,2,3,4,5,6,7,8,9,10]
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.issued_tickets = {}
    
    def takeTicket(self):
        if len(self.tickets) < 1:
            print("Parking garage is full!!")
            return
            
        number=self.tickets.pop(0)
        print(number)
        
        self.issued_tickets[number] = 'not paid'
        print(self.issued_tickets)
       
        self_parking_spaces=self.parking_spaces.pop(0)
        print(f"Parking spaces available are: {self.parking_spaces}. ")
        
        
    def payForParking(self):
        number=int(input("Please enter in your ticket number: "))
        if number in self.tickets:
            print("please select a valid ticket")
            return
        paid_ticket=(input("Please pay for the ticket. "))
        if int(paid_ticket) <1:
            print(input("Please pay for your ticket. "))
        else:
            self.issued_tickets[number] = 'paid'
            print(self.issued_tickets)
            print(f" Ticket {number} has been paid. You have 15 minutes to leave.")


    def leaveGarage(self):
        number=int(input("Please scan the ticket: "))
        if number in self.tickets:
            print("please select a valid ticket")
            return
        if self.issued_tickets[number] == 'paid':
            self.issued_tickets.pop(number)
            print(self.issued_tickets)
            print("Thank You, have a nice day")
            
            self.parking_spaces.append(number)
            self.tickets.append(number)
        else:
            print("Please pay for ticket!!")
            
        

class UI():
    def __init__(self, person):
        self.person = person
    
    def run_program(self):
        while True:
            response = input(f"Hello, What would you like to do? Park, pay, leave, or quit?")
            if response.lower() == 'quit':
                print(f"Hope to see you soon!!")
                break
            elif response.lower() == 'park':
                print("Please take ticket #")
                self.person.takeTicket()
            elif response.lower() == 'pay':
                self.person.payForParking()
            elif response.lower() == 'leave':
                self.person.leaveGarage()
           
            
#Driver Code
my_parking = Parking_garage()
ui = UI(my_parking)
ui.run_program()

