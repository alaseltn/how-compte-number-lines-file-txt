from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
#print("reading file ")
f=open("new.txt","r")
#print (f.read())
num_lines = sum(1 for line in open('new.txt')) 

print(num_lines)
      #for line in f
         # print(line[1])
f.close()



