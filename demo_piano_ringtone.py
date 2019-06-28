from MiTulib import *

half_beat = 0.2
tones = [9, 11, 14, 9, 11, 14, 9, 10,
         8, 11, 15, 8, 11, 15, 8, 9,
         7, 10, 14, 7, 10, 14, 7, 10,
         8, 11, 15, 8, 11, 15, 8, 11]
toneElements = []
for index in range(len(tones)):
    if index < 8:
        toneElements.append(MidiElement(6, tones[index], 0))
    elif index < 16:
        toneElements.append(MidiElement(6, tones[index], 0))
    elif index < 24:
        toneElements.append(MidiElement(6, tones[index], 0))
    else:
        toneElements.append(MidiElement(6, tones[index], 0))
    toneElements.append(DeltaTimeElement(half_beat))
elements = [BeginElement(BeginElement.MODE_FREE),
            LoopElement(toneElements),
            ]

order = MiTu.make(elements)
id_in_database = 32

sql = "update `ArchiveTable` set `ArchiveJSON` = '" + order + "' where ArchiveID = " + str(id_in_database) + ";"

print(sql)
