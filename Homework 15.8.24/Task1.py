a: tuple = (1, 2, 3, 5, 6 , 1)
b: tuple = (20, 31, 49, 50, 10, 5, 2)
#a.
first: tuple[int] = (99,)
#b.
tup: tuple[int] = 77, 88, 99


#c.
def tup_length(my_touple) -> int:
    return len(my_touple)


#d.
def combined_tuples(tuple1, tuple2) -> tuple:
    return tuple1 + tuple2


#e.
def combined_tuples(tuple1, tuple2) -> tuple:
    com = []
    for item in tuple1:
        if item in tuple2:
            com.append(item)
    return tuple(com)


print(combined_tuples(a, b))


#f.
def difference_tuples(tuple1, tuple2) -> tuple:
    different = []
    for item in tuple1:
        if item not in tuple2:
            different.append(item)
    for item in tuple2:
        if item not in tuple1 and item not in different:
            different.append(item)
    return tuple(different)


print(combined_tuples((1, 2, 3, 4), (3, 4, 5, 6)))
print(difference_tuples((1, 2, 3, 4), (3, 4, 5, 6)))


#g.
def tup_index(tuple1: tuple, index: int) -> str:
    if index < 0 or index > len(tuple1) - 1:
        return None
    return tuple1[index]


print(tup_index(a, 2))


#h.
def rev(tuple1: tuple) -> tuple:
    return tuple1[::-1]


print(rev(a))


#i.
def leftovers(tuple1: tuple, num: int) -> int:
    div: list = []
    for item in tuple1:
        if num % item == 0:
            div.append(item)
    return len([item for item in tuple1 if num % item == 0])


print(leftovers(b, 100))


#j.
def mult_tup(tuple1: tuple, num: int) -> tuple:
    return tuple1 * num


print(mult_tup(a, 3))


#k.
def tup_index(tuple1: tuple) -> tuple:
    return tuple((item, tuple1[item]) for item in range(len(tuple1)))


print(tup_index(("banana", "apple", "melon")))


#l.
def my_dict(tuple1: tuple) -> dict:
    dict1 = {}
    dict1["max"] = max(tuple1)
    dict1["min"] = min(tuple1)
    dict1["average"] = sum(tuple1) / len(tuple1)
    dict1["length"] = len(tuple1)
    dict1["reversed"] = sorted(tuple1)[::-1]
    dict1["sorted"] = sorted(tuple1)
#bonus
    dict2 = {}
    my_list = []
    for i in range(len(tuple1)- 1):
        if tuple1[i] not in my_list:
            my_list.append(tuple1[i])
    for i in range (len(my_list)):
        dict2[my_list[i]] = tuple1.count(my_list[i])
    dict1["dupe"] = dict2
    return dict1


print(my_dict((1, 3, 5, 9, 4, 8, 5, 1)))

#m.
def let_sen (tuple1:tuple) ->str:
    return ''.join(tuple1)

print (let_sen(("H","e","l","l","o")))

#n.
def sen_let (sent:str) -> tuple:
    return tuple(sent)

print(sen_let("Hello"))

#o.
def remo_num (tuple1:tuple, num=int) ->tuple:
    return tuple(item for item in tuple1 if item != num)

print(remo_num(b,10))

#p.
def no_duplicate (tuple1:tuple) -> tuple:
    my_list = []
    for i in range (len(tuple1)):
        if tuple1[i] not in my_list:
            my_list.append(tuple1[i])
    return tuple(my_list)
print(no_duplicate(a))

#q.
def index_num (tuple1:tuple,num:int) -> tuple:
    my_list =[]
    for i in range (len(tuple1)):
        if tuple1[i] == num:
            my_list.append(i)
    return tuple(my_list)

print(index_num(a,1))

#r.
names:list[str] =[]
grades: list[int] = []
while True:
    name:str = input("Please enter a name. To finish enter 'done': ")
    if name.isnumeric():
        print("Please enter a name, and not a number.")
        continue
    if name.lower() == "done":
        break
    names.append(name)

while True:
    try:
        grade: int = int(input("Please enter a grade, to quit enter '-999': "))
        if grade == -999:
            break
        if grade > -1 and grade < 101:
            grades.append(grade)
        else:
            print("Please enter a grade between 0 and 100")
            continue
    except:
        print("Please enter an integer!")
        continue
names_and_grades:tuple = tuple(zip(names, grades))
print(names_and_grades)










