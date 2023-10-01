#1 задание
def str1(lst):
    return ' '.join(map(str, lst))

size = int(input("Введите количество строк треугольника Паскаля: "))
pascalTriangle = [] # массив со строками для треугольника паскаля

for i in range(size):
    row = [1] * (i + 1)# количество чисел в каждой строке треугольника
    for j in range(1, i):
        row[j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j] # содержание строк треугольника
    pascalTriangle.append(row)

width = len((str1(pascalTriangle[-1])))

for line in pascalTriangle:
    print(str1(line).center(width))# выравнивание треугольника паскаля по центру

#2 задание
def sierpinskiTriangle(n):
    if n == 0:
        return ["*"]
    else:
        previous = sierpinskiTriangle(n - 1) # треугольник серпинсокго
        space = " " * (2 ** (n - 1)) # расстояние от звездочек до краев консоли
        result = [] # этажи треугольника
        for line in previous:
            result.append(space + line + space)
        for line in previous:
            result.append(line + " " + line)
        return result

depthOfTriangle = int(input("Введите глубину треугольника Серпинского: \n"))
triangle = sierpinskiTriangle(depthOfTriangle)
for line in triangle:
    print(line)


