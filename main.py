
import random
from sys import argv
from chemistry import Chemistry

random.seed(0)

chemfile = 'data/world.chem'
if len(argv) > 2: chemfile = argv[2]

chem = Chemistry(open(chemfile).read())

quantities = [random.randint(0, 100) for i in chem.species]

for i in range(int(argv[1])):
  print quantities
  quantities = chem.react(quantities)


