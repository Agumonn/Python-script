#2-3) Grade calculator

#Ask two grades from the user:
#a) exam point   (0-24)
#b) demo points  (0-12)
#and calculate the total based on the following table:
 

#	>= 33 	=> 5
#	>= 29 	=> 4
#	>= 25 	=> 3
#	>= 21 	=> 2
#	>= 18 	=> 1
#	< 18   	=> 0

#Example output:

#How many exam points did you get (0-24)?21
#How many demo points did you get (0-12)?6
#With total points 27, the final grade was 3



luku = int(input("How many exam points did you get (0-24)?  "))
luku1 = int(input("How many demo points did you get (0-12)?  "))
summa=luku+luku1

if summa < 18:
   print("With total points", summa ," the final grade was 0")
if( summa >= 18 and summa < 21  ):
   print("With total points", summa ," the final grade was 1")
if( summa >= 21 and summa < 24):
   print("With total points", summa ," the final grade was 2")
if(summa >= 25 and summa < 28):
   print("With total points", summa ," the final grade was 3")
if(summa >= 29 and summa < 32):
   print("With total points", summa ," the final grade was 4")
if(summa >= 33):
   print("With total points", summa ," the final grade was 5")