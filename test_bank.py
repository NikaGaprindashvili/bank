import bank


def test_hello():
    assert bank.value("hello world") == 0
    assert bank.value("Hello, how are you?") == 0
    assert bank.value("HELLO") == 0


def test_h():
    assert bank.value("hi there") == 20
    assert bank.value("hey!") == 20
    assert bank.value("Hooray!") == 20


def test_other():
    assert bank.value("what's up?") == 100
    assert bank.value("goodbye") == 100
    assert bank.value("123") == 100
