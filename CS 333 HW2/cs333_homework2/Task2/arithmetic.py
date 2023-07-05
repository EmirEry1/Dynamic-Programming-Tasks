

M = []
L = []

def createOperationValues(operation):
    global M
    global L

    numbers = []
    operands = []

    for j,element in enumerate(operation):
        if j%2 == 0:
            numbers.append(int(element))
        else:
            operands.append(element)    
    M = [ [None for i in range(len(numbers))] for j in range(len(numbers))]
    L = [ [None for i in range(len(numbers))] for j in range(len(numbers))]
    
    return numbers,operands

def findMaxInterval(numbers,operands,first,last):
    if M[first][last] != None:
        return M[first][last]
    
    if first == last:
        M[first][last] = numbers[first]
        return numbers[first]
    else:
        max_result = None
        for j in range(first+1,last+1):
            right_max = findMaxInterval(numbers,operands,j,last) #M[j][last]
            left_max =  findMaxInterval(numbers,operands,first,j-1)  #M[0][j-1]
            right_min = findMinInterval(numbers,operands,j,last) #M[j][last]
            left_min =  findMinInterval(numbers,operands,first,j-1)  #M[0][j-1]
            if operands[j-1] == '+':
                sub_result_1 = left_max+right_max
                sub_result_2 = left_min+right_min 
                sub_result_3 = left_min+right_max
                sub_result_4 = left_max+right_min 
            elif operands[j-1] == '-':
                sub_result_1 = left_max-right_max
                sub_result_2 = left_min-right_min 
                sub_result_3 = left_min-right_max
                sub_result_4 = left_max-right_min 
            elif operands[j-1] == '*':
                sub_result_1 = left_max*right_max
                sub_result_2 = left_min*right_min 
                sub_result_3 = left_min*right_max
                sub_result_4 = left_max*right_min  
            sub_result = max(sub_result_1,sub_result_2,sub_result_3,sub_result_4)
            if max_result == None or sub_result > max_result:
                max_result = sub_result
        M[first][last] = max_result
        return max_result


def findMinInterval(numbers,operands,first,last):
    if L[first][last] != None:
        return L[first][last]
    
    if first == last:
        L[first][last] = numbers[first]
        return numbers[first]
    else:
        min_result = None
        for j in range(first+1,last+1):
            right_max = findMaxInterval(numbers,operands,j,last) #M[j][last]
            left_max =  findMaxInterval(numbers,operands,first,j-1)  #M[0][j-1]
            right_min = findMinInterval(numbers,operands,j,last)
            left_min =  findMinInterval(numbers,operands,first,j-1)  #M[0][j-1]
            if operands[j-1] == '+':
                sub_result_1 = left_max+right_max
                sub_result_2 = left_min+right_min 
                sub_result_3 = left_min+right_max
                sub_result_4 = left_max+right_min  
            elif operands[j-1] == '-':
                sub_result_1 = left_max-right_max
                sub_result_2 = left_min-right_min 
                sub_result_3 = left_min-right_max
                sub_result_4 = left_max-right_min  
            elif operands[j-1] == '*':
                sub_result_1 = left_max*right_max
                sub_result_2 = left_min*right_min 
                sub_result_3 = left_min*right_max
                sub_result_4 = left_max*right_min   
            sub_result = min(sub_result_1,sub_result_2, sub_result_3, sub_result_4)
            if min_result == None or sub_result < min_result:
                min_result = sub_result
        L[first][last] = min_result
        return min_result

operation = input()
numbers,operands = createOperationValues(operation)
print(findMaxInterval(numbers,operands,0,len(numbers)-1))
