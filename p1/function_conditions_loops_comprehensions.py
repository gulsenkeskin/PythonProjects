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

# zip:
# birbirinden farklı tipdeki listeleri bir arada değerlendirme imkanı sağlar
# bir liste içerisinde tuple şeklinde birbirinden farklı listeleri bir araya getirir

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

x=list(zip(students, departments, ages))
print(x) # [('John', 'mathematics', 23), ('Mark', 'statistics', 30), ('Venessa', 'physics', 26), ('Mariam', 'astronomy', 22)]


###############################################
# lambda, map, filter, reduce
###############################################

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

# map
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)


#compherensions
salaries = [1000, 2000, 3000, 4000, 5000]

[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary<3000]

print([salary * 2 if salary<3000 else salary*0 for salary in salaries])

print([new_salary(salary * 2) if salary<3000 else new_salary(salary*0.2) for salary in salaries])


students = ["gulsen", "ayse", "buse", "ayca"]
students_no=["gulsen", "buse"]

print([student.upper() if student in students_no else student.lower() for student in students ])

print([student.lower() if student not in students_no else student.upper() for student in students ])


dictionary= {"a":1, "b":2, "c":3, "d":4}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())


x= {k:v **2 for (k,v) in dictionary.items()}
print(x)
x= {k.upper() :v for (k,v) in dictionary.items()}
print(x)
x= {k.upper() :v**2 for (k,v) in dictionary.items()}
print(x)

# çift sayıların karesini alarak sözlüğe ekle
numbers = range(10)
new_dict = {}

for n in numbers:
    if n%2==0:
        new_dict[n]=n**2

print(new_dict)
x= {n: n**2 for n in numbers if n % 2==0}
print(x)

# bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns # kütüphane import etme
df = sns.load_dataset("car_crashes")
df.columns # ilgi df nin değişken isimlerini listeler
print(df.columns)

A=[]
for col in df.columns:
    print(col)
    A.append(col.upper())

df.columns=A
print(df.columns)

df = sns.load_dataset("car_crashes")
df.columns=[col.upper() for col in df.columns]
print(df.columns)

# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

# tek if varsa for önce kullanılır
# if else yapısı varsa for sonda kullanılır

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]
print(df.columns)




df = sns.load_dataset("car_crashes")
num_cols=[col for col in df.columns if df[col].dtype!="O"]
print(num_cols)





