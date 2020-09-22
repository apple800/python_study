def sort_age(infos):
    return infos[1]

def sort_score(infos):
    return infos[2]

infos = [('Tom', '19', '80'),('John', '20', '90'),('Jony', '17', '91'),('Jony', '17', '93'),('Json', '21', '85')]

print('Unsorted Datas')
print(infos)


print('Sort based on name')
print(sorted(infos))


print('Sort based on age')
print(sorted(infos, key=sort_age))


print('Sort based on score')
print(sorted(infos, key=sort_score))