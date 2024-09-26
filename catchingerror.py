try:
# open file in read only mode
   with open("not_here.txt",'r') as f:
      f.write("hello world!")
except IOError as e:
   print("an error ocurred:",e)