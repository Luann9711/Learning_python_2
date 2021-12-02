# def test(*args):
#     result = 0
#     for number in args:
#         result += number
#     print(result)

# test(35352,6666,34)

a = set(['Kim', 'Lee', 'Park', 'Son', 'Min', 'Cho'])
b = set(['Kim', 'Lee', 'Park', 'Son', 'Cho'])

def solution():
    print(a.difference(b))


solution()