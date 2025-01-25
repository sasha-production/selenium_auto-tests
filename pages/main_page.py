from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    # В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        # Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает
        # ему все те аргументы, которые мы передали в конструктор MainPage
        # pass второй вариант