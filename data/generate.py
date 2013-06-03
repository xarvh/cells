
import sys
import math
import random


def generate_reaction(pin, pout):

  speed = int(math.ceil(math.exp(random.uniform(0, 5))))
  reagents = {}
  products = {}

  # select reagents and product species
  for src, dest in ((pin, reagents), (pout, products)):
    while len(src) and (len(dest) < 1 or random.uniform(0, 100) < 40):
      dest[src.pop()] = 1

  # select stechiometric coefficients for products
  for k in reagents:
    reagents[k] = random.choice( [1]*64 + [2]*16 + [3]*4 + [4] )

  # increase products to match reagents
  while sum(products.values()) < sum(reagents.values()):
    products[random.choice(products.keys())] += 1

  # increase reagents to match products
  while sum(reagents.values()) < sum(products.values()):
    reagents[random.choice(reagents.keys())] += 1

  # create string
  r, p = [[ "%d%s" % (v, k) for k, v in d.items()] for d in (reagents, products) ]
  return "%3d  %s -> %s" % (speed, ' + '.join(r), ' + '.join(p))



def generate_chemistry(species_cnt):

  o = []

  # generate species
  species = []
  for i in range(species_cnt):
    name = chr( i + ord('A') )
    diffusion = 0
    species.append(name)
    o.append("%s  %d" % (name, diffusion))

  # helper to generate shuffled species lists
  shsp = lambda: sorted(species, key=lambda x: random.random())

  # generate reactions
  for specie in species:

    # consumption reaction
    o.append(generate_reaction(shsp() + [specie], shsp()))

    # generation function
    o.append(generate_reaction(shsp(), shsp() + [specie]))

  #### generate more reactions?

  # done
  return '\n'.join(o)



#
if __name__ == '__main__':
  print generate_chemistry(int(sys.argv[1]))

