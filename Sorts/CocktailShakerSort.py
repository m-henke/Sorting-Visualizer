import time
from general import swap


def get_color(i, x, y, swapped):
    if i == x or i == y:
        if swapped:
            return 'blue'
        return 'yellow'
    return 'black'


def draw(data, x, y, swapped, canvas, root, vals):
    canvas.delete('all')
    cur = vals.ADJUSTER // 2
    for i, length in enumerate(data):
        color = get_color(i, x, y, swapped)
        canvas.create_line(cur, vals.CANVAS_HEIGHT, cur, length, fill=color, width=vals.ADJUSTER)
        cur += vals.ADJUSTER
    root.update_idletasks()


def cocktail_sort(data, speed, canvas, root, vals):
    going = True
    swapped = False
    leng = len(data) - 1
    x_offset = 0
    while going:
        going = False
        for x in range(leng - x_offset):
            x += x_offset
            if data[x] < data[x + 1]:
                swap(data, x, x + 1)
                swapped = True
                going = True
            draw(data, x, x + 1, swapped, canvas, root, vals)
            swapped = False
            time.sleep(speed)
        leng -= 1
        swapped = False
        for x in range(leng, x_offset, -1):
            if data[x] > data[x - 1]:
                swap(data, x, x - 1)
                swapped = True
                going = True
            draw(data, x, x - 1, swapped, canvas, root, vals)
            swapped = False
            time.sleep(speed)
        x_offset += 1
