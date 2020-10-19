import pyautogui


class Mouse:
    """Class that will have all the commands for the auto-clicker"""

    def get_current_mouse_position(self) -> dict:
        """Gets the coordinates os the mouse on screen
           return format:
          {"X": currentMouseY, "Y": currentMouseY}
        """
        current_mouse_x, current_mouse_y = pyautogui.position()
        return {"X": f"{current_mouse_x}", "Y": f"{current_mouse_x}"}

    def move_mouse(self, mouse_x, mouse_y) -> bool:
        """Move the mouse to the specified coordinates"""
        pyautogui.moveTo(mouse_x, mouse_y)
        return True

    def mouse_click(self) -> bool:
        """Clicks the mouse in current coordinates"""
        pyautogui.click()
        return True

