#taking percentage from usr

percentage = int(input("enter the percentage to get the grade"))


if percentage > 90:
     print("your grade is A")
elif percentage > 80:
     print("your garde is B")
elif percentage >= 60:
     print("your grade is C")
else:
     print ("your grade is D")