
class PoliticsVector:

    def __init__(self, dimensions, starting_array=None):
        self.dimensions = dimensions
        self.backing_array = [0] * dimensions

        if starting_array is not None:
            if len(starting_array) > dimensions:
                raise Exception("Starting array is longer than given vector dimension")
            else:
                for index in range(dimensions):
                    self.backing_array[index] = starting_array[index]

    def get(self, index):
        if index >= self.dimensions:
            print("Value at index requested for index outside vector. Returning 0.")
            return 0.0
        return self.backing_array[index]

    def put(self, index, value):
        self.backing_array[index] = value