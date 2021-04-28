from common.base_modules.country import Country
from common.country_populators import BasicCountryPopulator
from common.country_updaters import BasicCountryUpdater
from common.voting_systems import FirstPastThePostVotingSystem, RankedChoiceVotingSystem, SingleTransferableVoteVotingSystem
from common.party_systems import PoliticalCompassPartySystem
from pprint import pprint
import random
import pandas as pd
import matplotlib.pyplot as plt

#Create a DataFrame
data = pd.DataFrame()

num_runs = 50

for i in range(num_runs):
    print("Run " + str(i + 1))

    #Run the sim several times for FPTP and append the average district representation
    random.seed(0)
    rep_over_time_1 = []
    country = Country(BasicCountryPopulator(), BasicCountryUpdater(), FirstPastThePostVotingSystem(), PoliticalCompassPartySystem())
    for i in range(20):
        country.run_election()
        rep_over_time_1.append(sum(country.get_district_representation()) / len(country.get_district_representation()))
    if "FPTP Representation Score" in data:
        data["FPTP Representation Score"] += rep_over_time_1
    else:
        data["FPTP Representation Score"] = rep_over_time_1

    #Run the sim several times for Ranked Choice and append the average district representation
    random.seed(0)
    rep_over_time_2 = []
    country = Country(BasicCountryPopulator(), BasicCountryUpdater(), RankedChoiceVotingSystem(), PoliticalCompassPartySystem())
    for i in range(20):
        country.run_election()
        rep_over_time_2.append(sum(country.get_district_representation()) / len(country.get_district_representation()))
    if "Ranked Choice Representation Score" in data:
        data["Ranked Choice Representation Score"] += rep_over_time_2
    else:
        data["Ranked Choice Representation Score"] = rep_over_time_2

    #Run the sim several times for Single Transferable Vote and append the average district representation
    random.seed(0)
    rep_over_time_3 = []
    country = Country(BasicCountryPopulator(), BasicCountryUpdater(), SingleTransferableVoteVotingSystem(), PoliticalCompassPartySystem())
    for i in range(20):
        country.run_election()
        rep_over_time_3.append(sum(country.get_district_representation()) / len(country.get_district_representation()))
    if "STV Representation Score" in data:
        data["STV Representation Score"] += rep_over_time_3
    else:
        data["STV Representation Score"] = rep_over_time_3

    print(data)

data /= num_runs #instead of using the sum, we will use the average
data.plot(title="Representation Scores Over Time", ylim=(0,0.7))
plt.show()