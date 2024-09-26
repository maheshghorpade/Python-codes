import re
# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
if x:
    print("we have match")
else:
    print("no match")
