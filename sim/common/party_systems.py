from party_system import PartySystem
from politics_vector import PolicicsVector
from scipy.stats import halfnorm

class PoliticalCompassPartySystem(PartySystem):

    parties = set(["AuthLeft", "AuthRight", "LibLeft", "LibRight"])

    def get_party(self, vector):
        party_str = ""
        if vector.get(1) >= 0: #y axis is auth or lib
            party_str += "Auth"
        else:
            party_str += "Lib"
        if vector.get(0) >= 0: #x axis is left or right
            party_str += "Right"
        else:
            party_str += "Left"
        return party_str

    def generate_vector(self, party):
        xvalue = halfnorm.rvs() * (1 if "Right" in party else -1)
        yvalue = halfnorm.rvs() * (1 if "Auth" in party else -1)
        return PolicicsVector(2, [xvalue, yvalue])
        
        