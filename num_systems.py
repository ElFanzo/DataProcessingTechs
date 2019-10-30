class Convert:
    @staticmethod
    def convert(number, baseInit, baseFinal):
        """Convert a number with the base_init numeral system to a number with
        the base_final numeral system.

        :param number: the initial number
        :param base_init: a base of the initial number
        :param base_final: a base of the final number
        :return: the final number
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
