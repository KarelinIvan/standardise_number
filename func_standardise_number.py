import re
number_phone = input()


def standardise_number(phone_number: str) -> str:
    """ Функция принимает строку с номером мобильного телефона
     и приводит к единому формату записи """

    line = phone_number
    line_clean = re.sub(r"\D", "", line)
    numbers = list(line_clean)

    numbers[0] = "7"
    print(*numbers)

    phone = "".join(numbers)

    formatter = f"+{phone[0]}({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:11]}"
    print(formatter)


standardise_number(number_phone)
