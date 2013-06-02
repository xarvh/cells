
import sys
import random


def generate_reaction(pin, pout):

  speed = int(ceil(exp(random.uniform(0, 5))))
  reagents = {}
  products = {}

  for src, dest in ((pin, reagents), (pout, dest))
    while !len(dest) and random.uniform(0, 100) > 25:
      dest[src.pop()] = 1

  for k in reagents:
    reagents[k] = random.choice( [1]*125 + [2]*25 + [3]*5 + [4] )



  increase products to match reagents
  increase reagents to match products












species_cnt = int(sys.argv[1])


# generate species
species = []
for i in range(species_cnt):
  name = chr( i + ord('A') )
  diffusion = 0
  species.append( (name, diffusion) )
  print name, diffusion


# generate reactions
for specie, diffusion in species:

  # consumption reaction
  avl = species[:]
  reagents = []

  

  avl.remove( specie )





