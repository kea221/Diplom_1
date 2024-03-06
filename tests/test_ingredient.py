from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_ingredient_type_true(self):
        ing = Ingredient("FILLING", "Сыр с астероидной плесенью", 20.0)
        assert ing.type == "FILLING"

    def test_name_of_ingredient_true(self):
        ing = Ingredient("FILLING", "Сыр с астероидной плесенью", 20.0)
        assert ing.name == "Сыр с астероидной плесенью"

    def test_price_of_ingredient_true(self):
        ing = Ingredient("FILLING", "Сыр с астероидной плесенью", 20.0)
        assert ing.price == 20.0

    def test_get_price_price_got(self):
        ing = Ingredient("FILLING", "Сыр с астероидной плесенью", 20.0)
        assert ing.get_price() == 20.0

    def test_get_name_name_got(self):
        ing = Ingredient("начинка", "Сыр с астероидной плесенью", 20.0)
        assert ing.get_name() == "Сыр с астероидной плесенью"

    def test_get_type_type_got(self):
        ing = Ingredient("FILLING", "Сыр с астероидной плесенью", 20.0)
        assert ing.get_type() == "FILLING"
