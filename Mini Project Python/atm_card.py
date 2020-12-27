class ATMCard:
    def __init__(self, defaultPin, defafultBalance):
        self.defaultPin = defaultPin
        self.defafultBalance = defafultBalance
    def cekPinAwal(self):
        return self.defaultPin
    def cekSaldoAwal(self):
        return self.defafultBalance