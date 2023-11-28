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



class parkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        x = input('Would you like to park in this garage?(yes/no)')
        # parkingSpaces = 40
        # tickets = 40 
        if x == 'yes':
            print('Please take the ticket. You have fifteen minutes.')
            self.parkingSpaces - 1
            self.tickets - 1
        else: 
            print('Have a nice day')
    
    def payForParking(self):
        self.payment = input('It will be five dollars')
        if int(self.payment) >= 5:
            print('Thank you, have a nice day.')
            self.parkingSpaces + 1
            self.tickets + 1
        else:
            input('Something is wrong with your payemnt, please try again.')


mall_lot = parkingGarage(40, 40, {})

mall_lot.takeTicket()

