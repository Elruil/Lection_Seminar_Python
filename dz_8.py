import os, re

def printData(data):  
    phoneBook = []
    splitLine = "=" * 102
    print(splitLine) 
    print(" №  Фамилия        Имя          Номер телефона         Примечания")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone, notes = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "Фамилия": lastName,
                "Имя": name,
                "телефон": phone_format(phone),
                "примечания": notes
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone, notes = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15} {notes:<60}")

    print(splitLine)


def phone_format(n): 
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]




def showContacts(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- Нажмите любую клавишу ---")


def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию: ") + ","
        res += input("Введите имя: ") + ","
        res += input("Введите номер телефона: ") + ","
        res += input("Введите примечание: ")

        file.write(res + "\n")

    input("\nНомер успешно сохранен!\n--- Нажмите любую клавишу ---")


def findContact(fileName):  
    os.system("cls")
    target = input("Введите значение для поиска по справочнику: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"По данному параметру '{target}' ничего не найдено.")

    input("--- Нажмите любую клавишу ---")


def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер из списка контактов для изменения или 0 для возврата в меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый телефон: ")
            newNotes = input("Введите новое примечание: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "," + newNotes + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- Нажмите любую клавишу ---")
        else:
            return


def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер из списка контактов для удаления или 0 для возврата в меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- Нажмите любую клавишу ---")


def drawInterface():  
    print("#####   Телефонная книга   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 26)


def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите номер от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            return


path = "phonebook.txt"

main(path)