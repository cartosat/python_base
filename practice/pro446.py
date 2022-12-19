# Function to rotate a mrix
def rotate(m):

    if not len(m):
        return

    top = 0
    bottom = len(m)-1

    left = 0
    right = len(m[0])-1

    while left < right and top < bottom:

        prev = m[top+1][left]

        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = m[top][i]
            m[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = m[i][right]
            m[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = m[bottom][i]
            m[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = m[i][left]
            m[i][left] = prev
            prev = curr

        left += 1

    matrix=[]
    for row in m:
        matrix.append(row)


    print(matrix)


rotate([[1, 2, 3, 4 ],[5, 6, 7, 8 ],[9, 10, 11, 12 ],[13, 14, 15, 16 ]])
# Print modified mrix

