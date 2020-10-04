# *args(튜플) and **kwargs(딕셔너리)

# arg = (1,2,3)
def sum_numbers(*args):
    answer = 0
    for num in args:
        answer += num
    return answer

print(sum_numbers(1,2,3))

# TODO List -> sum_numbers


# Kwargs
def concat_string(**kwargs):
    answer=''
    for string in kwargs.values():
        answer += string
    return answer
print(concat_string(a="My ", b="name ", c="is ", d="Niz"))