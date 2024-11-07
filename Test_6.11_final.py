# Test-1


import statistics


# condition====
# 1 ---- Hova
num1: float = float(input("Enter a number: "))
num2: float = float(input("Enter a number: "))
if num1 > num2:
    for i in range(3):
        print(num2)
else:
    for i in range(3):
        print(num1)

# 2 ----- Hova
num3: int = int(input("Enter a number: "))
num4: int = int(input("Enter a number: "))
avg = (num3 + num4) / 2
print(f"The average is {avg}")

# 3 ---- Hova
a: int = int(input("Enter a number:"))
b: int = int(input("Enter a number:"))
c: int = int(input("Enter a number:"))
if a > b and a > c:
    print(a)
if b > a:
    print(b)
else:
    print(c)

# 4 ---- Hova
movie_long: int = int(input("Enter the movie long:"))
shaot = movie_long // 60
dakot = movie_long % 60
print(f"The movie long is {shaot} hour(s) and {dakot} minute(s)")

# 5
digit_4: int = int(input("Enter 4 digit number: "))
if digit_4 >= 1000:
    ahadot = digit_4 % 10
    print(f"The right digit is - {ahadot}")

# 6
digit_4: int = int(input("Enter 4 digit number: "))
if digit_4 >= 1000:
    ahadot = digit_4 % 100
    print(f"The second right digit is - {ahadot // 10}")

# 7
num: int = int(input("Enter 2 digit number:"))
s_num: int = num
sum_num = 0

while num > 0:
    ahadot = num % 10
    sum_num += ahadot
    num = num // 10
print(f" the sum of {s_num} = {sum_num}")

# 8
num_opsite: int = int(input("Enter 2 digit number"))
if 10 <= num_opsite <= 99:
    ahadot: int = num_opsite % 10
    asarot: int = num_opsite // 10
    num_new: int = ahadot * 10 + asarot

# 9
num_type: int = int(input("Enter a number: "))
if num_type % 2 == 0:
    print("Even")
else:
    print("Odd")

# 10
salary = float(input("Enter your salary: "))
tax = 0
if salary > 6000:
    tax = salary * 0.10
elif salary > 12000:
    tax = 100 * 0.10 + (salary - 6000) * 0.20
elif salary > 18000:
    tax = 100 * 0.10 + 100 * 0.20 + (salary - 12000) * 0.30
elif salary > 25000:
    tax = 100 * 0.10 + 100 * 0.20 + 300 * 0.30 + (salary - 18000) * 0.40
elif salary > 35000:
    tax = 100 * 0.10 + 100 * 0.20 + 300 * 0.30 + (salary - 25000) * 0.45
elif salary > 45000:
    tax = 100 * 0.10 + 100 * 0.20 + 300 * 0.30 + (salary - 35000) * 0.50
else:
    tax = 100 * 0.10 + 100 * 0.20 + 300 * 0.30 + 300 * 0.40 + (salary - 45000) * 0.51
after_tax = (salary - tax)
print(f"You need to pay: {after_tax}")

# 11
your_high: int = int(input("Enter your high: "))
your_age: int = int(input("how old are you: "))
if your_high >= 115 and 8 <= your_age <= 18 or your_high >= 100 and your_age >= 19:
    print("You are allowed to enter")
else:
    print("You can't enter")

# loop====
# 1 ---- Hova
num_top: int = int(input("Enter a number: "))
for i in range(1, num_top + 1):
    print(i, end='')

# 2 -----Hova
x: int = int(input("Enter number: "))
y: int = int(input("Enter number: "))
if x > y:
    for i in range(y, x + 1):
        print(i)
else:
    for i in range(x, y + 1):
        print(i)

# 3
n: int = int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i)

# 4
max_n: int = int(input("Enter number:"))
den_n: int = int(input("Enter a number: "))


# data =====
# 1 ----- hova
sum_numbers = 0
while True:
    user_num: int = int(input("Enter a number:"))
    if user_num == -99:
        break
    if user_num:  # i give range to the input that i can work with
        sum_numbers += user_num
if sum_numbers == 0:
    print(None)
print(f"The sum of the numbers is : {sum_numbers}")

# 2 ----- Hova

none_numb = None
biggest = 0
lowest = 9999
while True:
    pos_num: int = int(input("Enter positive number: "))
    if pos_num == -99:
        break
    if 1 <= pos_num <= 9999:
        pass
    if pos_num > biggest:
        biggest = pos_num
    if pos_num < lowest:
        lowest = pos_num

print(f"the biggest number is {biggest} and lowest is {lowest}")

# 3 ---- Hova

list_5: list[int] = [int(input("Enter a number: ")) for i in range(5)]
print(list_5)
big_num: int = max(list_5)
index_of_big = list_5.index(big_num)
print(f"The biggest number is {big_num} in index [{index_of_big + 1}]")

#4
v: int = int(input("Enter a number:"))
m: int = int(input("Enter a number:"))
with_hibur = 0

for _ in range(m):
    with_hibur += v
print(f"The multiplication is {with_hibur}")

#5
g: int = int(input("Enter a number:"))
j: int = int(input("Enter a number:"))
hezka = 0
for i in range(j):          #not work
    hezka += (g * (g* i))
print(hezka)
#6 --- Bonus

#7 --- Bonus

# 8
x: int = int(input('give me a number'))
for i in range(2, x + 1):
    if x < 2:
        pass
    else:
        if x == 1:
            pass
        else:
            divider: int = 2
            while divider < x:
                if x % divider == 0:
                    break
                divider += 1
            if divider < x:
                print(f"{x} is not prime")
            else:
                print(f"{x} is prime")

# complicated loops
# 1 ---- Hova
temps: list[float] = []

while len(temps) < 12:
    try:
        temp: float = float(input("Enter temperature:"))

        if not -5 <= temp <= 40:
            break
        if temp == 0:
            if len(temps) > 0 and temps[-1] == 0:
                continue
        temps.append(temp)
    except ValueError:
        print("you enter a str, while you need float")
    if temps:
        print(f"The yearly avg in TLV is {statistics.mean}")
        print(f"The max temp is {max(temps)} and The lowest temp is {min(temps)}")

#2
answer_list = ["1","2","3","4"]
counter = [0] * len(answer_list)
votes = 0
for i in range(4):
    try:
        answer = input("Do you want war? answer : 1-bead, 2-neged, 3-nimna , 4-veto: ")

        if answer in answer_list:
            index = answer_list.index(answer)
            votes += 1
            counter[index] +=1
        else:
            print("not valid letter")
    except ValueError:
        print("Your input is str , while is need to int")
for i in range(len(answer_list)):
    print(f"{answer_list[i]} : {counter[i]}")
if votes == 1 and answer== 1:
    print(f"the country that vote 'bead' first is number : {votes} ")