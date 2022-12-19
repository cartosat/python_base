
def rotate(m):
    layers = int(len(m) / 2)
    length = int(len(m) - 1)

    for layer in range(layers):
        for i in range(layer, length - layer):
            temp = m[layer][i]

            m[layer][i] = m[length - i][layer]

            m[length - i][layer] = m[length - layer][length - i]

            m[length - layer][length - i] = m[i][length - layer]

            m[i][length - layer] = temp
    matrix=[]
    for row in m:
        matrix.append(row)

    print(matrix)



rotate([[1,2],[3,4]])

rotate([[1,2,3],[4,5,6],[7,8,9]])