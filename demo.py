from MiTulib import *

order = MiTu.make([BeginElement(BeginElement.MODE_FREE),
                   MidiElement(0, 0, "A")])
id_in_database = 21

sql = "update `ArchiveTable` set `ArchiveJSON` = '" + order + "' where ArchiveID = " + str(id_in_database) + ";"

print(order)
