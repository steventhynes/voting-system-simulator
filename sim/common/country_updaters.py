from base_modules.country_updater import CountryUpdater

class BasicCountryUpdater(CountryUpdater):

    def update(self, country):
        country.legislature.clear()
        for dist in country.districts:
            country.legislature.extend(dist.representatives)