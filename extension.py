import os
from shutil import copyfile
from pyscipopt import Model

model = Model("Extension")  # model name is optional
a = model.addVar("a", vtype="CONTINUOUS")
b = model.addVar("b", vtype="CONTINUOUS")
c = model.addVar("c", vtype="CONTINUOUS")
o = model.addVar("o", vtype="CONTINUOUS")
tests = ["extension_test1"]

for test in tests:
    #me traigo el caso de test y le pongo de nombre input_B e input_N
    copyfile(os.path.join("tests","extension",test+"_B.txt"), "input_B.txt")
    copyfile(os.path.join("tests","extension",test+"_N.txt"), "input_N.txt")
    #Cargo en SCIP el problema en formato ZIMPL
    model.readProblem("caso3.zpl")
    model.optimize()
    sol = model.getBestSol()
    #Busco solucion e imprimo puntos
    blanco = open('input_B.txt', 'r').read()
    negro = open('input_N.txt', 'r').read()
    print("\n\n###############################################")
    print("Test "+test+":\n")
    print("Blanco: \n"+blanco)
    print("Negro: \n"+negro+"\n")
    print("Solucion:")
    print("a: {}".format(sol[a]))
    print("b: {}".format(sol[b]))
    print("c: {}".format(sol[c]))
    print("o: {}".format(sol[o]))
    print("###############################################")
os.remove("input_B.txt")
os.remove("input_N.txt")