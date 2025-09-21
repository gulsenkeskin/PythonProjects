help(print)

def calculate(x):
    print(x*2)

calculate(2)

#docstring
def summer(x, y):
    """
    sum of two numbers
    Args:
        x:int, float
        y:int, float

    Returns:
        int, float

    """
    return x + y

#-------------------------

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(98, 12, 78))

varma, moisturea, chargea, outputa = calculate(98, 12, 78)

#--------------------------------
# elif : c# da li else if :)

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)

# for döngüsü:

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)


def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 20))


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

# enumerate() fonksiyonu Python'da bir döngü içinde hem elemanın kendisini hem de indeksini (sırasını) almak için kullanılır.
def p1(val):
    result = ""
    for i, char in enumerate(val):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    print(result)

p1("gulsen")

students=["gulsen","ayse","buse","ayca"]

def divide_students(students):
   groups=[[], []]
    for index,student in enumerate(students):
        if index%2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)

     print(groups)
     return groups

divide_students(students)








