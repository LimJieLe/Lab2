import Lab2

def test_get_user_input():
    result = Lab2.get_user_input()
    test = None
    assert (result != test)

def test_calc_average():
    txt = [2, 3, 4, 5]
    result = Lab2.calc_average(txt)
    test = 3.5

    assert (result == test)