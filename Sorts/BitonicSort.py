import time
from general import swap


def get_color(i, x, y, swapped):
    if swapped:
        if x <= i <= y:
            return 'blue'
    if i == x or i == y:
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


def bitonic_merge(data, start, end, direction, speed, canvas, root, vals):
    if end > 1:
        swapped = False
        mid = end//2
        for x in range(start, start + mid):
            if (direction == 1 and data[x] > data[x + mid]) or (direction == 0 and data[x] < data[x + mid]):
                swap(data, x, x + mid)
                swapped = True
            draw(data, x, x + mid, swapped, canvas, root, vals)
            swapped = False
            time.sleep(speed)
        bitonic_merge(data, start, mid, direction, speed, canvas, root, vals)
        bitonic_merge(data, start + mid, mid, direction, speed, canvas, root, vals)


def bitonic(data, start, end, direction, speed, canvas, root, vals):
    if end > 1:
        mid = end//2
        bitonic(data, start, mid, 0, speed, canvas, root, vals)
        bitonic(data, start+mid, mid, 1, speed, canvas, root, vals)
        bitonic_merge(data, start, end, direction, speed, canvas, root, vals)
        if end == 256:
            return data


def bitonic_sort(data, start, end, direction, speed, canvas, root, vals):
    return bitonic(data, start, end, direction, speed, canvas, root, vals)
