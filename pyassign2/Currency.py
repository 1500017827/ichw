"""Currency.py: Exchange of two types of Currency.

__author__ = "Zhou Xu-yuan"
__pkuid__  = "1500017827"
__email__  = "1500017827@pku.edu.cn"
"""


def get_from(url):
    """
    This function sends the url to the website and turn the feedback to a string

    :param url: the url created by the user's input

    :return: the answer received from the website, which has type float
    """
    from urllib.request import urlopen

    doc = urlopen(url)
    doc_str = doc.read()
    doc.close()
    j_str = doc_str.decode('ascii')

    return j_str


def is_leg_input(w):
    """
    This function checks the legacy of the user's input
    if the exchange is successful, the function will return '0'
    otherwise, the function will return the error information
    :param w: a list that created from the answer received from the website
    :return: '0' for no error, and the error information for error
    """
    c = w[10]
    if c == ' : true, ':
        return 0
    else:
        return w[13]


def exchange(currency_from, currency_to, amount_from):
    """
    In this function, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    :param currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    :param currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    :param amount_from: amount of currency to convert
    Precondition: amount_from is a float

    :return: amount of currency received in the given exchange
    The value returned has type float
    """
    s = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
    s += currency_from
    s += '&to='
    s += currency_to
    s += '&amt='
    s += amount_from
    t = get_from(s)
    b = t.split('"')
    p = is_leg_input(b)
    if p == 0:
        c = b[7]
        d = c.split()
        e = d[0]
        f = float(e)
        return f
    else:
        return p


def cur_exc():
    """
    Module for currency exchange

    This module provides several string parsing functions to implement a
    simple currency exchange routine using an online currency service.
    The primary function in this module is exchange.
    """
    cf = input('origin currency =')
    ct = input('target currency =')
    af = input('amount of origin currency =')
    r = exchange(cf, ct, af)
    print(r)


def test_get_from():
    """
    This function tests the function 'get_from()'
    """
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }' ==
           get_from('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5'))


def test_is_leg_input():
    """
        This function tests the function 'is_leg_input()'
    """
    assert (0 == is_leg_input(['{ ', 'from', ' : ', '2.5 United States Dollars', ', ', 'to', ' : ',
                               '2.0952375 Euros', ', ', 'success', ' : true, ', 'error', ' : ', '', ' }']))
    assert('Source currency code is invalid.' == is_leg_input(['{ ', 'from', ' : ', '', ', ', 'to', ' : ', '', ', ',
                                                               'success', ' : false, ', 'error', ' : ',
                                                               'Source currency code is invalid.', ' }']))
    assert('Currency amount is invalid.' == is_leg_input(['{ ', 'from', ' : ', '', ', ', 'to', ' : ', '', ', ',
                                                                'success', ' : false, ', 'error', ' : ',
                                                                'Currency amount is invalid.', ' }']))


def test_exchange():
    """
        This function tests the function 'exchange()'
    """
    assert(13.0523 == exchange('USD', 'CNY', '2'))


def testAll():
    """
        This function tests all cases
    """
    test_get_from()
    test_is_leg_input()
    test_exchange()
    print("All tests passed")


def main():
    x = input('''What do you want to do? 
    input 'c' for running the calculator; 
    input 't' for running the test.''')

    if x == 't':
        testAll()
    elif x == 'c':
        cur_exc()
    else:
        print('''You have input an wrong value, please input 't' or 'r' for the next time''')


if __name__ == '__main__':
    main()
