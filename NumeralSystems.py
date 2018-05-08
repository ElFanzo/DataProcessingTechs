def convertTenToOther(num, sys):
    if sys == 2:
        return bin(num)[2:]
    else:
        s = ''
        while num != 0:
            if sys > 10:
                t = num % sys + 48
                if num % sys > 9:
                    t += 7
                s += chr(t)
            else:
                s += str(num % sys)
            num //= sys
        return s[::-1]


def convertOtherToTen(base, number):
    return int(base, number)
