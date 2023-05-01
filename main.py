from threading import *
from time import *


spisok_nazvania_tovara = []
spisok_sroka_godnosi = []


def timer(sekunda,minuta,chas):
    while True:
        sleep(1)
        sekunda+=1
        if sekunda == 60:
            minuta += 1
            sekunda = 0
        elif minuta == 60:
            minuta = 0
            chas += 1
        elif chas == 24:
            for i in range(len(spisok_sroka_godnosi)):
                spisok_sroka_godnosi[i] -= 1

def glavnoe_menu():
    while True:
        print("введите 1 чтобы увидить список товара с его сроком годности")
        print("введите 2 чтобы добавить новый объект")
        print("введите 3 чтобы удалить объект")
        vvod = int(input("ВВОД: "))
        if vvod == 1:
            for i in range(len(spisok_nazvania_tovara)):
                print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]} СКОЛЬКО ДНЕЙ ОСТАЛОСЬ: {spisok_sroka_godnosi[i]} ЕГО НОМЕР: {i}")
        elif vvod == 2:
            print("Введите название товара:")
            nazvanie_tovara = input("СЮДА: ")
            print("Введите через сколько закончиться его срок годности в днях:")
            srok_godnosti = int(input("СЮДА:"))
            spisok_nazvania_tovara.append(nazvanie_tovara)
            spisok_sroka_godnosi.append(srok_godnosti)
        elif vvod == 3:
            for i in range(len(spisok_nazvania_tovara)):
                print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]} СКОЛЬКО ДНЕЙ ОСТАЛОСЬ: {spisok_sroka_godnosi[i]} ЕГО НОМЕР: {i}")
            print("Введите номер товара который нужно удалить")
            nomer_index = int(input("ВВОД: "))
            spisok_nazvania_tovara.pop(nomer_index)
            spisok_sroka_godnosi.pop(nomer_index)
            print("Вы успешно удалили")
        else:
            print("Такого варианта нету, введите другой ответ")
def start():
    tr1 = Thread(target=timer, args=(0, 0, 0))
    tr2 = Thread(target=glavnoe_menu)
    tr2.start()
    tr1.start()

if __name__=="__main__":
    start()
else:
    print("Это главный файл :( ")