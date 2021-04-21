
class DistrictUpdater:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def update(self, district):
        raise NotImplementedError