'''
4-4) Suomi-englanti dictionary

Create a simple finnish-english dictionary

Example Output (anna sana == give a word): 
Anna sana>koira
dog
Anna sana>kieli
language
Anna sana>maa
country
'''

dicteng = {"LANGUAGE":"KIELI", "DOG": "KOIRA", "CAT":"KISSA", "CITY": "KAUPUNKI", "COUNTRY":"MAA", "AIRPLANE":"LENTOKONE"}
dictfin = {"KIELI":"LANGUAGE", "KOIRA": "DOG", "KISSA":"CAT", "KAUPUNKI": "CITY", "MAA":"COUNTRY", "LENTOKONE":"AIRPLANE"} 
dictionaries = {"dicteng" : dicteng, "dictfin" : dictfin}
while True:
   string=input("anna sana Give a word: ")
   stringiso = string.upper()
   for match in dicteng:
      if stringiso==match:
         print(dicteng[stringiso])
   for match in dictfin:
      if stringiso==match:
         print(dictfin[stringiso])
