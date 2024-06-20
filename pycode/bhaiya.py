# Operator 

# String 

# name = "Bhaiya"
# print(name[-2])

# slicing
# name = "Bhaiya"
# print(name[::-1])


# b = "Hello, World!"
# print(b[-5:-2])

# name = "1Bhaiya"
# print(name[::-3])

# replication
# name = "Bhaiya"
# print(name*3)


# Notes : # To create a dynamic variable in Python, you can use the globals() function. This allows you to create a new variable with a name based on the input. Here's how you can achieve it with your example:

# bhaiya = "Vipin"
# name = str(input("Enter the name : "))

# dynamic_variable = globals()[name]
# print("The name is : ", dynamic_variable)


# Array : 

# 1. list
# 2. tuple
# 3. set
# 4. dictionary

# List : -

# 1. list is a collection which is ordered and changeable. Allows duplicate members.
# 2. List is mutable

# l1 = [1,"Bhaiya",5.02,True]
# for i in range(len(l1)):
#     print(l1[i])

# names = ["Ohaiya","Vipin","Vikas","Uishal","Tivek"]

# names[0:3] = {"Bhaiya","Utkarsh","Deepesh"}

# print(names)
# for i in names:
#     vowels = "AEIOUaeiou"
#     if i[0] in vowels:
#         print(i)


# c = 1 
# def calculate(): 
#     print(c)
#     c = c + 2
# print(c) 
    
# calculate()



# 10 20 30 50

# t1 = (2019,'t')
# print(t1*3)


# def p1():
#     print("Hello, World!")
# print(p1())


# from nltk.tokenize import send_tokenize

# mytext = "Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"

# print(sent_tokenize(mytext))


from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()

lemmatiser = WordNetLemmatizer()

print("Stem %s: %s" % ("studying", stemmer.stem("studying")))

print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying")))

print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying", pos="v")))
