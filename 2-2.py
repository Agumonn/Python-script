#2-2) Byte, Kilobyte, Megabyte, Gigabyte converter

#Insert bytes and then your program shows many bytes in a kilobyte, megabyte and gigabyte.
#You must real mega, giga and tera definations (so for example 2^20 or 2^30)
#background information http://www.whatsabyte.com/

#Example output:

#Give your input in bytes: 1563200
#bytes  1563200 B
#Kilobytes  1526.5625 KB
#Megabytes  1.49078369140625 MB
#Gigabytes  0.001455843448638916 GB

luku = int(input("anna bittim‰‰r‰:  "))

Kluku=luku/1024
Mluku=Kluku/1024
Gluku=Mluku/1024



print("bytes    %d B", %luku)
print("Kilobytes    %d B", %Kluku)
print("Megabytes    %d B", %Mluku)
print("Gigabytes    %d B", %Gluku)