import sys

type = sys.argv[1]

if type ==  "t2.medium":
   print ("It will charge you 4 dollars a day")

elif type == "t2.mlarge":
     print ("It will charge you 14 dollars a day")

elif type == "t2.extralarge":
     print ("It will charge you 140 dollars a day")

elif type == "t2.xxlarge":
     print ("It will charge you 300 dollars a day") 

elif type == "t2.micro":
     print ("It will charge you 2 dollars a day")  

else:
    print ("Please provide a valid instance type")


# Here we are passing more conditions by using if, elif, else.    
