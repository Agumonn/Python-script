#4-1) Count all letters in a string
#
#How to count all letters with ignore-case in a string?
#
#Example Output: 
#Give a string>Add some words to calculate LETTERS in this string
#****************Letter ignorecase occurance*****************
#  : 8
#a : 3
#c : 2
#d : 3
#e : 4
import re


string=input("give a string:  ")
str=string.upper()

print("letter count: ",len(str))
symbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #kirjaimet jota etsitaan eli aakkoset
for key in (symbol):
   if (str.count(key) >= 1):
      print(key, str.count(key))