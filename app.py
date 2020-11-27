import pygame as pg
import button

class App:
    """Класс приложения.
    Управляет всеми процессами приложения.
    """

    def __init__(self):
        """Инициализация главных настроек приложения"""

        # Иницализация pg
        pg.init()

        # Настройки окна
        self.width = 640
        self.heigth = 480
        self.caption = 'Ловкая кнопка'

        # Инициализация окна
        self.window = pg.display.set_mode((self.width, self.heigth))
        pg.display.set_caption(self.caption)

        # Экземпляр кнопки
        self.button = button.Button(self.window, 60, 20, (20, 20, 20))
