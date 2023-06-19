from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("ovo")
    ingredient2 = Ingredient("manteiga")

    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1.__hash__() == ingredient1.__hash__()

    assert ingredient1.__eq__(ingredient2) is False
    assert ingredient1.__eq__(ingredient1) is True

    assert ingredient1.__repr__() == "Ingredient('ovo')"

    assert ingredient1.name == "ovo"
    assert ingredient2.name == "manteiga"

    assert ingredient1.restrictions == {Restriction.ANIMAL_DERIVED}
