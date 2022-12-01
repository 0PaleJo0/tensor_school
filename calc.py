# очистка консоли перед прогой
import os
os.system('cls')
input = input(">>> Введите IP адрес и маску сети через /: ")

# input
mask = int(input.split("/")[1])
ip = (input.split("/")[0]).split(".")
stringNet = ""
stringBroad = ""
x = mask // 8

# проверка на входные данные 
for i in range (0, 4):
    if (int(ip[i]) > 255) or (int(ip[i]) < 0) or (mask > 32) or (mask < 0):
        print("Неверные входные данные")
        raise SystemExit

# вся магия
for i in range (0, 4):
    if i < x:
        stringNet = stringNet + ip[i] + "."
        stringBroad = stringBroad + ip[i] + "."
    elif i == x:
        n = mask % 8
        m = 8 - n
        subnets = 2 ** n
        adr = 2 ** m
        for j in range (0, subnets + 1):
            if (int(ip[i]) >= (j * adr)) and (int(ip[i]) <= ((j + 1) * adr - 1)):
                stringNet = stringNet + str(j * adr) + "."
                stringBroad = stringBroad + str((j + 1) * adr - 1) + "."
    else:
        stringNet = stringNet + "0."
        stringBroad = stringBroad + "255."

print("## Сетевой адрес: " + stringNet[:-1])
print("## Шиrоковещательный адрес: " + stringBroad[:-1])