class Convert:
    """
    Class to convert one number to another with different numeral system.

    """

    @staticmethod
    def convert(number, baseInit, baseFinal):
        """
        Convert a number with the baseInit numeral system to a number with the baseFinal numeral system.
        :param number: The initial number
        :param baseInit: A base of the initial number
        :param baseFinal: A base of the final number
        :return: The final number
        """
        baseInit = int(baseInit)
        baseFinal = int(baseFinal)
        if baseInit < 2 or baseInit > 36 or baseFinal < 2 or baseFinal > 36:
            raise ValueError(
                "Base of the number must be at least 2 and not more than 36!"
            )
        if baseInit == 10:
            return str(Convert._convert_dec_to_other(number, baseFinal))
        if baseFinal == 10:
            return str(Convert._convert_to_dec(number, baseInit))
        return str(
            Convert._convert_dec_to_other(
                Convert._convert_to_dec(number, baseInit), baseFinal
            )
        )

    @staticmethod
    def _convert_to_dec(number, base):
        return int(str(number), base=base)

    @staticmethod
    def _convert_dec_to_other(number, base):
        number = int(number)
        if base == 2:
            return bin(number)[2:].upper()
        if base == 8:
            return oct(number)[2:].upper()
        if base == 16:
            return hex(number)[2:].upper()
        res = ""
        while number:
            mod = number % base
            if base > 10:
                t = mod + 48
                if mod > 9:
                    t += 7
                res += chr(t)
            else:
                res += str(mod)
            number //= base
        return res[::-1].upper()


if __name__ == "__main__":
    assert Convert.convert(10, 10, 2) == "1010"
    assert Convert.convert(1000, 2, 10) == "8"
    assert Convert.convert(1000, 2, 8) == "10"
    assert Convert.convert(1010, 2, 16) == "A"
    assert Convert.convert("Python", 35, 36) == "MKVTTW"
    E = int(Convert.convert("E", 16, 10))
    DA = int(Convert.convert("DA", 16, 10))
    BEC = int(Convert.convert("BEC", 16, 10))
    assert E * DA == BEC
