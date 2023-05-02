from threading import * #библиотека для создания потоков
from time import * #библиотека для работы со временем


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
                if spisok_sroka_godnosi[i] != 0:
                    print("-------------------------------------------------------------------")
                    print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]}; СКОЛЬКО ДНЕЙ ОСТАЛОСЬ: {spisok_sroka_godnosi[i]//24} ;СКОЛЬКО ОСТАЛОСЬ ЧАСОВ: {spisok_sroka_godnosi[i]%24} ; ЕГО НОМЕР: {i+1}")
                    print("-------------------------------------------------------------------")
                elif spisok_sroka_godnosi[i]<=0:
                    print("-------------------------------------------------------------------")
                    print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]}; !!!ВНИМАНИЕ ТОВАР ПРОСРОЧЕН!!!!; ЕГО НОМЕР: {i+1}")
                    print("-------------------------------------------------------------------")
        elif vvod == 2:
            print("Введите название товара:")
            nazvanie_tovara = input("СЮДА: ")
            print("Введите через сколько закончиться его срок годности в часах:")
            srok_godnosti = int(input("СЮДА:"))
            spisok_nazvania_tovara.append(nazvanie_tovara)
            spisok_sroka_godnosi.append(srok_godnosti)
        elif vvod == 3:
            for i in range(len(spisok_nazvania_tovara)):
                print("-------------------------------------------------------------------")
                print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]}; СКОЛЬКО ДНЕЙ ОСТАЛОСЬ: {spisok_sroka_godnosi[i]}; ЕГО НОМЕР: {i+1}")
                print("-------------------------------------------------------------------")
            print("Введите номер товара который нужно удалить")
            nomer_index = int(input("ВВОД: "))
            spisok_nazvania_tovara.pop(nomer_index-1)
            spisok_sroka_godnosi.pop(nomer_index-1)
            print(f"Вы успешно удалили елемент")
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