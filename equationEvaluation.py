eq = input("Enter equation: ")
eq = eq.replace(' ', '')

eqList = []
number = ''
operatorDict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
postfixVect = []
stackVect = []
output = []


for i in list(eq):
    
    
    if i in operatorDict.keys() or i == '(' or i == ')' :
        if len(number) > 0:
            eqList.append(number)
            number = ''

        eqList.append(i)
        
    else :
        number = number + str(i)


if len(number) > 0:
    eqList.append(number)


for i in eqList:
    if i == '(':
        stackVect.append(i)

    elif i == ')':
        

        for i in range(len(stackVect)-1, 0, -1):
            if stackVect[i] == '(':
                stackVect.pop()
                break
            else:
                postfixVect.append(stackVect.pop())
        
        

    elif i in operatorDict.keys():
        
        if len(stackVect) == 0 or stackVect[-1] == '(':
            stackVect.append(i)
        
        else:
            


            if operatorDict[stackVect[-1]] < operatorDict[i]:
                 stackVect.append(i)
            else:
                postfixVect.append(stackVect.pop())
                stackVect.append(i)
    
    else:
        postfixVect.append(i)

while len(stackVect) != 0:
    postfixVect.append(stackVect.pop())

if '(' in postfixVect:
    postfixVect.remove('(')
if ')' in postfixVect:
    postfixVect.remove(')')


for i in postfixVect:
    if i in operatorDict.keys():
        num2 = output.pop()
        num1 = output.pop()

        equation = str(num1) + str(i) + str(num2)
        output.append(eval(str(equation)))

    else:
        output.append(i)

print('Result: ' + str(output[0]))