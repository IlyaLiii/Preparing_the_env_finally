"""Генератор приветствий."""

def Greeting(name: str) -> str:
    """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          int: Текст приветствия
      """
    name = name.title()
    return 'Привет, {}'.format(name)
