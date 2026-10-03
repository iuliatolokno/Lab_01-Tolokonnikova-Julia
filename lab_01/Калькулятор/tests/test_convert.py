from toolkit.converter import convert


class TestConverter:
    def test_from_m_to_km(self):
        assert convert(100, "m", "km") == 0.1

    def test_from_cm_to_m(self):
        assert convert(100, "cm", "m") == 1.0

    def test_from_kg_to_g(self):
        assert convert(1.5, "kg", "g") == 1500.0

    def test_same_units(self):
        assert convert(5, "m", "m") == 5.0



