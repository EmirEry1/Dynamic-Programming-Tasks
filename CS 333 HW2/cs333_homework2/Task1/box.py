
M = []
p = []
def calculateM(index):
    global M 
    if M[index] == None:
        max = 0
        for value in p[index]:
            if calculateM(value) > max:
                max = calculateM(value)
        M[index] = max + 1 
        return max + 1 
    return M[index] 
def maxDepth(boxes,n):
    boxes = sorted(boxes, key=lambda x : x[0])
    global p
    p = [ [] for j in range(n) ]
    for i in range(n):
        for j in range(i):
            if boxes[i][0]>boxes[j][0] and boxes[i][1]>boxes[j][1] and boxes[i][2]>boxes[j][2]:
                p[i].append(j) 
    print(p)
    global M
    M = [ None for j in range(n)]
    max = 0
    for i in range(n):
        if calculateM(i) > max:
            max = calculateM(i)
    return max
    
def take_input():
    n = int(input())
    boxes = []
    for i in range(n):
        boxes.append(input().split(' '))
    
    for i in range(n):
        for j in range(3):
            boxes[i][j] = float(boxes[i][j])
    
    print(boxes)

    for i in range(len(boxes)):
        length = max(boxes[i][0],boxes[i][1],boxes[i][2])
        height = min(boxes[i][0],boxes[i][1],boxes[i][2])
        weight = 0
        for j in range(3):
            if boxes[i][j]  != length and boxes[i][j] != height:
                weight = boxes[i][j]

        boxes[i][0] = length
        boxes[i][1] = weight
        boxes[i][2] = height

        print("*******************")
    print(boxes)
    print(maxDepth(boxes,n))
take_input()


"""
M = []
p = []
OPT = []
def calculateM(index):
    global M 
    if M[index] == None:
        M[index] == max(M[index-1], M[p[index]]+1) 
    return M[index] 
def maxDepth(boxes,n):
    boxes = sorted(boxes, key=lambda x : x[0])
    global p
    p = [ None for j in range(n) ]
    global M
    M = [ None for j in range(n)]
    
    
    return max
    
def take_input():
    n = int(input())
    boxes = []
    for i in range(n):
        boxes.append(input().split(' '))
    
    for i in range(n):
        for j in range(3):
            boxes[i][j] = float(boxes[i][j])
    
    print(maxDepth(boxes,n))
take_input()"""