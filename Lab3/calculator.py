operators = ("+", "-", "*", "/", "=")

while True:

    try:
        result = int(input("Введите ЦЕЛОЕ число \n"))
        break
    except:
        print("Не правильное число \n")


while True:

    inputValue = input(
        "Введите оператор  '+', '-', '*', '/' или '=', чтобы завершить \n")

    if inputValue not in operators:

        print("Не правильный оператор \n")

    else:
        if inputValue == "=":

            print("Конец \n")
            break

        else:

            inputNumber = input("Введите ЦЕЛОЕ число \n")

            try:
                inputNumber = int(inputNumber)
            except:
                print("Не корректное число \n")
                break

            if inputValue == '+':
                result += inputNumber

            elif inputValue == '-':
                result -= inputNumber

            elif inputValue == '*':
                result *= inputNumber

            elif inputValue == '/':
                result /= inputNumber

            else:
                print("Не правильный оператор \n")

print("Результат " + str(result))
