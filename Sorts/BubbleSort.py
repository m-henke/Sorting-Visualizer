import time
from general import swap


def get_color(i, x, swapped):
    if i == x or i == x + 1:
        if swapped:
            return 'blue'
        return 'yellow'
    return 'black'


def draw(data, x, swapped, canvas, root, vals):
    canvas.delete('all')
    cur = vals.ADJUSTER // 2
    for i, length in enumerate(data):
        color = get_color(i, x, swapped)
        canvas.create_line(cur, vals.CANVAS_HEIGHT, cur, length, fill=color, width=vals.ADJUSTER)
        cur += vals.ADJUSTER
    root.update_idletasks()


def bubble_sort(data, speed, canvas, root, vals):
    going = True
    swapped = False
    length = len(data) - 1
    while going:
        going = False
        for x in range(length):
            if data[x] < data[x + 1]:
                going = True
                swapped = True
                swap(data, x, x + 1)
            draw(data, x, swapped, canvas, root, vals)
            swapped = False
            time.sleep(speed)
        length -= 1
