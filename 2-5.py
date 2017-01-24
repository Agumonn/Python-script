
#2-5) multiplication table

#Calculate the multiplication table
#based on the upper limit given by the user

#Example output:

#upper limit>4
#1 * 1 = 1
#1 * 2 = 2
#1 * 3 = 3
#1 * 4 = 4
#2 * 1 = 2
#2 * 2 = 4
#2 * 3 = 6

luku = int(input("anna luku väliltä 1-10>"))
for a in range(1,11):
   for b in range(1,luku+1):
      print (a, "*", b , "=", (a*b))