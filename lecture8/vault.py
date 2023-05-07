class Vault:
    def __init__(self, galleons=0, sickless=0, knuts=0):
        self.galleons = galleons
        self.sickless = sickless
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickless} Sickless, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickless = potter.sickless + weasley.sickless
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickless, knuts)
print(total)