import pyautogui as mouse_commands

def get_current_mouse_position() -> dict:
    """Gets the coordinates os the mouse on screen
       return format:
      {"X": currentMouseY, "Y": currentMouseY}
    """
    current_mouse_x, current_mouse_y = mouse_commands.position()
    return {"X": f"{current_mouse_x}", "Y": f"{current_mouse_x}"}
