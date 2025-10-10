# n = int(input("Введите количество чисел: "))
# arr = list(map(int, input("Введите числа: ").split(' ')))
#
# if n != len(arr):
#     print(Exception)
#
#
# def razn(list) -> int:
#     arrChet = [x for x in list if x % 8 == 0]
#     arrNechet = [x for x in list if x % 8 != 0]
#     avg_arrChet = sum(arrChet) // len(arrChet)
#     avg_arrNechet = sum(arrNechet) // len(arrNechet)
#     difAvgChet_AvgNechet = avg_arrChet - avg_arrNechet
#     return difAvgChet_AvgNechet
#
#
# def chast(list) -> int:
#     elementsNechet = [x for x in list if x % 2 != 0]
#     elementsChet = [x for x in list if x % 2 == 0]
#     avg_arrNechet = sum(elementsNechet) // len(elementsNechet)
#     avg_arrChet = sum(elementsChet) // len(elementsChet)
#     chast = avg_arrNechet * avg_arrChet
#     return chast
#
#
# print(razn(arr))
# print(chast(arr))


N = int(input("Введите количество чисел: "))
arrChet = []
arrNechet = []

elementsNechet = []
elementsChet = []

count_even = 0
count_odd = 0

for i in range(N):
    x = int(input("Введите "))
    #raznost
    if x % 8 == 0:
        arrChet.append(x)
    if x % 8 != 0:
        arrNechet.append(x)

    #chast
    if x % 2 != 0:
        elementsNechet.append(x)
    if x % 2 == 0:
        elementsChet.append(x)



avg_arrChet = sum(arrChet) // len(arrChet)
avg_arrNechet = sum(arrNechet) // len(arrNechet)

difAvgChet_AvgNechet = avg_arrChet - avg_arrNechet
chast = avg_arrNechet * avg_arrChet

print(difAvgChet_AvgNechet, chast)
