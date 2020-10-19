from app.keyboard import keyboard_commands
from app.mouse import mouse_commands


class AlphaOmega:

    def rank1(self):
        """Farming script for Alpha omega classes in rank 1"""
        print('Make sure youre close enought from enemy')
        continue_ = True
        while continue_:
            continue_ = not keyboard_commands.is_pressed('f6')

        while not continue_:
            mouse_commands.click(760, 959)
            mouse_commands.click(835, 981)
            continue_ = keyboard_commands.is_pressed('f6')

    def rank2(self):
        """Farming script for Alpha omega classes in rank 2"""
        print('Make sure youre close enought from enemy')
        while keyboard_commands.is_pressed("f6"):
            mouse_commands.click(760, 960, interval=1)
            mouse_commands.click(835, 960, interval=1)
            mouse_commands.click(910, 960, interval=1)
            mouse_commands.click(852, 137, interval=1)

    def rank3(self):
        """Farming script for Alpha omega classes in rank 3"""
        print('Make sure youre close enought from enemy')
        while keyboard_commands.is_pressed("f6"):
            mouse_commands.click(760, 960, interval=1)
            mouse_commands.click(835, 960, interval=1)
            mouse_commands.click(910, 960, interval=1)
            mouse_commands.click(852, 137, interval=1)
            mouse_commands.click(985, 960, interval=1)

    def rank4(self):
        pass

    def rank5(self):
        pass
