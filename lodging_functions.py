# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:52:56 2017

@author: William
"""

# %%
import locale


# %%
locale.setlocale(locale.LC_ALL, '')


# %%
# Tax Constants assume Davidson County, TN
SALES_TAX = .1525
LODGING_TAX = 2.5
AAA_DISCOUNT = .10
# Discount & Commission Constants
MANAGERS_DISCOUNT = .15
EXPEDIA_DISCOUNT = .10
EXPEDIA_COMMISSION = .17
# Test Values
RACK_RATE = 117.95
RACK_TOTAL = 138.44
ROOM_TOTALS_LIST = [x for x in range(100, 200, 5)]


# %%
def add_tax(rate):
    """
    Given a number rate, return rate with tax

    Parameters
    ----------
    rate: number
        A dollar value representing the daily rate

    Returns
    -------
    res: number
        Total with tax added, computed using given SALES_TAX and LODGING_TAX

    Example
    -------
    >>> add_tax(101.95)
    120.00

    """
    tax = SALES_TAX + 1
    return (rate * tax) + LODGING_TAX


# %%
def remove_tax(total):
    """
    Given a total, return the rate without tax

    Parameters
    ----------
    total: number
        A dollar value representing the grand total after tax

    Returns
    -------
    res: number
        The rate, with given SALES_TAX and LODGING_TAX removed

    Example
    -------
    >>> remove_tax(120.00)
    101.95

    """
    tax = SALES_TAX + 1
    return (total - LODGING_TAX) / tax


# %%
def make_currency_pretty(number):
    """
    Given a number, return the properly formatted local currency

    Parameters
    ----------
    number: real number
        A real number

    Returns
    -------
    res: string
        A string of properly formatted local currency

    Example
    -------
    >>> make_pretty_currency(101.954)
    $101.95

    """
    acc = round(number, 2)
    return locale.currency(acc, grouping=True)


# %%
def add_taxes(lor):
    """
    Given a list of rates, returns a list of totals

    Parameters
    ----------
    lot: list of numbers
        a list of rates

    Returns
    -------
    res: list of numbers
        a list of totals after tax

    """
    acc = []
    for rate in lor:
        acc.append(add_tax(rate))
    return acc


# %%
def remove_taxes(lot):
    """
    Given a list of totals, returns a list of rates

    Parameters
    ----------
    list: list of numbers
        a list of totals after tax

    Returns
    -------
    res: list of numbers
        a list of rates

    """
    acc = []
    for total in lot:
        acc.append(remove_tax(total))
    return acc


# %%
def make_currencies_pretty(lor):
    """
    Given a list of rates, returns a list of properly formatted local currency

    Parameters
    ----------
    lor: list of numbers
        a list of rates

    Returns
    -------
    res: a list of strings
        a list of strings of pretty currency

    """
    acc = []
    for rate in lor:
        acc.append(make_currency_pretty(rate))
    return acc


# %%
def apply_discount(rate, discount):
    """
    Given a rate and a discount, returns new rate decremented by a percent

    Parameters
    ----------
    rate: number
        a number representing a currency value

    discount: number
        a decimal number representing a percentage

    Returns
    -------
    res: number
        a discounted rate

    Example
    -------
    >>> apply_discount(117.95, .10)
    106.16

    """
    return rate - (rate * discount)


# %%
def remove_discount(rate, discount):
    """
    Given a rate and a discount, returns rate incremented by a percent

    Parameters
    ----------
    rate: number
        a number representing a currency value

    discount: number
        a decimal number representing a percentage

    Returns
    -------
    res: number
        a rate without the discount applied

    Example
    -------
    >>> remove_discount(106.16, .10)
    117.95

    """
    return rate + (rate / discount)


# %%
def expedia_price(rate, discount, commission):
    """
    Creates the expedia_price() value by first applying the discount to the
    rate, then decrementing the accumulator by the commission percentage

    Parameters
    ----------
    rate: number
        a number representing a currency value

    discount: number
        a decimal number representing a percentage

    commission: number
        a decimal number representing a percentage

    Returns
    -------
    res: number
        an estimate of the price offered through Expedia.com

    Example
    -------
    >>> expedia_price(117.95, .10, .17)
    88.11

    """

    acc = apply_discount(rate, discount)
    return apply_discount(acc, commission)


# %%
def rate_from_expedia(total, discount, commission):
    """
    Given an Expedia.com rate and the associatdd discount and commision,
    returns the original rack rate

    Parameters
    ----------
    total: number
        a number representing a rate offered on Expedia.com

    discount: number
        a decimal number representing a percentage

    commission: number
        a decimal number representing a percentage

    Returns
    -------
    res: number
        the rack rate the given expedia rate would be derived from

    Example
    -------
    >>> rate_from_expedia(88.11, .10, .17)
    117.95

    """

    acc = remove_discount(total, discount)
    return remove_discount(acc, commission)


# %%
if __name__ == "__main__":
    room_rates_list = [RACK_RATE,
                       apply_discount(RACK_RATE, AAA_DISCOUNT),
                       apply_discount(RACK_RATE, MANAGERS_DISCOUNT),
                       expedia_price(RACK_RATE,
                                     EXPEDIA_DISCOUNT,
                                     EXPEDIA_COMMISSION)]
    room_totals_list = add_taxes(room_rates_list)
    pretty_room_rates = make_currencies_pretty(room_rates_list)
    pretty_room_totals = make_currencies_pretty(room_totals_list)
    print(pretty_room_rates)
    print(pretty_room_totals)
