import crudtxt
from crudcsv import addRow,crearCsv

crudtxt.crearArchivo("pacso.txt")



crearCsv("cosa.csv", ["user","tipo de usuario"])



addRow("cosa.csv", ["hugo","admin"])
addRow("cosa.csv", ["andrés david","tl"])
addRow("cosa.csv", ["paco","invitado"])