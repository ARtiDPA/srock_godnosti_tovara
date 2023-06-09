from threading import * #библиотека для создания потоков
from time import * #библиотека для работы со временем


spisok_nazvania_tovara = []
spisok_sroka_godnosi = []


def timer(sekunda,minuta): # Блок с таймером
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

def glavnoe_menu(): #Меню управлением всей системой
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
            with open("Podgruzaema_pamat", "a") as file:
                file.write(nazvanie_tovara + "\n")
                file.write(str(srok_godnosti) + "\n")

        elif vvod == 3:
            for i in range(len(spisok_nazvania_tovara)):
                print("-------------------------------------------------------------------")
                print(f"НАЗВАНИЕ ТОВАРА: {spisok_nazvania_tovara[i]}; СКОЛЬКО ДНЕЙ ОСТАЛОСЬ: {spisok_sroka_godnosi[i]}; ЕГО НОМЕР: {i+1}")
                print("-------------------------------------------------------------------")
            print("Введите номер товара который нужно удалить")
            nomer_index = int(input("ВВОД: "))
            spisok_nazvania_tovara.pop(nomer_index-1)
            spisok_sroka_godnosi.pop(nomer_index-1)
            with open("Podgruzaema_pamat", "r") as file:
                lines = file.readlines()
            lines.pop(nomer_index-1)
            lines.pop(nomer_index)
            with open("Podgruzaema_pamat") as file:
                file.writelines(lines)
        else:
            print("Такого варианта нету, введите другой ответ")

def start(): #Перенесение из тектового документа в масив во время, и запуск потоков
    with open("Podgruzaema_pamat", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if i%2 != 0:
            print(f"НАЗВАНИЕ - {lines[i].strip()}")
            vrem_peremena = int(lines[i].strip())
            spisok_sroka_godnosi.append(vrem_peremena)
        elif i%2 == 0:
            print(f"ЧАСОВ - {lines[i].strip()}")
            vrem_peremena = lines[i].strip()
            spisok_nazvania_tovara.append(vrem_peremena)
    file.close()
    zapusk_programma()

def zapusk_programma(): # Запуск 2 потоков
    tr1 = Thread(target=timer, args=(0, 0))
    tr2 = Thread(target=glavnoe_menu)
    tr2.start() #запуск потока с таймером
    tr1.start() #запуск потока с меню управлением

if __name__=="__main__": #Проверка чтобы избежить ошибок
    start()
else:
    print("Это главный файл :( ")
