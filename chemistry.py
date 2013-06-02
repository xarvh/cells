import re


class Specie:
  "A chemical substance able to interact with other substances."

  def __init__(self, str):
    name, diffusion = str.split()
    self.name = name
    self.diffusion = int(diffusion)


class Reaction:
  ""

  def __init__(self, str, species_names):

    tokens = str.split()
    self.speed = int(tokens[0])
    self.reagents = [0] * len(species_names)
    self.products = [0] * len(species_names)
    target = self.reagents

    for t in tokens[1:]:
      if t == '->': target = self.products
      elif t == '+': continue
      else:
        cf, specie = re.match(r'(\d?)(\S+)', t).groups()         
        cf = int(cf) if cf else 1
        target[species_names.index(specie)] = cf

    if sum(self.reagents) < 1:
      raise Exception('nil ex nihilo error')

    # enforce Lavoisier's law
    if sum(self.reagents) is not sum(self.products):
      raise Exception('Lavoisier error')



class Chemistry:
  def __init__(self, bf):
    self.species = []
    self.reactions = []

    for n, l in enumerate(bf.split('\n')):
      if len(l) == 0 or l[0] == '#': continue
      try: self.species.append(Specie(l))
      except:
        try: self.reactions.append(Reaction(l, [s.name for s in self.species]))
        except Exception as e:
          raise Exception('Unable to interprete line %d: "%s" (%s)' % (n+1, l, e))

    # add ids
    for i, r in enumerate(self.reactions): r.id = i
    for i, s in enumerate(self.species): s.id = i

    ### check: all substances must appear at least once as products of a reaction
    ### and at least once as reagents


  def react(self, quantities):
    """
    Makes a batch of quantities react together, calculating new quantities.

    Reactions are limited in the amount of a specie they can consume by the
    stechiometric proportions.

    ex: if the reaction is 2A + B = 3C, but there is not enough A, not all
    available B will be consumed.

    Also, the reactions are in competition: the more a specie is consumed
    by a certain reaction, the less the specie will be available for other
    reactions.
   
 
    To calculate how to distribute a specie among all reactions, we compare
    the "demand" for that specie by a single reaction with the total demand for
    that specie.
    The demand by a specific reaction is defined as the maximum quantity that
    the reaction would consume if it was the only reaction present, times the
    reaction's speed.

    The portion of a specie consumed by a certain reaction is weighted by the
    specific demand diviided by the total demand.
    """

    reactions = self.reactions
    species = self.species

    # raw demand for each reaction
    # easier to calculate than specific demand
    # raw_demand(r) := demand(r, s) / stechiometric_reagent_cf(r, s)
    raw_demand = [ r.speed * min( q / cf for q, cf in zip(quantities, r.reagents) if cf ) for r in reactions ]


    # total demand for each specie
    total_demand = [ sum( raw_demand[r.id] * r.reagents[s.id] for r in reactions ) for s in species ]

    # available quantity divided by total demand
    weights = [ q / float(t) if t else 0 for q, t in zip(quantities, total_demand) ]
    

    # actual events per reaction
    events = [
      min( w * raw / cf for w, cf in zip(weights, r.reagents) if cf )
      for raw in raw_demand]


    # remove used reagents
    for e, r in zip(events, reactions):
      for specie, cf_in, cf_out in zip(species, r.reagents, r.products):
        quantities[specie.id] += (cf_out - cf_in) * int(e)

    # done
    return quantities

