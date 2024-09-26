import json

#some json
x = '{"name":"john", "age":30, "city":"new york"}'

#parse x:
y = json.loads(x)

#the result is a python dictionary:
print(y["age"])