def Projection1(table : list, nomColonne : 'string') -> list:
    colIndex = -1

    for i in range(len(table[0])):
        if(table[0][i] == nomColonne):
            colIndex = i
            break
    if (colIndex == -1):
        return []

    newTable = []
    
    for i in range(len(table)):
        newTable.append(table[i][colIndex])

    return newTable

def Selection(table : list, nomColonne : 'string', fonctionComparaison : 'fonction lambda'):
    colIndex = -1

    for i in range(len(table[0])):
        if(table[0][i] == nomColonne):
            colIndex = i
            break
    if (colIndex == -1):
        return []

    newTable = []
    newTable.append(table[0])
    for i in range(1, len(table)):
        if(fonctionComparaison(table[i][colIndex])):
            newTable.append(table[i])

    return newTable

