
import random
from sys import argv
from chemistry import Chemistry

#random.seed(0)

chemfile = 'data/world.chem'
if len(argv) > 2: chemfile = argv[2]

chem = Chemistry(open(chemfile).read())

quantities = [random.randint(0, 100) for i in chem.species]
total_matter = sum(quantities)

# iteration
previous_quantities = [1]
iterations = 0
print quantities
while quantities != previous_quantities and iterations < 1000:
  previous_quantities = quantities
  quantities = chem.react(list(previous_quantities))
  iterations += 1
  print quantities

print 'starting matter:', total_matter
print 'end matter:', sum(quantities)
print 'iterations:', iterations

