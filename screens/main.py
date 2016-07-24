# coding=utf-8
import pygame

from elements.label import Label
from elements.button import Button
from elements.image import Image

from .names import NamesScreen

from .screen import Screen

class MainScreen(Screen):
    def __init__(self, screen, **kwargs):
        super(MainScreen, self).__init__(screen)

        self.objects.append(Image(
            self.screen,
            pos=(30, 20)
        ))

        self.objects.append(Label(
            self.screen,
            text = u'member auswählen',
            pos=(65, 250),
            size=50
        ))

        i = 0
        for c in range(97, 97+26):
            text = str(chr(c))
            self.objects.append(Button(
                self.screen,
                text = text,
                pos=self.__get_pos(i),
                click=self.switch_to_screen,
                click_param=text
            ))

            i += 1

        self.objects.append(Button(
            self.screen,
            text='Abbrechen',
            pos=(150, 750),
            size=30,
            click=self.home,
        ))              

    def switch_to_screen(self, param, pos):
        from .screen_manager import ScreenManager
        screen_manager = ScreenManager.get_instance()
        screen_manager.set_active(
            NamesScreen(self.screen, param)
        )

    def home(self, param, pos):
        from .screen_manager import ScreenManager
        screen_manager = ScreenManager.get_instance().set_default()

    def __get_pos(self, i):

        x = i * 60
        y = 10
        dd = 7

        breaks = [7, 14, 21]

        j = 1
        for b in breaks:
            if i > b:
                y = j * 100
                x = (i - b - 1) * 60
            j += 1

        return (x + 20, y + 350)
