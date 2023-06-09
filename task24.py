# В фермерском хозяйстве в Карелии выращивают чернику. # Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. # Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. # Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# подзадачи: вводим количество кустов, вводим количество ягод на кусте, 
# находим максимальную сумму ягод левого, среднего и правого куста, выводим сумму ягод за 1 заход 

kyst = int(input("Введите количество кустов на вашей грядке: "))
chernichka = map(int, input(f"Введите для каждого из {kyst} кустов количество ягод через пробел: ").split())

allChernichka = list(chernichka)

maxChernichka = 0
for i in range(len(allChernichka) - 1):
    sum = int(allChernichka[i - 1] + allChernichka[i] + allChernichka[i + 1])
    if sum > maxChernichka: 
        maxChernichka = sum

print("Максимум собрать", maxChernichka, "шт")
print("Больше всего ягод у куста №", allChernichka.index(max(allChernichka)) + 1)