from pyscipopt import Model
# Create a solver instance.
model = Model("Example")  # model name is optional
# Access the methods in the scip.pyx file using the solver/model instance model, e.g.:

model.readProblem("ejemplos.zpl")
#model.setObjective(x + y)
#model.addCons(2*x - y*y >= 0)
model.optimize()
sol = model.getBestSol()
print(sol)
#print("o: {}".format(sol[o]))
#print("a: {}".format(sol[a]))
#print("b: {}".format(sol[b]))
model.writeProblem()












#
#model.readProblem("ejemplo.zpl")