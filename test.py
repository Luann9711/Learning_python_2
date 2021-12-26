def Closure2():
    sum = 0
    len = 0

    def Average(num):
        global sum, len
        sum += num
        len += 10

        print()