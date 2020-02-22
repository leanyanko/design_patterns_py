class Reader:
    def __init__(self, name):
        self.name = name
    #
    # def notify(self, magazine, reason):
    #     print("Dear " + self.name + " , there is a " + reason + " edition from " + magazine + " has been published")

    def notify(self, sender, magazine, name):
        if sender == "publisher":
            print("Dear " + self.name + " , there is a new magazine " + magazine.name + " available for subscription from " + name)
        else:
            print("Dear " + self.name + " , there is a " + name + " edition from " + magazine + " has been published")


class Magazine:
    def __init__(self, name, publisher):
        self.publisher = publisher
        self.name = name
        self.subscribers = []
        publisher.add(self)

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def publish(self, reason):
        for subscriber in self.subscribers:
            subscriber.notify("magazine", self.name, reason)


class Publisher:
    def __init__(self, name):
        self.name = name
        self.editions = []
        self.subscribers = []

    def notify(self, sender,  magazine, reason):
        self.editions.append({magazine, reason})

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def add(self, magazine):
        for subscriber in self.subscribers:
            subscriber.notify("publisher", magazine, self.name)


jane = Reader('Jane')
phoebe = Reader('Phoebe')
eve = Reader('Eve')
lily = Reader('Lily')
pam = Reader('Pam')

condeNast = Publisher("Conde Nast")
arctechnica = Magazine('Arc Technica', condeNast)
newYorker = Magazine('New Yorker', condeNast)

arctechnica.subscribe(jane)
arctechnica.subscribe(phoebe)
arctechnica.subscribe(eve)
newYorker.subscribe(eve)
newYorker.subscribe(lily)
newYorker.subscribe(pam)
arctechnica.subscribe(condeNast)
newYorker.subscribe(condeNast)

condeNast.subscribe(lily)
condeNast.subscribe(pam)
arctechnica.publish('February')
newYorker.publish('February')

vogue = Magazine("vogue", condeNast)


newYorker.publish('Saint Valentines Special')
arctechnica.publish('March')

print(condeNast.editions)