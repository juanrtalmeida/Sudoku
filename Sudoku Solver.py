import random

deucerto = False
matriz = []
vector = []


def build(n):
    for i in range(n):
        for j in range(n):
            k = random.choice(vector)
            vector.remove(k)
            matriz[i].append(k)

def verify():

    sum = {"linhas": {}, "colunas": {},"diagonal principal":{0:0},"diagonal secundaria":{0:0}}
    for i in range(m):

        sum["diagonal principal"][0] += matriz[i][i]
        sum["diagonal secundaria"][0]+= matriz[i][(m-1-i)]

        for j in range(m):
            if i not in sum["linhas"].keys():
                sum["linhas"][i] = matriz[i][j]
            else:
                sum["linhas"][i] += matriz[i][j]

            if i not in sum["colunas"].keys():
                sum["colunas"][i] = matriz[j][i]
            else:
                sum["colunas"][i] += matriz[j][i]


    sumstotal = set()
    for x in sum["linhas"]:
        sumstotal.add(sum["linhas"][x])
    for x in sum["colunas"]:
        sumstotal.add(sum["colunas"][x])
    for x in sum["diagonal principal"]:
        sumstotal.add(sum["diagonal principal"][x])
    for x in sum["diagonal secundaria"]:
        sumstotal.add(sum["diagonal secundaria"][x])

    if len(sumstotal) == 1:
        result = True
    else:
        result = False

    return result


m = input('Whats the size of the matrix N x N ?')
while not m.isdigit():
    n = input('Whats the size of the matrix N x N ?')
m = int(m)

while deucerto == False:

    matriz = []
    for i in range(1, (m * m) + 1):
        vector.append(i)

    for i in range(m):
        matriz.append([])

    build(m)
    if verify():
        deucerto = True

print("The first Optimized Matrix we found for the problem is: ")
for i in range(m):
    print(matriz[i])
