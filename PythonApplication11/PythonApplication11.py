#1
def print_trees(n):
    tree = ["   /\\   ",
            "  /  \\  ",
            " /    \\ ",
            "/------\\"]

    for _ in range(n):
        for line in tree:
            print(line, end="  ")
        print() 

n = int(input("Sisestage jõulupuude arv (1 kuni 9): "))
print_trees(n)


#2
def multiply_odd_numbers(r):
    result = 1
    for num in range(r + 1):
        if num % 2 != 0:
            result *= num
    return result

r = int(input("Sisestage R-number: "))
print("Paaritute arvude korrutis kuni", r, ":", multiply_odd_numbers(r))

#3
import random

def count_positive_numbers(N):
    numbers = [random.randint(-100, 100) for _ in range(N)]
    positive_count = sum(1 for num in numbers if num > 0)
    return positive_count

N = int(input("Sisestage numbrite arv N: "))
print("Positiivsete arvude arv:", count_positive_numbers(N))

#4
def count_even_odd_digits(num):
    even_count = 0
    odd_count = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

num = int(input("Sisestage naturaalarv: "))
even_count, odd_count = count_even_odd_digits(num)
print("Paarisarvud:", even_count)
print("Pole paarisarumbreid:", odd_count)

#5
def sum_of_series(A, B):
    return sum(range(A, B + 1))

#5
def sum_of_series(A, B):
    return sum(range(A, B + 1))

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Введите целое число.")

A = get_integer_input("Sisestage number A: ")
B = get_integer_input("Sisestage number B: ")
print("Numbrite summa alates", A, "kuni", B, ":", sum_of_series(A, B))


нужно сделать на каждом проверку ввода, если цифры надо, чтобы писал что только цифры, если например с 1-11 то если вводится другое число просило 1-11, должна юыть прверка ввода. Также елку нормальную сделать 