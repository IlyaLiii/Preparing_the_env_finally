from pytest import mark

from main import greeting

TEST_DATA = (('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга'))


@mark.parametrize('name,expected', TEST_DATA)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greeting(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'яндекс практикум'
    assert greeting(name) == 'Привет, Яндекс Практикум'
