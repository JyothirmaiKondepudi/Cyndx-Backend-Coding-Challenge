def findPeak(matrix, low, high):
    rows,cols = len(matrix), len(matrix[0])
    if rows==1 and cols==1:
         return (0,0)
    mid = (low+high)//2
    maxElement = matrix[0][mid]
    maxRow = 0
    for i in range(rows):
        if matrix[i][mid]>maxElement:
            maxElement,maxRow = matrix[i][mid],i
            
    
    # check if this maxElement could be the peak
    # print(maxElement,mid,index)

    up = float('-inf') if maxRow-1<0 else matrix[maxRow-1][mid]
    down = float('-inf') if maxRow+1>=rows else matrix[maxRow+1][mid]
    left = float('-inf') if mid-1<0 else matrix[maxRow][mid-1]
    right = float('-inf') if mid+1>=cols else matrix[maxRow][mid+1]

    print(up,down,right,left,maxElement)
    if maxElement > up and maxElement>down:
            if maxElement > left :
                if maxElement> right:
                    return (maxRow,mid)
                else:
                    return findPeak(matrix,mid+1,high)
            else:
                return findPeak(matrix,low,mid-1)
                
        


matrix = [[10, 8, 10, 10],
[14, 13, 12, 11],
[15, 9, 11, 21],
[16, 17, 19, 20]
]
res = findPeak(matrix,0,len(matrix[0])-1)
print(res)