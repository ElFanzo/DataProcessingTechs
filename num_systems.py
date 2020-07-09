"""Module for converting numbers to various numeral systems."""

from typing import Tuple, Union


def convert(number: Union[int, str], base_init: int, base_final: int) -> str:
    """Convert a number to another numeral system.

    :param number: the initial number
    :param base_init: a base of the initial number
    :param base_final: a base of the final number
    :return: converted number
    """
    base_init, base_final = _bases_validate(base_init, base_final)

    if base_init == 10:
        return _convert_dec_to_other(number, base_final)
    if base_final == 10:
        return str(_convert_to_dec(number, base_init))
    return _convert_dec_to_other(
        _convert_to_dec(number, base_init), base_final
    )


def _bases_validate(init: int, final: int) -> Tuple[int, int]:
    try:
        init = int(init)
    except ValueError:
        raise ValueError("Base of the number must be numeric.") from None
    try:
        final = int(final)
    except ValueError:
        raise ValueError("Base of the number must be numeric.") from None

    if not (1 < init < 37) or not (1 < final < 37):
        raise ValueError(
            "Base of the number must be at least 2 and not more than 36."
        )

    return init, final


def _convert_to_dec(number: str, base: int) -> int:
    """Convert a number to the decimal numeral system.

    :param number: the initial number
    :param base: a base of the initial number
    :return: converted number
    """
    try:
        return int(str(number), base=base)
    except ValueError:
        raise ValueError("Invalid number base.") from None


def _convert_dec_to_other(number: Union[int, str], base: int) -> str:
    """Convert the decimal number to another numeral system.

    :param number: the initial number
    :param base: a base of the final number
    :return: converted number
    """
    try:
        number = int(number)
    except ValueError:
        raise ValueError(
            "The decimal number can only consist of digits."
        ) from None

    if base == 2:
        return bin(number)[2:]
    if base == 8:
        return oct(number)[2:]
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
