def factorial(N):
    fact = 1
    for i in range(1,N+1):  #loop from 1 to N
        fact = fact*i       #for each iteration multiply i with previous product of fact and i-1
    return fact

def oddProductPair(numbers):
    for i in range(len(numbers)):   #loop through the list of numbers
        for j in range(i,len(numbers)):
            if((numbers[i] != numbers[j]) and ((numbers[i] * numbers[j])%2)==1): #Check if the 2 numbers are distinct and there product is odd
                return True
    return False

def reverseDigits(num):
    revNumber = 0       #To store reverse of num
    isNeg = False
    if(num<0):          #Check if the number is negative
        isNeg = True    #Set isNeg to true
        num = num * (-1)    #Convert the num to positive
    while(num>0):                               #if num  = 123                  ,num = 12
        revNumber = revNumber*10 + (num%10)     #(num%10) = 3, revNumber = 3    ,(num%10) = 2, revNumber = 32
        num = int(num/10)                       #num = 12                       ,num = 1
    if(isNeg):              #if num is negative
        return(revNumber*(-1))
    return revNumber

def removeComma(line):
    comma = ','
    withoutComma = ""
    for char in line:
        if(char != comma):      #compare each character in line with ','
            withoutComma = withoutComma + char  #if character is not ',' add the character to the string withoutcomma
    return withoutComma

def validateBrackets(brackets):
    openBrac = ['(','{','[']  #Store open brackets in openBrac list
    closeBrac = [')','}',']']   #Store close brackets in closeBrac list
    stack = []
    for i in brackets:
        if i in openBrac:   #if a open bracket is found, add it to the stack
            stack.append(i)
        elif i in closeBrac:   #if a close bracket is found
            pos = closeBrac.index(i)   #find its position in closeBrac list
            if ((len(stack) > 0) and (openBrac[pos] == stack[len(stack)-1])):  #If stack contains any open bracket and if the open bracket matches the close bracket
                stack.pop()                                                     #then, remove the open bracket from the stack
            else:
                return "Unbalanced"
    if len(stack) == 0:     #If all the open brackets are popped then, string is balanced
        return "Balanced"
    else:
        return "Unbalanced"

def combineSortedList(list1, list2):
    index1 = 0
    index2 = 0
    sortedList = []     #used to store combined sorted lists
    while(index1<len(list1) and index2<len(list2)):   #loop through both the lists
        if(list1[index1]<list2[index2]):        #if value in list1 is less that list2, add list1 value to sortedList
            sortedList.append(list1[index1])
            index1+=1             #move to the next value of list1
        else:
            sortedList.append(list2[index2])     #add list2 value to sortedList
            index2+=1            #move to the next value of list1
    sortedList = sortedList + list1[index1:] + list2[index2:]  #Add the remaining values from both the list
    return sortedList


N = int(input("Enter a number to find its factorial: "))
print("The factorial of the number: ",factorial(N))

numbers = []
print("\nEnter 5 numbers")
for i in range(5):
    numbers.append(int(input()))
print("Sequence of numbers contain a distict pair of values whose product is odd: ", oddProductPair(numbers))

num = int(input("Enter a number to reverse: "))
print("Reverse Number: ",reverseDigits(num))

line = input("Enter a string to remove comma: ")
print(removeComma(line))

brackets = input("Enter the string of brackets: ")
print(validateBrackets(brackets))

print("Enter 2 sorted list of 4 numbers")
print("List1: ")
list1 = []
for i in range(4):
    list1.append(int(input()))

print("List2: ")
list2 = []
for i in range(4):
    list2.append(int(input()))

print("Sorted List: ", combineSortedList(list1,list2))