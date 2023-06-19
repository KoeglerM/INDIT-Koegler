#HÜ Matthias Koegler

import random

anzahl_tipps = int(input("Lottotipps eingeben: "))

lotto_tipps = []
while len(lotto_tipps) < anzahl_tipps:
    tipp = random.sample(range(1, 46), 6)
    
    if tipp not in lotto_tipps:
        lotto_tipps.append(tipp)

print(lotto_tipps)

print("Good luck")


# In[ ]: