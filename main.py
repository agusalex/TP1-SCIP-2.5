from pyscipopt import Model
# Create a solver instance.
model = Model("Example")  # model name is optional
# Access the methods in the scip.pyx file using the solver/model instance model, e.g.:
x = model.addVar("x")
y = model.addVar("y", vtype="INTEGER")
model.setObjective(x + y)
model.addCons(2*x - y*y >= 0)
model.optimize()
sol = model.getBestSol()
print("x: {}".format(sol[x]))
print("y: {}".format(sol[y]))