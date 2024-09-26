#Close the file when you are finish with it:

f = open("mahesh.txt", "r")
print(f.readline())
f.close()
print("closed successfully")