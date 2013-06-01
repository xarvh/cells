
class Species:
  def __init__(self):
    self.id = ''
    self.diffusion = 100


class Reaction:
  def __init__(self, reagents, products, speed):

    if len(reagents) < 1:
      raise Error('nil ex nihilo!')

    if len(reagents) != len(products):
      raise Error('species number error')

    # enforce Lavoisier's law
    if sum(reagents) is not sum(products):
      raise Error('Lavoisier error')

    # stechiometric coefficiens
    self.reagents = reagents
    self.products = products
    self.speed = speed


class Chemistry:
  def __init__(self):
    self.species = []
    self.reactions = []


  def react(quantities):
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
    normalization_cf = [ q / t if t else 0 for q, t in zip(quantities, total_demand) ]
    

    # actual events per reaction
    events = [
      min( N * raw / cf for N, cf in zip(normalization_cf, r.reagents) if cf )
      for raw in raw_demand]


    # remove used reagents
    for e, r in zip(events, reactions):
      for cf_in, cf_out in zip(r.reagents, r.products):
        quantities += (cf_out - cf_in) * e

    # done
    return quantities

