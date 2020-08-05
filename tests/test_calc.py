from rxtouchtoggle.calc import add, sub

# test add function
def test_add():
    assert add(1, 2) == 3

# test sub function
def test_sub():
    assert sub(2, 1) == 1
