def Projection1(table : list, nomColonne : 'string') -> list:
    colIndex = -1

    for i in range(len(table[0])):
        if(table[0][i] == nomColonne):
            colIndex = i
            break
    if (colIndex == -1):
        return [table[0]]

    newTable = []
    
    for i in range(len(table)):
        newTable.append(table[i][colIndex])

    return newTable

#Comment faire une fonction lambda
#https://www.w3schools.com/python/python_lambda.asp
def Selection(table : list, nomColonne : 'string', comp : 'fonction lambda'):
    colIndex = -1

    for i in range(len(table[0])):
        if(table[0][i] == nomColonne):
            colIndex = i
            break
    if (colIndex == -1):
        return [table[0]]

    newTable = []
    newTable.append(table[0])
    for i in range(1, len(table)):
        if(comp(table[i][colIndex])):
            newTable.append(table[i])

    return newTable

