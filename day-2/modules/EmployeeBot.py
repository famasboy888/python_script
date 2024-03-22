class EmployeeBot:
    
    def __init__(self, firstN, lastN, lifeSpan):
        self.firstN = firstN
        self.lastN = lastN
        self.lifeSpan = lifeSpan

    def greet(self):
        print(f'Hi there! I\'m {self.firstN} {self.lastN}. I\'ll be happy happy working with you for {self.lifeSpan} year(s).')