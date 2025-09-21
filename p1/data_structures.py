from collections.abc import dict_keys

# list
x=[1,2,3]
type(x)

# dictionary
x={"name":"John","age":25}
type(x)

# tuple
x=(1,2,3)
type(x)

# set
x={1,2,3}
type(x)

# list , tuple, set ve dictionary veri yapıları python collections (arrays) olarak da ifade edilir

# sayının karesini alma:
b= 2.1
a = 2
a ** 2

# tip değişimleri:
int(b)
float(a)

#strings
name="Gülsen"
name[0:2] # 0 dan başla 2 . karaktere kadar al
print(name[0:3])

# string içerisinde karakter sorgulamak
"G" in name

# verilen veriyapısa ait methodları görüntüemek
# dir(veri_yapisi)

dir(int)
dir(str)

# string methods

# len
name="gulsen"
len(name)
print(len(name))

"gulsen".upper()
"GULSEN".lower()
print("GULSEN".lower())

#replace karakter değiştirir
# 1. parametre hangi karakterin değiştirileceği
# 2. parametre ne ile değiştirileceği

name= "gulsen"
name = name.replace("u","ü")
print(name)

# split: böler
# parametre olarak bölme işleminin hangi karaktere göre yapılalcağını alır
# parametre verilmez ise boşluğa göre bölme işlemi yapar

name_and_surname= "Gülsen Keskin"
print(name_and_surname.split()) # ['Gülsen', 'Keskin']
print(name_and_surname.split("e")) # ['Güls', 'n K', 'skin']

# strip : kırpma methodu
# verilen argümana göre kırpma işlemi yapar
# argüman verilmez ise boğluğa göre kırpar c# daki trim() methodu gibi

name= " gulsen "
print(name.split()) #['gulsen']

name= "gulsen"
print(name.split("s")) # ['gul', 'en']

# capitalize: ilk harfi büyütür
"gulsen".capitalize()
print("gulsen".capitalize())


# list
names= ["ayse", "buse", "deniz", "mert"]
not_nam=["1",1,True,["a",3]]
print(not_nam[3][1])

names[0]="gülsen"
print(names[0])
print(names[1:3]) # 1. elemandan 3 elemana kadar alır 3 dahil değildir

# list methods:
len(not_nam)

# append: son indexe eleman ekler
names.append("bulut")
print(names)

# pop indexe göre eleman siler
names.pop(0)
print(names)

# insert  verilen indexe eleman ekler
names.insert(0,"guls")
print(names)

# dictionary:

dict={"name":"gulsen", "surname":"keskin"}
print(dict["name"])
print(dict.get("surname"))


# key sorgulama
"name" in dict
print("name" in dict) # true, false

dict["name"]="Gülsen" # değer deişimi
print(dict["name"])

# tüm key ya da value lara erişmek
dict.keys()
print(dict.keys())
print(dict.values())

# tüm çiftleri tuple halinde listeye çevirme
dict.items()
print(dict.items()) # dict_items([('name', 'Gülsen'), ('surname', 'keskin')])

# key value değerini güncellemek
dict.update({"name":"guls"})
print(dict)

# yeni key-value eklemek
dict.update({"date":"5"})
print(dict)
# uupdate methodu verilen key değeri var ise güncelleme işlemi yapar yok ise insert işlemi yapar


# tuple :
# değiştirilemez, birden fazla veri yapısını tutabilir, sıralıdır(index seçimi yapabilirirz)
t=("gulsen","keskin",1,2)
print(t[0])
print(t[1:0])

# küme set:
# değiştirilebilir, sırasız ve eşsizdir, kapsayıcıdır

set1= set([1,2,3])
set2= set([1,3,5])

# set 1 de olup 2 de olmayanları bulmak için difference methodu kullanılır
set1.difference(set2)
print(set1.difference(set2)) #{2}

# symmetric_difference(): iki kümede de de birbirine göre olmayanları getirir
set1.symmetric_difference(set2)
print(set1.symmetric_difference(set2)) #{2, 5}
# ya da - operatörü kullanılabilir
set1 - set2
print(set1 - set2)  # {2}

# intersection(): iki kümenin kesişimi
set1= set([1,2,3])
set2= set([1,3,5])
set1.intersection(set2)
print(set1.intersection(set2))  # {1, 3}
# ya da & operatörü kullanılabilir
set1 & set2
print(set1 & set2)  # {1, 3}

#union : iki kümenin birleşimi:
set1.union(set2)
print(set1.union(set2))

# isdisjoint(): iki kümenin kesişimi boş mu?
print(set1.isdisjoint(set2)) # False

#issubset: bir küme diğer kümenin alt kümesi mi?
set1= set([7,8,9])
set2= set([5,6,7,8,9,10])
print(set1.issubset(set2)) #true

#issuperset(): bir küme diğer kümeyi kapsıyor mu?
set1= set([7,8,9])
set2= set([5,6,7,8,9,10])
print(set2.issuperset(set1)) #true






