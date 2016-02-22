#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that converts Fahrenheit to Celsius
    and displays the result as a decimal.
    """

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def kelvin_to_celsius(degrees):
    """Defines a function that converts Kelvin to Celsius

    Args:
        degrees (int): Degrees in Kelvin.

    Returns:
        decimal: Degrees converted to Celsius.

    Examples:
        >>> kelvin_to_celsius(373.15)
        Decimal('100')

        >>> kelvin_to_celsius(273.15)
        Decimal('0')
    """

    return decimal.Decimal(degrees) - ABSOLUTE_DIFFERENCE


def celsius_to_fahrenheit(degrees):
    """Defines a function that converts Celsius to Fahrenheit.

    Args:
        degrees (int): Degrees in Celsius.

    Returns:
        decimal: Degrees converted to Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(100)
        Decimal('212')

        >>> celsius_to_fahrenheit(0)
        Decimal('32')
    """

    return (decimal.Decimal(degrees) * 1.8) + 32


def kelvin_to_fahrenheit(degrees):
    """Defines a function that converts Kelvin to Fahrenheit

    Args:
        degrees (int): Degrees in Kelvin

    Returns:
        decimal: Degrees converted to Fahrenheit

    Examples:
        >>> fahrenheit_to_kelvin(373.15)
        Decimal('212')

        >>>fahrenheit_to_kelvin(273.16)
        Decimal('32')
    """

    return celsius_to_fahrenheit(kelvin_to_celsius(degrees))
