f = open("Readme.txt", "r")

if f.mode == "r":
    contents = f.read()
    print(contents)

f.close()