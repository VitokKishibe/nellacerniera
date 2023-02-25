class Human:
    intellect = 95
    gladness = 75
    deference = 50
    riches = 40
    secretiveness = 15

class Boss(Human):
    intellect = 145
    deference = 230
    riches = 1000
    secretiveness = 200

class Underboss(Boss):
    deference = 170
    riches = 750
    secretiveness = 120

class Drug_gang_leader(Boss):
    gladness = 85
    intellect = 130
    deference = 60
    riches = 650
    secretiveness = 50

class Caporegime(Underboss):
    gladness = 90
    intellect = 120
    deference = 145
    riches = 550
    secretiveness = 70

class Liquidator_gang_leader(Caporegime):
    gladness = 40
    deference = 60
    riches = 100

class Other_gang_leader(Caporegime):
    intellect = 140
    deference = 100
    riches = 200

class Gang_members(Other_gang_leader):
    intellect = 115
    deference = 90
    riches = 130
    secretiveness = 45

class Traitor(Human):
    intellect = 140
    gladness = 30
    deference = 0
    secretiveness = 150

diavolo_vinnegar = Boss()
vinnegar_doppio = Underboss()
massimo_volpe = Drug_gang_leader()
perikollo = Caporegime()
risotto_nerro = Liquidator_gang_leader()
bruno_bucciarati = Other_gang_leader()
narancia_ghirga = Gang_members()
cannolo_murolo = Traitor()

print("----------~Intellect~----------")
print("Diavolo's intellect:", diavolo_vinnegar.intellect)
print("- - - - - - - - - - - - - - - ")
print("Doppio's intellect:", vinnegar_doppio.intellect)
print("- - - - - - - - - - - - - - - ")
print("Massimo's intellect:", massimo_volpe.intellect)
print("- - - - - - - - - - - - - - - ")
print("Perikollo's intellect:", perikollo.intellect)
print("- - - - - - - - - - - - - - - ")
print("Risotto's intellect:", risotto_nerro.intellect)
print("- - - - - - - - - - - - - - - ")
print("Bucciarati's intellect:", bruno_bucciarati.intellect)
print("- - - - - - - - - - - - - - - ")
print("Narancia's intellect:", narancia_ghirga.intellect)
print("- - - - - - - - - - - - - - - ")
print("Murolo's intellect:", cannolo_murolo.intellect)
print("- - - - - - - - - - - - - - - ")

print("----------~Gladness~----------")
print("Diavolo's gladness:", diavolo_vinnegar.gladness)
print("- - - - - - - - - - - - - - - ")
print("Doppio's gladness:", vinnegar_doppio.gladness)
print("- - - - - - - - - - - - - - - ")
print("Massimo's gladness:", massimo_volpe.gladness)
print("- - - - - - - - - - - - - - - ")
print("Perikollo's gladness:", perikollo.gladness)
print("- - - - - - - - - - - - - - - ")
print("Risotto's gladness:", risotto_nerro.gladness)
print("- - - - - - - - - - - - - - - ")
print("Bucciarati's gladness:", bruno_bucciarati.gladness)
print("- - - - - - - - - - - - - - - ")
print("Narancia's gladness:", narancia_ghirga.gladness)
print("- - - - - - - - - - - - - - - ")
print("Murolo's gladness:", cannolo_murolo.gladness)
print("- - - - - - - - - - - - - - - ")

print("----------~Deference~----------")
print("Diavolo's deference:", diavolo_vinnegar.deference)
print("- - - - - - - - - - - - - - - ")
print("Doppio's deference:", vinnegar_doppio.deference)
print("- - - - - - - - - - - - - - - ")
print("Massimo's deference:", massimo_volpe.deference)
print("- - - - - - - - - - - - - - - ")
print("Perikollo's deference:", perikollo.deference)
print("- - - - - - - - - - - - - - - ")
print("Risotto's deference:", risotto_nerro.deference)
print("- - - - - - - - - - - - - - - ")
print("Bucciarati's deference:", bruno_bucciarati.deference)
print("- - - - - - - - - - - - - - - ")
print("Narancia's deference:", narancia_ghirga.deference)
print("- - - - - - - - - - - - - - - ")
print("Murolo's deference:", cannolo_murolo.deference)
print("- - - - - - - - - - - - - - - ")

print("----------~Riches~----------")
print("Diavolo's riches:", diavolo_vinnegar.riches)
print("- - - - - - - - - - - - - - - ")
print("Doppio's riches:", vinnegar_doppio.riches)
print("- - - - - - - - - - - - - - - ")
print("Massimo's riches:", massimo_volpe.riches)
print("- - - - - - - - - - - - - - - ")
print("Perikollo's riches:", perikollo.riches)
print("- - - - - - - - - - - - - - - ")
print("Risotto's riches:", risotto_nerro.riches)
print("- - - - - - - - - - - - - - - ")
print("Bucciarati's riches:", bruno_bucciarati.riches)
print("- - - - - - - - - - - - - - - ")
print("Narancia's riches:", narancia_ghirga.riches)
print("- - - - - - - - - - - - - - - ")
print("Murolo's riches:", cannolo_murolo.riches)
print("- - - - - - - - - - - - - - - ")

print("----------~Secretiveness~----------")
print("Diavolo's secretiveness:", diavolo_vinnegar.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Doppio's secretiveness:", vinnegar_doppio.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Massimo's secretiveness:", massimo_volpe.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Perikollo's secretiveness:", perikollo.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Risotto's secretiveness:", risotto_nerro.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Bucciarati's secretiveness:", bruno_bucciarati.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Narancia's secretiveness:", narancia_ghirga.secretiveness)
print("- - - - - - - - - - - - - - - ")
print("Murolo's secretiveness:", cannolo_murolo.secretiveness)
print("- - - - - - - - - - - - - - - ")
