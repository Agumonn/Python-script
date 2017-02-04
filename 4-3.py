#4-3) list calculation with type detection

#calculate sum and average of elements in the list
#ignore all values in the list that are not numbers

#initializing the list with the following values

#list = [1,2,3,4,5,6,7,8,9,20,30, "aa", "bee", 11, "test", 51, 63]

#Example Output: 
#Sum 220/14 and average 15.71

list = [1,2,3,4,5,6,7,8,9,20,30, "aa", "bee", 11, "test", 51, 63]


def summalaskuri(a):
   summa=0
   luku=0
   lippu=0
   for luku in a:
      if type(luku) == int or type(luku) == float:
         summa += luku
         lippu += 1
   print("Sum %d/%d and average %.2f" %(summa,lippu,(summa/lippu)))

summalaskuri(list)