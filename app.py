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
        self._color_fon = (20, 20, 20)
        self.width = 640
        self.heigth = 480
        self.caption = 'Ловкая кнопка'

        self._fps = 60
        self._clock = pg.time.Clock()

        # Инициализация окна
        self.window = pg.display.set_mode((self.width, self.heigth))
        pg.display.set_caption(self.caption)

        # Экземпляр кнопки
        self.button = button.Button(self.window, 90, 30, (220, 20, 20))


    def _quit(self):
        """Завершение программы"""
        pg.quit()
        quit()


    
    def _check_events(self):
        """Обработка событий приложения"""

        [self._quit() for event in pg.event.get() if event.type == pg.QUIT]

        keys = pg.key.get_pressed()

        if keys[pg.K_u]:
            self.button.set_position()

    
    def _draw(self):
        """Отрисовка объектов в окне"""
        self.window.fill(self._color_fon)
        self.button.draw()
        pg.display.update()


    def _update_position(self):
        """Обновляет положение объектов в окне"""
        self.button.update_position()


    def run(self):
        """Основной цикл приложения"""
        while True:
            self._check_events()
            self._update_position()
            self._draw()

            self._clock.tick(self._fps)


    


    
