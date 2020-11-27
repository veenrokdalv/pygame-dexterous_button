import random
import pygame as pg

class Button:
    """
    Класс кнопки.
    Содержит все атрибуты и методы кнопки.
    """
    
    def __init__(self, window: object, width: int, height: int, color: tuple):
        """Инициализация всех настроек кнопки.

        Arguments:
            window {object} -- Поверхность, на которой будет отображаться кнопка.
            width {int} -- Ширина кнопки.
            height {int} -- Высота кнопки.
            color {tuple} -- Цвсет кнопки в формате RGB (R, G, B).
        """

        self.window = window

        self.width = width
        self.height = height
        self.color = color
        self.pos_x = random.randrange(0, pg.display.get_window_size()[0] - self.height)
        self.pos_y = random.randrange(0, pg.display.get_window_size()[1] - self.height)

