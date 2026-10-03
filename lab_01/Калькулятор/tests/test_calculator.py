from toolkit.calculator import calculate


class TestCalculator:
    def test_add(self):
        assert calculate("2 + 2") == 4 #assert проверка кода, если нет то ложь

    def test_subtract(self):
        assert calculate("5 - 3") == 2

    def test_division(self):
        assert calculate("10 / 2") == 5

    def test_unary_minus(self):
        assert calculate("-5 * 3") == -15

    def test_float_numbers(self):
        assert calculate("1.5 + 2.5") == 4

    def test_multiply(self):
        assert calculate("3 * 4") == 12
