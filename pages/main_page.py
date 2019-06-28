from .base_page import BasePage


class MainPage(BasePage):
    """Т.к не осталось никаких методов, заглушка:"""
    def __init__(self, *args, **kwargs):
        """метод __init__ вызывается при создании объекта.
        Конструктор ключевым словом super на самом деле только вызывает конструктор класса предка
        и передает ему все те аргументы, которые мы передали в конструктор MainPage"""
        super(MainPage, self).__init__(*args, **kwargs)
