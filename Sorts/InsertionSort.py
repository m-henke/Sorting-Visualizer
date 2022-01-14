import time


def get_color(i, x, y, inserted):
    if i == x or i == y:
        if inserted:
            return 'blue'
        if i == x:
            return 'red'
        return 'yellow'
    return 'black'


def draw(data, x, y, inserted, canvas, root, vals):
    canvas.delete('all')
    cur = vals.ADJUSTER // 2
    for i, length in enumerate(data):
        color = get_color(i, x, y, inserted)
        canvas.create_line(cur, vals.CANVAS_HEIGHT, cur, length, fill=color, width=vals.ADJUSTER)
        cur += vals.ADJUSTER
    root.update_idletasks()


def ins(data, x, y):
    temp = data[x]
    insert_at = y
    data[insert_at:insert_at] = [temp]
    del data[x + 1]


def insertion_sort(data, speed, canvas, root, vals):
    inserted = False
    for x in range(len(data)):
        if x == 0:
            continue
        for y in range(x-1, -1, -1):
            if data[x] > data[y]:
                if data[x] > data[y - 1] and y - 1 >= 0:
                    pass
                else:
                    inserted = True
                    ins(data, x, y)
            draw(data, x, y, inserted, canvas, root, vals)
            time.sleep(speed)
            if inserted:
                inserted = False
                break
            inserted = False

    print()
