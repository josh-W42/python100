import tkinter


def handle_button_press() -> None:
    """
    When the "Calculate" button is pressed this function will
    trigger the necessary functions to both perform the conversion from miles
    to Km and also update the view.
    """
    try:
        miles = float(miles_field.get())
        km = 1.60934 * miles
        km_label.config(text=km)
    except ValueError:
        print("Could not convert str to float")
        miles_field.config(border="red")


# Initialize the GUI
gui = tkinter.Tk()
gui.title("Convert Miles to Kilometers")
gui.minsize(width=250, height=75)
gui.config(padx=25, pady=20)

# Configure assets.
submit_button = tkinter.Button(text="Calculate", command=handle_button_press)

miles_field = tkinter.Entry(width=10)

km_pre_label = tkinter.Label(text="is equal to")
km_post_label = tkinter.Label(text="Km")

km_label = tkinter.Label()

miles_label = tkinter.Label(text="Miles")

# Render
submit_button.grid(row=2, column=1)
miles_field.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
km_pre_label.grid(row=1, column=0)
km_post_label.grid(row=1, column=2)
km_label.grid(row=1, column=1)

gui.mainloop()
