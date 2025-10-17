N = int(input("Введите количество чисел: "))
arrChet = []
arrNechet = []

elementsNechet = []
elementsChet = []

count = 2

for i in range(N):
    x = int(input("Введите "))

    if count % 2 != 0:
        elementsNechet.append(x)
    if count % 2 == 0:
        elementsChet.append(x)

    #raznost
    if x % 8 == 0:
        arrChet.append(x)
    if x % 8 != 0:
        arrNechet.append(x)

    count += 1

avg_arrChet = sum(arrChet) / len(arrChet)
avg_arrNechet = sum(arrNechet) / len(arrNechet)

difAvgChet_AvgNechet = avg_arrChet - avg_arrNechet


chast = (sum(elementsNechet) / len(elementsNechet)) * (sum(elementsChet) / len(elementsChet))

print(difAvgChet_AvgNechet, chast)
print(arrChet, arrNechet)
