text= "Hello Python"
print(text.lower())   #coverts the string to lower case
print(text.upper())  #converts the string to upper case
print(text.strip())    #removes the leading and trailing space

a= text.split()         #splits the string into a list of words
print(a)

b= "~".join(a)
print(b)                  #joins elements of a list into a string

print(text.replace("Python","World")) #Replaces a substring with another substring

print(text.find("Python")) #Finds the first occurence of a string

print(text.startswith("Hello")) #Checks the start substring

print(text.endswith("Python"))#Checks the end substring

txt="Hello" #alphabet count of a substring
print(txt.count("l"))


