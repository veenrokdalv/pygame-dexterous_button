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

        self._width = width
        self._height = height
        self._color = color
        self._pos_x = random.randrange(0, pg.display.get_window_size()[0] - self._width)
        self._pos_y = random.randrange(0, pg.display.get_window_size()[1] - self._height)

        self._object = pg.Surface((self._width, self._height))
        self._rect = self._object.get_rect(topleft=(self._pos_x, self._pos_y))
        self._object.fill(self._color)

        self.font = pg.font.SysFont()

    
    def draw(self):
        """Отрисовка кнопки"""
        self.window.blit(self._object, self._rect)
    
    def update_position(self):
        """Обновление положния"""
        self.check_collision_cursor()
        self._rect = self._object.get_rect(topleft=(self._pos_x, self._pos_y))
        
    
    def set_position(self):
        """Изменение значений self.pos_x, self.pos_y"""
        self._pos_x = random.randrange(0, pg.display.get_window_size()[0] - self._width)
        self._pos_y = random.randrange(0, pg.display.get_window_size()[1] - self._height)
    
    def check_collision_cursor(self):
        """Проверяет пересечение с курсором"""
        mouse_x = pg.mouse.get_pos()[0]
        mouse_y = pg.mouse.get_pos()[1]
        if self._pos_x <= mouse_x and (self._pos_x + self._width) >= mouse_x:
            if self._pos_y < mouse_y and (self._pos_y + self._height) > mouse_y:
                self.set_position()


