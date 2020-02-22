class Event:
    def __init__(self, name, required_experience):
        self.name = name
        self.required_experience = required_experience

    def print(self):
        print(self.name + " requires " + self.required_experience);


class Speaker:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        self.events = []

    def speak(self, event):
        if event.required_experience > self.experience:
            print(self.name + " does not have enough experience to speak at " + event.name)
        else:
            print(self.name + " is speaking at the " + event.name)
            self.experience += event.required_experience
            self.events.append(event)

    def print_status(self):
        print(self.name + " spoke at" + str(len(self.events)) + " events: ")
        for event in self.events:
            print("  * " + event.name)
        print("this speaker has " + str(self.experience) + " level of experience");


dina = Speaker('Dina', 1)
meetup = Event('Meetup', 2)
party = Event('Party', 1)
conference = Event("Conference", 5)

dina.speak(party)
dina.speak(meetup)
dina.speak(conference)

dina.print_status()
