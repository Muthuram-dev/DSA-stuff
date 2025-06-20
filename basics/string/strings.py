normalString = "This is a good day's for everyone"
multiLineString = """ 
Hello there 
Welcome back to our company"""
print(normalString)
print(multiLineString)

print("Hello there \"MY IOHIAHEFOUABEUF\"") #Escape character useCase

print("TRAVERSING STRING THROUGH INDEXING")
# Traversing a string
print(normalString[1]) # will print the letter "h" in the index position 1
print(normalString[-1]) # last character will be printed
print(normalString[0:4]) # will print "This"
anotherString = normalString[:] # will copy all the characters in the normalString to a new var
print(anotherString)
