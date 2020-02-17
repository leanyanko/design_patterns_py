def sayhi():
    print("hi, " + input("what's your name?"))

sayhi()

file = open("empl.txt", "r")
print(file.read())
file.close()