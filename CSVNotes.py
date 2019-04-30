import csv


def divisible_by_3(num: str):
    if not all_16_digits(num):
        return False
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS 16 DIGITS!")
        return False


# with open("Book1.csv") as old_csv:
#     reader = csv.rea\(old_csv)
#     for row in reader:
#         old_number = int(row[0]) + 1
#         old_number = row[0]
#         print(old_number)

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#
# print("DONE")

def reverse_it(string):
    print(string[::-1])


reverse_it("Hello World")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]
            if divisible_by_3(old_number) and divisible_by_2(old_number):
                writer.writerow(row)

print("DONE")
