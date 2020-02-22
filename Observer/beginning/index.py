class Reader:
    def __init__(self, name):
        self.name = name

    def publish(self, reason):
        print(reason + " from " + self.name + " was just published")


class Magazine:
    def __init__(self, name):
        self.name = name

    def publish(self, reason):
        print(reason + " from " + self.name + " was just published")


class Publisher:
    def __init__(self):
        editions = []

arctechnica = Magazine('Arc Technica');
newYorker = Magazine('New Yorker');

jane = Reader('Jane')
phoebe = Reader('Phoebe')
eve = Reader('Eve')
lily = Reader('Lily')
pam = Reader('Pam')

condeNast = Publisher('Conde Nast');