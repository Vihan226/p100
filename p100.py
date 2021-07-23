class Atm(object):
    def __init__(self, cashWithdrawl, balanceEnquiry, cardSwiped, cashedOut):
        self.cashWithdrawl=cashWithdrawl
        self.balanceEnquiry=balanceEnquiry
        self.cardSwiped=cardSwiped
        self.cashedOut= cashedOut

    def checkIn(self):
        print("Please swipe the card to check in!")

    def checkBalance(self):
        print("Checked the balance: $200,000")

    def takingCash(self):
        print("You have taken cahs out of the atm: $50")


quickTouch = Atm("100", "Checked the balance", "2457", "Taken $50")

print(quickTouch.checkBalance())