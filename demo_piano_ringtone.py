from mitulib import *

half_beat = 0.3
tones = [9, 11,  14, 9, 11, 14, 9, 10,
         8, 11, 15, 8, 11, 15, 8, 9,
         7, 10, 14, 7, 10, 14, 7, 10,
         8, 11, 15, 8, 11, 15, 8, 11]
toneElements = []
for tone in tones:
    toneElements.append(MidiElement(0, tone, 0))
    toneElements.append(DeltaTimeElement(half_beat))
elements = [BeginElement(BeginElement.MODE_FREE),
            LoopElement(toneElements),
            ]

order = Mitu.make(elements)
id_in_database = 28

sql = "update `ArchiveTable` set `ArchiveJSON` = '" + order + "' where ArchiveID = " + str(id_in_database) + ";"

print(sql)
