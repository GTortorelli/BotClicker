import pyautogui

mouse_commands = pyautogui

def get_current_mouse_position() -> dict:
    """Gets the coordinates os the mouse on screen
       return format:
      {"X": currentMouseY, "Y": currentMouseY}
    """
    current_mouse_x = mouse_commands.position().x
    current_mouse_y = mouse_commands.position().y
    return {"X": f"{current_mouse_x}", "Y": f"{current_mouse_y}"}
