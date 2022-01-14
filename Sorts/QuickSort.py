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


def partition(data, start, end, speed, canvas, root, vals):
    pi = start
    p = data[pi]
    swapped = False

    while start < end:
        while start < len(data) and p <= data[start]:
            start += 1
            draw(data, start, -9999, swapped, canvas, root, vals)
            time.sleep(speed)
        while data[end] > p:
            end -= 1
            draw(data, start, end, swapped, canvas, root, vals)
            time.sleep(speed)
        if start < end:
            swapped = True
            swap(data, start, end)
        draw(data, start, end, swapped, canvas, root, vals)
        swapped = False
        time.sleep(speed)
    swap(data, pi, end)
    draw(data, start, end, swapped, canvas, root, vals)
    return end


def quick(data, start, end, speed, canvas, root, vals):
    if start < end:
        pivot = partition(data, start, end, speed, canvas, root, vals)

        quick(data, start, pivot - 1, speed, canvas, root, vals)
        quick(data, pivot + 1, end, speed, canvas, root, vals)


def quick_sort(data, speed, canvas, root, vals):
    quick(data, 0, len(data) - 1, speed, canvas, root, vals)
