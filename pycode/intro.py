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


