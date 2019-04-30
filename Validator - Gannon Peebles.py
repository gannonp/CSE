import csv


def sixteen_digits(num: str):
    if (len(num)) == 16:
        if len(num) == 16:
            return True
        else:
            print("NOT EVERY NUMBER IS 16 DIGITS!")
            return False


def divisible_by_2(num: int):
    if num % 2 == 0:
        return True
    return False


def valid_card_number(num: str):
    last_num = int(num[15])
    valid_card_number_list = list(num)
    valid_card_number_list.remove(last_num)
    if not sixteen_digits(num):
        return False
    reversed_num = num[::-1]
    reversed_num_list = list(reversed_num)
    for index in range(len(reversed_num_list)):
        if divisible_by_2(index):
            if reversed_num_list[index] * 2 > 9:
                (reversed_num_list[index] * 2) - 9
            else:
                reversed_num_list[index] *= 2
    sum_numbers = sum(reversed_num_list)
    if (sum_numbers % 10) == 0:
        print("Valid Card Number")
    else:
        print("Invalid Card Number")


with open("Book1.csv", 'r') as old_csv:
    with open("ValidatorCheck.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            if