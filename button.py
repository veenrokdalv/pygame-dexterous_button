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

        self.btn = pg.Surface((self._width, self._height))
        self.btn.fill(self._color)

        self.rect_btn = self.btn.get_rect(topleft=(self._pos_x, self._pos_y))

        self.font = pg.font.SysFont(None, 24)
        self.render = self.font.render('Нажми меня!', True, (50, 50, 50))

        self.rect_render = self.render.get_rect(center=(self._width//2, self._height//2))
        
        self.btn.blit(self.render, self.rect_render)

    
    def draw(self):
        """Отрисовка кнопки"""
        self.window.blit(self.btn, self.rect_btn)
    
    def update_position(self):
        """Обновление положния"""
        self.check_collision_cursor()
        self.rect_btn = self.btn.get_rect(topleft=(self._pos_x, self._pos_y))
        
    
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


