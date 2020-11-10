import os
from shutil import copyfile
from pyscipopt import Model

model = Model("Caso2")  # model name is optional
a = model.addVar("a", vtype="CONTINUOUS")
b = model.addVar("b", vtype="CONTINUOUS")
o = model.addVar("o", vtype="CONTINUOUS")
tests = ["caso2_test1","caso2_test2"]

for test in tests:
    #me traigo el caso de test y le pongo de nombre input_B e input_N
    copyfile(os.path.join("tests","caso2",test+"_B.txt"), "input_B.txt") 
    copyfile(os.path.join("tests","caso2",test+"_N.txt"), "input_N.txt")
    #Cargo en SCIP el problema en formato ZIMPL
    model.readProblem("caso2.zpl")
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
    print("o: {}".format(sol[o]))
    print("###############################################")
os.remove("input_B.txt")
os.remove("input_N.txt")








#model.setObjective(o,"maximize")

#model.addCons(4>=a*2 + b + o)
#model.addCons(5>=a*3 + b + o)
#model.addCons(1<=a*3 + b - o)


#model.addCons(-a -b -c - o>= -2)
#model.addCons(-16*a -4*b -c - o>= -2)
#model.addCons(-4*a -2*b -c +o <= -2)
#model.addCons(-9*a -3*b -c +o <= -2)

#
#model.readProblem("ejemplo.zpl")