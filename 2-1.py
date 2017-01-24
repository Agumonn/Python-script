
#2-1) calculate characters in a string

#Give a string and search how many 'a/A' or 'e/E' letters there are in the string
#How to count all letters in a string?

#Example output:

#Give a string>Jumping Errors and some test arrays Added
#a/A letters:  4
#e/E letters:  4





string = input("Give a string:    ")
print("a/A letters:  ",(string.count('A'))+(string.count('a')))
print("e/E letters:  ",(string.count('E'))+(string.count('e')))