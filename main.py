import tkinter as tk

HEIGHT = 480
WIDTH = 800

input = "adsfdasf"

def test_function(entry):
	print("This is the entry:", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg = "#121113")
canvas.pack()

top_frame = tk.Frame(root, bg='#121113', bd=5)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

title = tk.Label(top_frame, anchor='center', bg='#121113', fg='white', text="Gas Concentration Detection System", font=('Arial',15))
title.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#121113', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

value = tk.Label(lower_frame, anchor='center', bg='#121113', fg='white', text=input+"PPM")
value.place(relwidth=1, relheight=1)

root.mainloop()

"""
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            input = ser.readline().decode('utf-8').rstrip()

root = Tk() 
value = Label(root, anchor='center', bg='#121113', fg='white', text=input) 
value.insert(1.0, " ")
value.pack() 
root.geometry("800x480")
root['background'] = '#121113'
root.mainloop() 
"""