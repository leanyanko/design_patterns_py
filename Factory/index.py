class Member:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def __str__(self):
        return self.name + " who works as a" + self.job_title + " is now a member of our community\n"


class Organizer:
    def __init__(self, name, job_title, responsibility):
        self.name = name
        self.job_title = job_title
        self.responsibility = responsibility

    def __str__(self):
        return self.name + " who works as a" + self.job_title + " is responsible for " + self.responsibility + "\n"


class Speaker:
    def __init__(self, name, job_title, expertise):
        self.name = name
        self.job_title = job_title
        self.expertise = expertise

    def __str__(self):
        return self.name + " who works as a" + self.job_title + " is speaking about " + self.expertise + "\n"


def memberFactory (type, name, job_title, other):
    if type == "organizer":
        return Organizer(name, job_title, other)
    elif type == "speaker":
        return Speaker(name, job_title, other)
    return Member(name, job_title)

carry = Member('Carry', 'Software Engineer');
jessica = Organizer('Jessica', 'Engineering Manager', 'Organizing');
emily = Speaker('Emily', 'Front End Developer', 'React');

print(carry)
print(jessica)
print(emily)