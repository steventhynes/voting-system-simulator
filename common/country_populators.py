from common.base_modules.politics_vector import PoliticsVector
from common.base_modules.country_populator import CountryPopulator
from common.district_populators import BasicDistrictPopulator
from common.district_updaters import BasicDistrictUpdater
from common.base_modules.district import District
from random import random

class BasicCountryPopulator(CountryPopulator):

    def populate(self, country):
        district_count = 10
        for i in range(district_count):
            baseline_dimensions = PoliticsVector(2, [random(), random()])
            district_populator = BasicDistrictPopulator()
            district_updater = BasicDistrictUpdater()
            country.districts.append(District(baseline_dimensions, district_populator, district_updater))