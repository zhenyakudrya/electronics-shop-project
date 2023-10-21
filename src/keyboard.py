from src.item import *


class MixinLog:
    keyboard_lang = []

    def __init__(self):
        self.keyboard_lang = []

    def add_to_keyboard_lang(self, value):
        self.keyboard_lang.append(value)


class Keyboard(Item, MixinLog):
    __language = 'EN'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return self.__language

    # @property
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            MixinLog.add_to_keyboard_lang(MixinLog, self.__language)
        else:
            self.__language = 'EN'
            MixinLog.add_to_keyboard_lang(MixinLog, self.__language)

