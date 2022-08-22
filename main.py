from tkinter import ttk, GROOVE, SUNKEN, HORIZONTAL, SW
import tkinter as tk
import random
from bubble_sort import bubbleSort
from quick_sort import quick_sort
from merge_sort import mergesort

window = tk.Tk()
window.title("Sorting Algorithm Visualiser")
window.geometry("900x600")
window.config(bg="light grey")
data = []
# draw data
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400   # we have multiply by 400 because we will normalised our data
                                            # so that data won't exceed our  canvas
        x1 = (i+1) * x_width
        y1 = canvas_height



        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),
                           font=("new roman", 15, "italic bold"), fill="snow")
    window.update_idletasks()
def startAlgorithm():
    global data
    if not data:
        return

    if algo_menu.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    elif algo_menu.get() == "Bubble Sort":
        bubbleSort(data, drawData, speedScale.get())
    elif algo_menu.get() == "Merge Sort":
        mergesort(data, drawData, speedScale.get())
    drawData(data, ["red" for x in range(len(data))])
def Generate():
    global data
    print("Selected Algorithm " + selected_algorithm.get())

    # we will take values from our speed scale
    miniValue = int(minValue.get())
    maxiValue = int(maxValue.get())
    sizeeValue = int(sizeValue.get())

    data = []
    for _ in range(sizeeValue):
        data.append(random.randrange(miniValue, maxiValue+1))
    drawData(data, ["snow" for x in range(len(data))])


selected_algorithm = tk.StringVar()



# Label, button, speed scale

mainLabel = tk.Label(window, text="Algorithm : ",
                     font= ("new roman", 16, "italic bold"),
                     bg="light blue", width=10, fg="black",
                     relief= GROOVE, bd=5)
mainLabel.place(x=0, y=0)

algo_menu = ttk.Combobox(window, width=15,
                         font=("new roman", 20, "italic bold"),
                         textvariable=selected_algorithm,
                         values=["Bubble Sort", "Merge Sort", "Quick Sort"])
algo_menu.place(x=145, y=0)
algo_menu.current(0) # by default is Bubble sort selected


random_generate = tk.Button(window, text="Generate", bg="magenta",
                            font=("new roman", 12, "italic bold"),
                            relief=SUNKEN, activebackground="coral",
                            activeforeground="white",
                            bd=5, width=10, command=Generate)
random_generate.place(x=750, y=60)

sizeValueLabel = tk.Label(window,  text="Size: ",
                     font= ("new roman", 12, "italic bold"),
                     bg="dodger blue", width=10, fg="black", height=2,
                     relief= GROOVE, bd=5)
sizeValueLabel.place(x=0, y=60)

sizeValue = tk.Scale(window, from_=0, to=30, resolution=1, orient=HORIZONTAL,
                     font=("new roman", 14, "italic bold"), relief=GROOVE, bd=2,
                     width=10)
sizeValue.place(x=120, y=60)

minValueLabel = tk.Label(window,  text="Min Value: ",
                     font= ("new roman", 12, "italic bold"),
                     bg="dodger blue", width=10, fg="black", height=2,
                     relief= GROOVE, bd=5)
minValueLabel.place(x=250, y=60)

minValue = tk.Scale(window, from_=0, to=10, resolution=1, orient=HORIZONTAL,
                     font=("new roman", 14, "italic bold"), relief=GROOVE, bd=2,
                     width=10)
minValue.place(x=370, y=60)

maxValueLabel = tk.Label(window,  text="Max Value: ",
                     font= ("new roman", 12, "italic bold"),
                     bg="dodger blue", width=10, fg="black", height=2,
                     relief= GROOVE, bd=5)
maxValueLabel.place(x=500, y=60)

maxValue = tk.Scale(window, from_=0, to=100, resolution=1, orient=HORIZONTAL,
                     font=("new roman", 14, "italic bold"), relief=GROOVE, bd=2,
                     width=10)
maxValue.place(x=620, y=60)


start = tk.Button(window, text="Start", bg="magenta",
                            font=("new roman", 12, "italic bold"),
                            relief=SUNKEN, activebackground="coral",
                            activeforeground="white",
                            bd=5, width=10, command=startAlgorithm)
start.place(x=750, y=0)

speedLabel = tk.Label(window,  text="Speed: ",
                     font= ("new roman", 12, "italic bold"),
                     bg="dodger blue", width=10, fg="black",
                     relief= GROOVE, bd=5)
speedLabel.place(x=400, y=0)
speedScale = tk.Scale(window, from_=0.1, to=5.0, resolution=0.2, length=200,
                      digits=2, orient=HORIZONTAL,
                      font=("new roman", 14, "italic bold"),
                      relief=GROOVE, bd=2, width=10)

speedScale.place(x=520, y=0)

canvas = tk.Canvas(window, width=870, height=450, bg="black")
canvas.place(x=10, y=130)

window.mainloop()