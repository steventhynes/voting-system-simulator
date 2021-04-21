
class District:

    def __init__(self, baseline_dimensions, district_populator, district_updater, other_data={}):
        self.baseline_dimensions = baseline_dimensions
        self.district_populator = district_populator
        self.district_updater = district_updater
        self.other_data = other_data

        self.candidates = []
        self.representatives = []
        self.voters = []

        self.district_populator.populate(self)