from tkinter import *
from calculator import Calculator  # Import the Calculator class


class Gui:
    def __init__(self, window: Tk) -> None:
        """
        Initialize the GUI with both Basic and Area calculators.

        Args:
            window (Tk): The root window for the Tkinter application.
        """
        self.window = window
        self.calculator = Calculator()  # Create an instance of the Calculator class

        # Initialize both modes (Basic and Area calculators)
        self.init_basic_calculator()
        self.init_area_calculator()

        # Start with Basic Calculator as the default
        self.show_basic_calculator()

    def init_basic_calculator(self) -> None:
        """
        Initialize the Basic Calculator GUI components.
        """
        self.basic_frame = Frame(self.window)

        # Display screen (readonly)
        self.screen_var = StringVar()  # Create a StringVar to manage the screen's text
        self.screen = Entry(self.basic_frame, width=50, font=("Arial", 16), justify="right", state="readonly",
                            textvariable=self.screen_var)
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons
        buttons = [
            "x^2", "Mode", "DEL", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "CE", '0', '.', "="
        ]

        # Button layout
        row, col = 1, 0
        for button in buttons:
            cmd = lambda b=button: self.on_button_click(b)
            if button == "Mode":
                Button(self.basic_frame, text=button, width=10, height=2, command=self.show_area_calculator).grid(
                    row=row, column=col, padx=2, pady=2)
            else:
                Button(self.basic_frame, text=button, width=10, height=2, command=cmd).grid(row=row, column=col, padx=2,
                                                                                            pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def init_area_calculator(self) -> None:
        """
        Initialize the Area Calculator GUI components.
        """
        self.area_frame = Frame(self.window)

        # Mode Button
        Button(self.area_frame, text="Back to Basic", command=self.show_basic_calculator, width=20).pack(pady=10)

        # Radio buttons for selecting shapes
        self.frame_shape = Frame(self.area_frame)
        self.label_operation = Label(self.frame_shape, text="Shape\t")
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text="Circle", variable=self.radio_1, value=1,
                                        command=self.shape)
        self.radio_square = Radiobutton(self.frame_shape, text="Square", variable=self.radio_1, value=2,
                                        command=self.shape)
        self.radio_rectangle = Radiobutton(self.frame_shape, text="Rectangle", variable=self.radio_1, value=3,
                                           command=self.shape)
        self.radio_triangle = Radiobutton(self.frame_shape, text="Triangle", variable=self.radio_1, value=4,
                                          command=self.shape)
        self.label_operation.pack(side="left", padx=5)
        self.radio_circle.pack(side="left")
        self.radio_square.pack(side="left")
        self.radio_rectangle.pack(side="left")
        self.radio_triangle.pack(side="left")
        self.frame_shape.pack(anchor="w", pady=10)

        # Input fields for the first and second numbers
        self.frame_first = Frame(self.area_frame)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side="left")
        self.entry_first.pack(padx=20, side="left")
        self.frame_first.pack(anchor="w", pady=10)
        self.entry_first.pack_forget()

        self.frame_second = Frame(self.area_frame)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side="left")
        self.entry_second.pack(padx=20, side="left")
        self.frame_second.pack(anchor="w", pady=10)
        self.entry_second.pack_forget()

        # Results label
        self.frame_result = Frame(self.area_frame)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.area_frame)
        self.button_compute = Button(self.frame_button, text="COMPUTE", command=self.compute_area)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def show_basic_calculator(self) -> None:
        """
        Show the Basic Calculator and hide the Area Calculator.
        """
        # Hide Area Calculator
        self.area_frame.pack_forget()

        # Make sure the Basic Calculator is displayed
        self.basic_frame.pack()
        self.screen_var.set("")  # Optionally reset the calculator screen

    def show_area_calculator(self) -> None:
        """
        Show the Area Calculator and hide the Basic Calculator.
        """
        # Hide Basic Calculator
        self.basic_frame.pack_forget()

        # Make sure the Area Calculator is displayed
        self.area_frame.pack()

    def shape(self) -> None:
        """
        Adjust inputs based on the selected shape in the Area Calculator.
        """
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text="")
        self.entry_first.pack()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_first.config(text="Radius")
            self.label_second.config(text="")
            self.entry_second.pack_forget()
        elif shape == 2:
            self.label_first.config(text="Side")
            self.label_second.config(text="")
            self.entry_second.pack_forget()
        elif shape == 3:
            self.label_first.config(text="Length")
            self.label_second.config(text="Width")
            self.entry_second.pack()
        elif shape == 4:
            self.label_first.config(text="Base")
            self.label_second.config(text="Height")
            self.entry_second.pack()

    def compute_area(self) -> None:
        """
        Compute the area for the selected shape.
        """
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            shape = self.radio_1.get()

            if shape == 1:
                result = self.calculator.compute_area("circle", float(first_num))
                self.label_result.config(text=f"Circle area = {result}")
            elif shape == 2:
                result = self.calculator.compute_area("square", float(first_num))
                self.label_result.config(text=f"Square area = {result}")
            elif shape == 3:
                result = self.calculator.compute_area("rectangle", float(first_num), float(second_num))
                self.label_result.config(text=f"Rectangle area = {result}")
            elif shape == 4:
                result = self.calculator.compute_area("triangle", float(first_num), float(second_num))
                self.label_result.config(text=f"Triangle area = {result}")
            else:
                self.label_result.config(text="No shape selected")
        except ValueError:
            self.label_result.config(text="Enter valid numeric values")
        except TypeError:
            self.label_result.config(text="Values must be positive")

    def on_button_click(self, button: str) -> None:
        """
        Handle button clicks for the Basic Calculator.

        Args:
            button (str): The text of the clicked button.
        """
        current_text = self.screen_var.get()  # Get the current text from the screen

        if button == "CE":
            self.screen_var.set("")  # Clear entry
        elif button == "DEL":
            self.screen_var.set(current_text[:-1])  # Remove the last character
        elif button == "=":
            try:
                # Evaluate the expression and update the screen
                result = eval(current_text)
                self.screen_var.set(str(result))
            except Exception:
                self.screen_var.set("Error")  # Display error if the expression is invalid
        elif button == "x^2":
            try:
                # Square the number
                result = float(current_text) ** 2
                self.screen_var.set(str(result))
            except ValueError:
                self.screen_var.set("Error")  # If input is not a valid number, show error
        elif button == ".":
            # Prevent multiple decimal points in the same number
            if "." not in current_text:
                self.screen_var.set(current_text + ".")
        else:
            # Add the button's value to the current text
            self.screen_var.set(current_text + button)
