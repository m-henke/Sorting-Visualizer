import time


def get_color(i, start, stop):
    if start < i < stop:
        return 'blue'
    if i == start or i == stop:
        return 'yellow'
    return 'black'


def draw(data, start, stop, canvas, root, vals):
    canvas.delete('all')
    cur = vals.ADJUSTER // 2
    for i, length in enumerate(data):
        color = get_color(i, start, stop)
        canvas.create_line(cur, vals.CANVAS_HEIGHT, cur, length, fill=color, width=vals.ADJUSTER)
        cur += vals.ADJUSTER
    root.update_idletasks()


def merge_sort(data, start, end, speed, canvas, root, vals):
    merge(data, start, end, speed, canvas, root, vals)


def merge(data, start, end, speed, canvas, root, vals):
    if start < end:
        middle = (start + end)//2

        merge_sort(data, start, middle, speed, canvas, root, vals)
        merge_sort(data, middle + 1, end, speed, canvas, root, vals)

        s = start
        m = middle + 1
        temp = []

        for x in range(start, end + 1):
            if s > middle:
                temp.append(data[m])
                m += 1
            elif m > end:
                temp.append(data[s])
                s += 1
            elif data[s] > data[m]:
                temp.append(data[s])
                s += 1
            else:
                temp.append(data[m])
                m += 1
        s = start
        for num in temp:
            data[s] = num
            s += 1
        draw(data, start, end + 1, canvas, root, vals)
        time.sleep(speed)
