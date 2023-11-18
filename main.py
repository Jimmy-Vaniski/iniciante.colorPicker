from tkinter import *
import tkinter.messagebox


# Colors
c1 = "#444466"  # black
c2 = "#feffff"  # white
c3 = "#004338"  # hunter green

# Creating window
window = Tk()
window.geometry("530x205")
window.configure()
window.title('Color Selector')

# Creating label and frames
display = Label(window, bg=c1, width=40, height=10, bd=1)
display.grid(row=0, column=0, padx=5)

display2 = Frame(window, bg=c2, padx=3)
display2.grid(row=0, column=1)

display3 = Frame(window)
display3.grid(row=1, column=0, columnspan=2, pady=15)

# Creating sliders
l_red = Label(display2, text='Red', width=7, bg=c2, fg='red', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_red.grid(row=0, column=0)

slider_red = Scale(display2, from_=0, to=255, length=150, bg=c2, fg='red', orient=HORIZONTAL)
slider_red.grid(row=0, column=1)

l_blue = Label(display2, text='Blue', width=7, bg=c2, fg='blue', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_blue.grid(row=1, column=0)

slider_blue = Scale(display2, from_=0, to=255, length=150, bg=c2, fg='blue', orient=HORIZONTAL)
slider_blue.grid(row=1, column=1)

l_green = Label(display2, text='Green', width=7, bg=c2, fg='green', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_green.grid(row=2, column=0)

slider_green = Scale(display2, from_=0, to=255, length=150, bg=c2, fg='green', orient=HORIZONTAL)
slider_green.grid(row=2, column=1)

# Configuring under frame
l_rgb = Label(display3, text='Color Code: ', bg=c2, font=('Ivy', 10, 'bold'))
l_rgb.grid(row=0, column=0, padx=3)

entry_color = Entry(display3, width=12, font=('Ivy', 10, 'bold'), justify=CENTER)
entry_color.grid(row=0, column=1, padx=5)

# Button copy
button_copy = Button(display3, text='Copy Color', bg=c2, font=('Ivy', 10, 'bold'), relief=RAISED, overrelief=RIDGE)
button_copy.grid(row=0, column=2, padx=5)

# App name
l_name = Label(display3, text='Color Selector', bg=c2, font=('Ivy', 16, 'bold'))
l_name.grid(row=0, column=3, padx=40)


window.mainloop()


