from random import randint

class Train:
    def __init__(self, trainName, trainNumber, placeFrom, placeTo):
        self.trainName = trainName
        self.trainNumber = trainNumber
        self.placeFrom = placeFrom
        self.placeTo = placeTo

    def ticketBooking(self):
        print(f"ticket in booked in train no {self.trainNumber} from {self.placeFrom} to {self.placeTo}")

    def getStatus(self):
        print(f"train no {self.trainNumber} running late by {randint(1, 5)} hours")

    def getFare(self):
        print(f"Ticket fare in train {self.trainNumber} from {self.placeFrom} to {self.placeTo} fare is {randint(866, 7900)}")

firstTrain = Train("Mahabodhi", 12345, "Delhi", "Kolkata")
firstTrain.ticketBooking()
firstTrain.getFare()
firstTrain.getStatus()