import re
number_phone = input("Введите номер мобильного телефона\n")


def standardise_number(phone_number: str) -> str:
    """ Функция принимает строку с номером мобильного телефона
     и приводит к единому формату записи """

    # Проверяем не содержит ли строка быквы
    has_letters = any(char.isalpha() for char in number_phone)

    numbers = []

    if has_letters:
        print("Ошибка, в номере телефона не должно быть букв.")
    else:
        line = phone_number
        # Очищаем строку от символов, оставляем только цифры
        line_clean = re.sub(r"\D", "", line)
        numbers = list(line_clean)

        if len(numbers) == 11:
            if numbers[0] == "8":
                numbers[0] = "7"
            phone = "".join(numbers)
            formatter = (
                f"+{phone[0]}({phone[1:4]}){phone[4:7]}"
                f"-{phone[7:9]}-{phone[9:11]}"
            )
            print(formatter)
        elif len(numbers) > 11 or len(number_phone) < 11:
            print("Неверный формат мобильного номера телефлна РФ,"
                  "номер должен состоять из 11 цифр.")


standardise_number(number_phone)
