

from mspresidio import anonymize
from ner import get_ner_dict

text = []

text = ["""Konstantin Päts sündis meetrika andmeil 10. (uue kalendri järgi 22.) veebruaril 1874 Pärnumaal Tahkuranna vallas maaomanik Jakob Pätsi (1848–1909) teise lapsena Pätsi (Põldeotsa) talus Tahku külas Tahkuranna mõisas. Alates 1897. aastast on Pätsi sünnikuupäevana kasutusel 11. veebruar vana kalendri (23. veebruar uue kalendri) järgi ja see kuupäev on avaldatud kõigis teatmeteostes. Ühepäevase erinevuse põhjus pole teada. Tal oli neli venda ja üks õde: Nikolai Päts, Paul Päts (1876–1881), Voldemar Päts, Peeter Päts, Marianna Pung (1882–1947).

Tema ema oli Olga Tumanova, kes sündis Viljandis ja kasvas üles Valga linnapea Razumovski perekonnas.[viide?] Väidetud on ka, et Tumanova kasvatati üles parun Krüdeneri peres[1], kuid tegemist on eksitusega, sest Olga oli paruni peres guvernant. Olga isa oli Hariton Tumanov, kelle päritolu on selgusetu. Tumanov oli haruldane perekonnanimi, mida kasutasid eeskätt Kaukaasiast pärit inimesed, kes venestasid oma nime, näiteks Tumanishvili või Tumanjan.

Konstantin Päts oli õigeusklik, kuulus Tahkuranna kogudusse.

Tema haridustee algas Tahkuranna apostliku õigeusu kihelkonnakoolis, jätkudes seejärel Raeküla Nikolai koolis ja Riia Vaimulikus Seminaris.[2] Seminari jättis Päts pooleli ning jätkas õpinguid Pärnu Meesgümnaasiumis. 1894–1898 õppis ta Tartu ülikooli õigusteaduskonnas, mille lõpetas cand. jur. kraadi (hiljem nimetati 1. järgu diplomiga) ja kubermangusekretäri auastmega, Rooma õiguse teemal. Sellele järgnes aastane teenistus Pihkvas 96. Omski jalaväepolgus, lõpetades Peterburis lipnike kursused, milline auaste andis õiguse isiklikule, mittepärandatavale aadliseisusele.

1900. aastal asus Päts tööle Tallinnas advokaat Jaan Poska abina. 1901–1905 andis Päts välja ja toimetas ajalehte Teataja. 1901. aastal osales ta Jalgrattasõitjate Seltsi Kalev asutamises ja temast sai seltsi aseesimees. 1904. aasta Tallinna linnavolikogu valimisteks organiseeris ta eesti-vene valimisliidu, mis võitis valimistel baltisakslaste ees. Päts valiti 8. veebruaril 1905 Tallinna linnanõunikuks ja 19. aprillil sai Pätsist Tallinna linnapea abi, sama aasta 2. detsembrist ka linnapea kohusetäitja. Saamaks hääleõigust Vene riigivolikogu valimistel, ostis ta Mäe talu Kodilas Rapla vallas ja valiti Harjumaa valijameheks."""]



ner_dicts = [get_ner_dict(t) for t in text]

def printable_ners(ner_dict,text):
    line = ""
    for k in ner_dict.keys():
        line += text[k[0]:k[1]] + " : " + ner_dict[k] + " | "
    line += "\n"
    return line

printed_ners = [printable_ners(nd,t) for nd,t in zip(ner_dicts,text)]


with open("ner.txt",'w') as f:
    f.writelines(printed_ners)