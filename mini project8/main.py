import stackclass
print("Welcome to Postfix Calculator")
print("Enter exit to quit")
x =input("Enter Expression\n")
while x !="exit":
    #Splits the contents of the list into separate string elements
    y = x.split()
    #instantiates a stack/list from the class Stack
    original_list = stackclass.Stack()
    #Loops through the items in the original list
    for i in range(0,len(y)):
        original_list.push(y.pop())
    final_list = []
    while not original_list.isEmpty():
        z = original_list.pop()
        if z =="+":
            result =float(final_list.pop()) +float(final_list.pop())
            final_list.append(result)
        elif z =="-":
            result =float(final_list.pop(-2)) -float(final_list.pop())
            final_list.append(result)
        elif z =="*":
            result =float(final_list.pop()) *float(final_list.pop())
            final_list.append(result)
        elif z =="/":
            result =float(final_list.pop(-2)) /float(final_list.pop())
            final_list.append(result)
        else:
            final_list.append(z)
    print("Result: "+str(final_list[0]))
    x =input("Enter Expression\n")

