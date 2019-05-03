import csv


def sixteen_digits(number16: str):
    if (len(number16)) == 16:
        if len(number16) == 16:
            return True
        else:
            # print("NOT EVERY NUMBER IS 16 DIGITS!")
            return False


def divisible_by_2(number: int):
    if number % 2 == 0:
        return True
    return False


def valid_card_number(num: str):
    if not sixteen_digits(num):
        return False
    valid_card_number_list = list(num)
    valid_card_number_list.pop(15)
    for number in range(len(valid_card_number_list)):
        valid_card_number_list[number] = int(valid_card_number_list[number])
    reversed_num = num[::-1]
    reversed_num_list = []
    for i in range(len(reversed_num)):
        reversed_num_list.append(int(reversed_num[i]))
    for index in range(len(reversed_num_list)):
        if divisible_by_2(index):
            if int(reversed_num_list[index]) * 2 > 9:
                reversed_num_list[index] = int(reversed_num_list[index]) * 2 - 9
            else:
                reversed_num_list[index] *= 2
    sum_numbers = sum(reversed_num_list)
    if (sum_numbers % 10) == 0:
        # print('\033[1m' + "                                Valid Card Number")
        return True

    return False


with open("Book1.csv", 'r') as old_csv:
    with open("ValidatorCheck.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            num = row[0]
            if valid_card_number(num):
                writer.writerow(row)
        print("Done")

