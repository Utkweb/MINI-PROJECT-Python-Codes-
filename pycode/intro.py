# txt="The best things in life are free!"

# # print("free" in txt)

# if "live" in txt:
#     print("Yes, 'free' is present ")
# else:
#     print("none is present")


# b="Apple"



# print(len(b))
# # slicing 
# # print(b[6:13])
# print(b[1:3])


# def solution(S):
#     stack = []

#     for token in S.split():
#         if token.isdigit():
#             stack.append(int(token))
#         elif token == "DUP":
#             if len(stack) < 1:
#                 return -1  # Error: Not enough elements in the stack
#             stack.append(stack[-1])
#         elif token == "POP":
#             if len(stack) < 1:
#                 return -1  # Error: Not enough elements in the stack
#             stack.pop()
#         elif token == "+":
#             if len(stack) < 2:
#                 return -1  # Error: Not enough elements in the stack
#             result = stack.pop() + stack.pop()
#             if result >= 2**20:
#                 return -1  # Error: Overflow
#             stack.append(result)
#         elif token == "-":
#             if len(stack) < 2:
#                 return -1  # Error: Not enough elements in the stack
#             result = stack.pop() - stack.pop()
#             if result < 0:
#                 return -1  # Error: Underflow
#             stack.append(result)

#     if len(stack) == 0:
#         return -1  # Error: Stack is empty

#     return stack[-1]


# def main():
#     # Read the input string
#     S = input("Enter the sequence of operations: ")

#     # Call the solution function
#     result = solution(S)

#     # Print the result
#     if result == -1:
#         print("Error occurred.")
#     else:
#         print("Topmost value from the stack:", result)


# # Call the main function
# main()





# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1

#     l = 0
#     r = N - 1
#     while l <= r:
#         m = (l + r) // 2

#         if A[m] > X:
#             r = m - 1
#         else:
#             l = m + 1

#     if r >= 0 and A[r] == X:
#         return r

#     return -1



# print("Welcome to the class of Python Programming Language Will how you feel?")


# a = 10
# b = 20
# print(a+b)

# a=3
# b=2
# print(a%b)



# a+b

# operands and operators


# 1. Addition +
# 2. Subtraction -
# 3. Multiplication *
# 4. Division /
# 5. Modulus %
# 6. Exponentiation **
# 7. Floor Division //

# base = 4
# power = 3

# print(base**power)




# a = 10
# b = 20

# print(a+b)





# print("Welcome to the class of Python Programming Language Will how you feel?")


# variables: It is used to store data values.


# a = 10
# print(a)

# defining multiple variables
# l1 = [1,2,3,4,5,6,7,8,9,10]
# print(l1[1:5])
# print(l1[1:5:2])
# l1.append(11)

# a = 10.650

# data types: It helps to store different types of data.

# 1. Integers (int): It is used to store whole numbers.
# 2. Float (float): It is used to store decimal numbers.
# 3. String (str): It is used to store characters.
# 4. boolean (bool): It is used to store True or False.

# a = 10 (int)
# b = 10.5 (float)
# c = "Python" (str)
# d = True (bool)

# Operators and operands:


# a+b