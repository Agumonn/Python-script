#4-2) Sum of arguments
#Calculate the sum of the list of command arguments


#Example Output: 
#python3 ex_calc_func_list_args.py 1 2 3 4 5 6 7 8 9 10 20 40 50
#Arguments: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '40', '50']  and sum = 165



import sys
summa=0

for luku in sys.argv[1:]:
   summa += int(luku)
print("Arguments: " , sys.argv[1:] , "and sum = " , summa)
