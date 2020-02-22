class Reader:
    def __init__(self, name):
        self.name = name

    def notify(self, magazine, reason):
        print("Dear " + self.name + " , there is a " + reason + " edition from " + magazine + " has been published")


class Magazine:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def publish(self, reason):
        # print(reason + " from " + self.name + " was just published")
        for subscriber in self.subscribers:
            subscriber.notify(self.name, reason)


class Publisher:
    def __init__(self, name):
        self.name = name
        self.editions = []

    def notify(self, magazine, reason):
        self.editions.append({magazine, reason})


arctechnica = Magazine('Arc Technica')
newYorker = Magazine('New Yorker')

jane = Reader('Jane')
phoebe = Reader('Phoebe')
eve = Reader('Eve')
lily = Reader('Lily')
pam = Reader('Pam')

condeNast = Publisher("Conde Nast")

arctechnica.subscribe(jane)
arctechnica.subscribe(phoebe)
arctechnica.subscribe(eve)
newYorker.subscribe(eve)
newYorker.subscribe(lily)
newYorker.subscribe(pam)
arctechnica.subscribe(condeNast)
newYorker.subscribe(condeNast)

arctechnica.publish('February')
newYorker.publish('February')
newYorker.publish('Saint Valentines Special')
arctechnica.publish('March')

print(condeNast.editions)