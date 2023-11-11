from tkinter import *

# Also note above, different way to import.

# This capture is all about creating GUI using tkinter lib.

window = Tk()

window.title("A GUI")
window.minsize(width=500, height=300)

# Labels

my_label = Label(text="This is a cool label", font=("Arial", 24, "bold"))
# my_label.pack()

# How to update a tkinter label (Reminder, a label could just be text.)

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_event():
    print("Button has been pressed")
    my_label.config(text=text_entry.get())


button = Button(text="Click Me", command=button_event)
# button.pack()

text_entry = Entry(width=10)
text_entry.insert(END, string="Default text")
# text_entry.pack()

# Text areas
text_area = Text(height=5, width=30)
text_area.focus()
# Add some text to begin with.
text_area.insert(END, "Multi-line text entry")
# Retrieves current value in textbox
print(text_area.get("1.0", END))
# text_area.pack()


# Spinbox (or a number incrementer or decrement(or)
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# Scales
def scale_used():
    print(scale.get())


scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


# Checkboxes
def checkbox_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
# check_button.pack()


# Radio buttons. to hold on to which radio button value is checked
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

# radio_1.pack()
# radio_2.pack()


# Listboxes
def listbox_used():
    print(listbox.curselection())


listbox = Listbox(height=2)
fruits = ["Apple", "Orange"]
for i in range(len(fruits)):
    listbox.insert(i, fruits[i])
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# Pack, Place, and Grid
"""
    In tkinter there's three methods of
    placing one of these complex objects in the GUI
    
    There's pack: which we've been using, which will just place the items
    in the GUI one after another with not a lot of direction or control
    
    There's Place: Which is like the opposite, you have control over the
    exact placement of the item.
    
    Then there's Grid: Which is like a flexible inbetween. Note that you cannot
    utilize grid and pack in the same program.

"""

# my_label.pack()
# my_label.place(x=10, y=100)
# my_label.grid(row=0, column=0)

#  Challenge: new orientation

new_button = Button(text="New button")
new_button.grid(row=0, column=3)

my_label.grid(row=0, column=0)
button.grid(row=1, column=1)
text_entry.grid(row=2, column=4)

# Padding - You can add padding like you would in HTML and CSS
my_label.config(padx=100, pady=100)

window.mainloop()

# Practicing *args
#
# def add(*args):
#     return sum(args)
#
#
# user_input = input("Please give me numbers separated by commas (exit to close): ").strip()
# while user_input != 'exit':
#     try:
#         print(add(*[float(x.strip()) for x in user_input.split(",")]))
#     except ValueError:
#         print("Please only input numbers.")
#     user_input = input('Please give me numbers separated by commas (exit to close): ').strip()
#
#
