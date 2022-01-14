import tkinter as tk
import random
import time
from general import Values
from Sorts.BubbleSort import bubble_sort
from Sorts.MergeSort import merge_sort
from Sorts.BitonicSort import bitonic_sort
from Sorts.CocktailShakerSort import cocktail_sort
from Sorts.InsertionSort import insertion_sort
from Sorts.QuickSort import quick_sort


v = Values()


def is_sorted(data):
    for x in range(len(data) - 1):
        if data[x] < data[x + 1]:
            return False
    return True


def animate_completed(data):
    x = 0
    while x < len(data):
        canvas.delete('all')
        cur = v.ADJUSTER // 2
        for i, length in enumerate(data):
            color = 'green' if i <= x else 'black'
            canvas.create_line(cur, v.CANVAS_HEIGHT, cur, length, fill=color, width=v.ADJUSTER)
            cur += v.ADJUSTER
        x += 1
        root.update_idletasks()


def draw(data):
    canvas.delete('all')
    cur = v.ADJUSTER // 2
    for i, length in enumerate(data):
        canvas.create_line(cur, v.CANVAS_HEIGHT, cur, length, fill='black', width=v.ADJUSTER)
        cur += v.ADJUSTER
    if is_sorted(data):
        animate_completed(data)


def get_speed(speed):
    if speed == 'Slow':
        return .25
    if speed == 'Medium':
        return .025
    return 0


def run():
    global data
    if alg_choice.get() in v.ALGORITHMS and speed_choice.get() in v.SPEEDS:
        speed = get_speed(speed_choice.get())
        if alg_choice.get() == 'Bubble Sort':
            start = time.time()
            bubble_sort(data, speed, canvas, root, v)
            end = time.time()
        elif alg_choice.get() == 'Merge Sort':
            start = time.time()
            merge_sort(data, 0, len(data) - 1, speed, canvas, root, v)
            end = time.time()
        elif alg_choice.get() == 'Bitonic Sort':
            slider.set(256)
            update_slider(label_size, label_runtime)
            # the above two extra lines are because bitonic sort only works on powers of 2
            start = time.time()
            data = bitonic_sort(data, 0, len(data), 0, speed, canvas, root, v)
            end = time.time()
        elif alg_choice.get() == 'Cocktail Shaker Sort':
            start = time.time()
            cocktail_sort(data, speed, canvas, root, v)
            end = time.time()
        elif alg_choice.get() == 'Insertion Sort':
            start = time.time()
            insertion_sort(data, speed, canvas, root, v)
            end = time.time()
        elif alg_choice.get() == 'Quick Sort':
            start = time.time()
            quick_sort()
            end = time.time()
        time_taken = end - start
        label_runtime['text'] = 'RunTime:', str(round(time_taken, 2)), 'seconds'
        draw(data)


def reset():
    global data
    slider.set(v.DEFAULT_DATA_SIZE)
    data = [random.randint(1, v.CANVAS_HEIGHT) for x in range(slider.get())]
    v.ADJUSTER = v.WIDTH // slider.get()
    draw(data)


def update_slider(ls, lt):
    ls['text'] = 'Data Size: ' + str(slider.get())
    lt['text'] = 'RunTime: N/A'
    global data
    data = [random.randint(1, v.CANVAS_HEIGHT) for x in range(slider.get())]
    v.ADJUSTER = v.WIDTH // slider.get() if v.WIDTH % slider.get() == 0 else (v.WIDTH // slider.get()) + 1
    draw(data)


if __name__ == '__main__':
    root = tk.Tk()
    data = [random.randint(1, v.CANVAS_HEIGHT) for x in range(v.DEFAULT_DATA_SIZE)]

    master = root
    root.title('Sorting Algorithm Visualizer')

    f = tk.Frame(root, width=v.WIDTH, height=v.HEIGHT, bg='grey')
    f.pack()

    top_f = tk.Frame(f, width=v.WIDTH, height=v.TOP_HEIGHT, bg='grey')
    top_f.pack()
    top_f.pack_propagate(0)

    alg_choice = tk.StringVar(top_f)
    alg_choice.set('Pick Algorithm to Visualize')
    alg_menu = tk.OptionMenu(top_f, alg_choice, *v.ALGORITHMS)
    alg_menu.pack(side=tk.LEFT, padx=10)

    speed_choice = tk.StringVar(top_f)
    speed_choice.set('Pick Speed to Visualize')
    speed_menu = tk.OptionMenu(top_f, speed_choice, *v.SPEEDS)
    speed_menu.pack(side=tk.LEFT)

    submit_button = tk.Button(top_f, text='Start', command=lambda: run())

    reset_button = tk.Button(top_f, text='Reset', command=lambda: reset())

    label_size = tk.Label(top_f, text='Data Size: ' + str(v.DEFAULT_DATA_SIZE), bg='grey')

    label_runtime = tk.Label(top_f, text='RunTime: N/A', bg='grey')

    slider = tk.Scale(top_f, from_=10, to=v.MAX_DATA_SIZE, orient=tk.HORIZONTAL, length=200,
                      command=lambda l: update_slider(label_size, label_runtime), showvalue=False, resolution=2)
    slider.set(100)

    slider.pack(side=tk.LEFT, padx=10)
    label_size.pack(side=tk.LEFT)
    submit_button.pack(side=tk.LEFT, padx=10)
    reset_button.pack(side=tk.LEFT)
    label_runtime.pack(side=tk.LEFT, padx=10)

    canvas = tk.Canvas(f, width=v.WIDTH, height=v.CANVAS_HEIGHT, bg='white')
    canvas.pack()
    draw(data)

    root.mainloop()
