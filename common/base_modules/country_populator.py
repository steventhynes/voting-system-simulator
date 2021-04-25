
class CountryPopulator:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def populate(self, country):
        raise NotImplementedError