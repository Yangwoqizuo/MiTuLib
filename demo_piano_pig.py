from mitulib import *

quarter_beat = 0.2
toneElements = [
    # 第一行
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat * 4),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 4),

    # 第二行
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),

    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 5, 0),
    DeltaTimeElement(quarter_beat * 2),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 4),
    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 2),

    # 第三行
    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 4),
    MidiElement(0, 16, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 4),
    MidiElement(0, 16, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 16, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 16, 0),
    DeltaTimeElement(quarter_beat * 2),

    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 4),
    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 4),

    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 7, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 8, 0),
    DeltaTimeElement(quarter_beat),
    MidiElement(0, 9, 0),
    DeltaTimeElement(quarter_beat * 2),
    MidiElement(0, 11, 0),
    DeltaTimeElement(quarter_beat * 2),

    MidiElement(0, 12, 0),
    DeltaTimeElement(quarter_beat * 8),

]
elements = [BeginElement(BeginElement.MODE_FREE),
            LoopElement(toneElements),
            ]

order = Mitu.make(elements)
id_in_database = 30

sql = "update `ArchiveTable` set `ArchiveJSON` = '" + order + "' where ArchiveID = " + str(id_in_database) + ";"

print(sql)
