from gui import *
from tkinter import Tk


def main() -> None:
    """
    Initializes and runs the main calculator window using Tkinter.

    This function creates the main window for the calculator application,
    sets its title, size, and properties, and then runs the Tkinter main loop.
    It also initializes the GUI class for the calculator.

    Returns:
        None
    """
    window = Tk()
    window.title('Calculator')
    window.geometry('550x350')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
