

#2-4) read inputs

#Give integers as a command line arguments
#and calculate the end results based on the integers
#Use for loop for calculating the results

#Example output:

#python3 ex_args_calculator.py 12 15 22 41 2 5 15
#Total sum for args is  112
import sys
summa=0

for luku in sys.argv[1:]:
   summa += int(luku)
print(summa)