# def solution(A):
#     department_count = {}

#     for department in A:
#         if department in department_count:
#             department_count[department] += 1
#         else:
#             department_count[department] = 1

#     max_count = max(department_count.values())
#     return max_count











# # def solution(S):
# #     stack = []

# #     for token in S.split():
# #         if token.isdigit():
# #             stack.append(int(token))
# #         elif token == "DUP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.append(stack[-1])
# #         elif token == "POP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.pop()
# #         elif token == "+":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() + stack.pop()
# #             stack.append(result)
# #         elif token == "-":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() - stack.pop()
# #             stack.append(result)

# #     if len(stack) == 0:
# #         return -1  # Error: Stack is empty

# #     return stack[-1]





# # def solution(S):
# #     stack = []

# #     for token in S.split():
# #         if token.isdigit():
# #             stack.append(int(token))
# #         elif token == "DUP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.append(stack[-1])
# #         elif token == "POP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.pop()
# #         elif token == "+":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() + stack.pop()
# #             if result >= 2**20:
# #                 return -1  # Error: Overflow
# #             stack.append(result)
# #         elif token == "-":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() - stack.pop()
# #             if result < 0:
# #                 return -1  # Error: Underflow
# #             stack.append(result)

# #     if len(stack) == 0:
# #         return -1  # Error: Stack is empty

# #     return stack[-1]

# # def main():
    
# #     # Call the solution function
# #     result = solution(S)


# a = 7
# b = 9


# print(a+b)

# a+b 

# operands 

# operators


# a = 7
# b = 9

# a = a+b  # a=16
# b = a-b  #b =7
# a = a-b  #a =9

# # a,b = b,a

# print(a,b)


# a = 9
# b = 7

# String formatting 

# name = "Ryan"

# print("Hello, How are you?", name)







def add():
    print("Hello, How are you?")
    print("Hello, How are you?") 


# main function
add()


