from pyscipopt import Model
# Create a solver instance.
model = Model("Example")  # model name is optional
# Access the methods in the scip.pyx file using the solver/model instance model, e.g.:

a = model.addVar("a", vtype="CONTINUOUS")
b = model.addVar("b", vtype="CONTINUOUS")
c = model.addVar("c", vtype="CONTINUOUS")
o = model.addVar("o", vtype="CONTINUOUS")



#model.addCons(4>=a*2 + b + o)
#model.addCons(5>=a*3 + b + o)
#model.addCons(1<=a*3 + b - o)


#model.addCons(-a -b -c - o>= -2)
#model.addCons(-16*a -4*b -c - o>= -2)
#model.addCons(-4*a -2*b -c +o <= -2)
#model.addCons(-9*a -3*b -c +o <= -2)
model.readProblem("caso3.zpl")
#model.setObjective(o,"maximize")
model.optimize()
sol = model.getBestSol()
print("a: {}".format(sol[a]))
print("b: {}".format(sol[b]))
print("c: {}".format(sol[c]))
print("o: {}".format(sol[o]))
model.writeProblem()













#
#model.readProblem("ejemplo.zpl")