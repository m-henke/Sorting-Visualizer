class Values:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 600

        self.TOP_HEIGHT = 40  # height of the top input box

        self.CANVAS_HEIGHT = self.HEIGHT - self.TOP_HEIGHT  # height of the canvas area
        self.MAX_DATA_SIZE = 500  # max number of data elements
        self.DEFAULT_DATA_SIZE = 100  # default number of data elements
        self.ADJUSTER = self.WIDTH//self.DEFAULT_DATA_SIZE  # number to adjust the width of a line

        self.SPEEDS = ['Slow', 'Medium', 'Fast']
        self.ALGORITHMS = [
            'Bitonic Sort',
            'Bubble Sort',
            'Cocktail Shaker Sort',
            'Insertion Sort',
            'Merge Sort',
            'Quick Sort'
        ]


def swap(data, x, y):
    temp = data[x]
    data[x] = data[y]
    data[y] = temp
