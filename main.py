# Task 1
print('Task 1')


def get_string_quantity_of_ingredients():
    with open('recipes.txt', encoding='utf-8') as file:
        idx_count_lines = []
        for idx, l in enumerate(file):
            if l.strip().isdigit():
                idx_count_lines.append(idx)
    return idx_count_lines  # [1, 7, 14, 20]


def get_string_value_quantity_of_ingredients():
    with open('recipes.txt', encoding='utf-8') as file:
        ing_count_lines = []
        for line in file:
            if line.strip().isdigit():
                ing_count_lines.append(line.strip())
    return ing_count_lines


def get_string_with_title():
    with open('recipes.txt', encoding='utf-8') as file:
        idx_count_lines = []
        for idx, l in enumerate(file):
            if l.strip().isdigit():
                idx_count_lines.append(idx - 1)
    return idx_count_lines


def get_string_value_of_title():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        idx_count_lines = get_string_with_title()
        for idx, l in enumerate(file):
            if idx in idx_count_lines:
                cook_book[l.strip()] = []
    return cook_book


def get_list_of_ingredients(dishes, person_count, cook_book):
    count = person_count
    ingred = {}
    listics = dishes
    for dish in listics:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in ingred:
                ingred.update({ingr['ingredient_name']: {'measure': ingr['measure'], 'quantity': count * int(ingr['quantity']) + int(ingred[ingr['ingredient_name']]['quantity'])}})
            else:
                ingred[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': count * int(ingr['quantity'])}
    return ingred


with open('recipes.txt', encoding='utf-8') as f:
    keys = ['ingredient_name', 'quantity', 'measure']
    cook_book = get_string_value_of_title()
    idx_count_lines = get_string_with_title()
    idx1_count_lines = get_string_quantity_of_ingredients()
    idxs_count_lines = get_string_value_quantity_of_ingredients()
    lines = f.readlines()
    for i in range(0, len(idx_count_lines)):
        for j in range(idx1_count_lines[i] + 1, idx1_count_lines[i] + int(idxs_count_lines[i]) + 1):
            values = lines[j].strip().split(" | ")
            d = dict(zip(keys, values))
            cook_book[lines[idx_count_lines[i]].strip()] += [d]
    print('Cook_book:')
    print(cook_book)

    # Task 2
    print('Task 2')
    list_of_ingredients = get_list_of_ingredients(['Фахитос', 'Омлет'], 2, cook_book)
    print('List of ingredients:')
    print(list_of_ingredients)


# Task 3
print('Task 3')

file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
result = 'result.txt'
f1 = open(file1, encoding='utf-8')
f2 = open(file2, encoding='utf-8')
f3 = open(file3, encoding='utf-8')
fr = open(result, 'w', encoding='utf-8')
fr.write('')
fr.close()
fr = open(result, 'a', encoding='utf-8')
d1 = f1.readlines()
d2 = f2.readlines()
d3 = f3.readlines()
d = [d1, d2, d3]
length = [len(d1), len(d2), len(d3)]
length.sort()
for i in range(0, 3):
    for j in d:
        if len(j) == length[i]:
            if j == d1:
                fr.write('file1.txt\n')
            elif j == d2:
                fr.write('file2.txt\n')
            else:
                fr.write('file3.txt\n')
            fr.write(str(len(j)))
            fr.write('\n')
            for t in range(0, len(j)):
                fr.write(j[t].strip())
                fr.write('\n')
f1.close()
f1.close()
f1.close()
fr.close()

f = open('result.txt', 'r', encoding='utf-8')
print(f.read())
