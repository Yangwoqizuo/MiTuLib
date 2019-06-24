from mitulib import *

order = Mitu.make([BeginElement(BeginElement.MODE_FREE),
                   IfElement("A", "==", "1",
                             then_do=[VarAssignmentElement("A", 1)],
                             else_do=[VarAssignmentElement("B", 2)]),
                   VarAssignmentElement("C", 3)])
id_in_database = 21

sql = "update `ArchiveTable` set `ArchiveJSON` = '" + order + "' where ArchiveID = " + str(id_in_database) + ";"

print(sql)
