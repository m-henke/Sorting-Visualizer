# values used for drawing the window
class Values:
    WIDTH = 1000
    HEIGHT = 600

    TOP_HEIGHT = 40  # height of the top input box

    CANVAS_HEIGHT = HEIGHT - TOP_HEIGHT  # height of the canvas area
    MAX_DATA_SIZE = 500  # max number of data elements
    DEFAULT_DATA_SIZE = 100  # default number of data elements
    ADJUSTER = WIDTH // DEFAULT_DATA_SIZE  # number to adjust the width of a line


    SPEEDS = {
        'Slow': .25,
        'Medium': .025,
        'Fast': 0
    }
    ALGORITHMS = [
        'Bitonic Sort',
        'Bubble Sort',
        'Cocktail Shaker Sort',
        'Insertion Sort',
        'Merge Sort',
        'Quick Sort'
    ]


# swaps x and y position in data
def swap(data, x, y):
    temp = data[x]
    data[x] = data[y]
    data[y] = temp
