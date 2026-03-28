import tkinter as tk
from tkinter import ttk
import random
import time

root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("900x600")
root.config(bg="white")

data = []

# ---------------- DRAW BARS ----------------
def draw_data(data, color_array):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 800

    bar_width = canvas_width / len(data)
    max_val = max(data)

    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - (val / max_val * 350)
        x1 = (i + 1) * bar_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(val))

    root.update_idletasks()


# ---------------- GENERATE ARRAY ----------------
def generate_array():
    global data
    data = [random.randint(10, 100) for _ in range(30)]
    draw_data(data, ["blue" for _ in range(len(data))])


# ---------------- BUBBLE SORT ----------------
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):

            colors = ["blue"] * len(data)
            colors[j] = "red"
            colors[j+1] = "red"
            draw_data(data, colors)

            time.sleep(0.05)

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    draw_data(data, ["green"] * len(data))


# ---------------- SELECTION SORT ----------------
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i

        for j in range(i + 1, len(data)):
            colors = ["blue"] * len(data)
            colors[min_idx] = "red"
            colors[j] = "yellow"

            draw_data(data, colors)
            time.sleep(0.05)

            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    draw_data(data, ["green"] * len(data))


# ---------------- INSERTION SORT ----------------
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

            colors = ["blue"] * len(data)
            if j >= 0:
                colors[j] = "red"

            draw_data(data, colors)
            time.sleep(0.05)

        data[j + 1] = key

    draw_data(data, ["green"] * len(data))


# ---------------- QUICK SORT ----------------
def quick_sort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quick_sort(data, low, pi - 1)
        quick_sort(data, pi + 1, high)


def partition(data, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):

        colors = ["blue"] * len(data)
        colors[j] = "yellow"
        colors[high] = "red"

        draw_data(data, colors)
        time.sleep(0.05)

        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


# ---------------- MERGE SORT ----------------
def merge_sort(data, left, right):
    if left < right:

        mid = (left + right) // 2

        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)

        merge(data, left, mid, right)


def merge(data, left, mid, right):

    left_part = data[left:mid+1]
    right_part = data[mid+1:right+1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):

        colors = ["blue"] * len(data)
        colors[k] = "yellow"

        draw_data(data, colors)
        time.sleep(0.05)

        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1

        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        k += 1


# ---------------- START SORTING ----------------
def start_sorting():

    algo = algo_menu.get()

    if algo == "Bubble Sort":
        bubble_sort(data)

    elif algo == "Selection Sort":
        selection_sort(data)

    elif algo == "Insertion Sort":
        insertion_sort(data)

    elif algo == "Quick Sort":
        quick_sort(data, 0, len(data) - 1)
        draw_data(data, ["green"] * len(data))

    elif algo == "Merge Sort":
        merge_sort(data, 0, len(data) - 1)
        draw_data(data, ["green"] * len(data))


# ---------------- UI ----------------
ui_frame = tk.Frame(root, bg="white")
ui_frame.pack(pady=20)

algo_menu = ttk.Combobox(
    ui_frame,
    values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort", "Merge Sort"],
    width=20
)
algo_menu.grid(row=0, column=0, padx=10)
algo_menu.current(0)

generate_button = tk.Button(ui_frame, text="Generate Array", command=generate_array)
generate_button.grid(row=0, column=1, padx=10)

start_button = tk.Button(ui_frame, text="Start Sorting", command=start_sorting)
start_button.grid(row=0, column=2, padx=10)

canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack()

root.mainloop()