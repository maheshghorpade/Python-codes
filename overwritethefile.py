f = open("mahesh.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("mahesh.txt", "r")
print(f.read())