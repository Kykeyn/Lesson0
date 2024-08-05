first_stone = int(input('Введите число от 3 до 20: '))


pair = list(range(1, first_stone))
pairs = []


for i in pair:
    for j in pair:
        if i >= j:
            continue
        else:
            multiple = first_stone % (i + j)
            if multiple == 0:
                pairs.append([i,j])


result = 'Нужные числа это: '

print(result,*pairs)