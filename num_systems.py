"""Module for converting numbers to various numeral systems."""

from typing import Union


def convert(number: Union[int, str], base_init: int, base_final: int) -> str:
    """Convert a number to another numeral system.

    :param number: the initial number
    :param base_init: a base of the initial number
    :param base_final: a base of the final number
    :return: converted number
    """
    _bases_validate(base_init, base_final)

    if base_init == 10:
        return _convert_dec_to_other(number, base_final)
    if base_final == 10:
        return str(_convert_to_dec(number, base_init))
    return _convert_dec_to_other(
        _convert_to_dec(number, base_init), base_final
    )


def _bases_validate(init: int, final: int):
    if not isinstance(init, int) or not isinstance(final, int):
        raise ValueError("Base of the number must be integer.")

    if not (1 < init < 37) or not (1 < final < 37):
        raise ValueError(
            "Base of the number must be at least 2 and not more than 36."
        )


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

    if number < 10 and number < base:
        return str(number)

    if base == 2:
        return bin(number)[2:]
    if base == 8:
        return oct(number)[2:]
    if base == 16:
        return hex(number)[2:].upper()

    result = ""
    while number:
        mod = number % base
        result = f"""{(chr(mod + (48 if mod < 10 else 55))
                        if base > 10 else str(mod))}{result}"""
        number //= base

    return result.upper()
