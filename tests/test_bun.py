from praktikum.bun import Bun


class TestBun:
    def test_name_and_price_of_bun_true(self):
        bun = Bun("Марсианская", 55.0)
        assert bun.name == "Марсианская" and bun.price == 55.0

    def test_get_name_name_got(self):
        bun = Bun("Красный гигант", 65.5)
        assert bun.get_name() == "Красный гигант"

    def test_get_price_price_got(self):
        bun = Bun("Красный гигант", 65.5)
        assert bun.get_price() == 65.5
