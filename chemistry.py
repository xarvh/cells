import re


class Specie:
  "A chemical substance able to interact with other substances."

  def __init__(self, str):
    name, diffusion = str.split()
    self.name = name
    self.color = None

    # diffusion is the proportion of specie that is diffused away at each iteration
    self.diffusion = float(diffusion)


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



  def diffuse(self, quantities, points = 4)
    diffused = [None] * len(quantities)

    for i, s in enumerate(self.species):
      diffused[i] = int(quantities[i] * s.diffusion / points)
      quantities[i] -= diffused[i] * points

    return diffused
    



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
    """

    reactions = self.reactions
    species = self.species

    for s in species:
      s.cfs = [ r.reagents[s.id] for r in reactions ]

    # reactions speed
    S = [ r.speed for r in reactions ]

    # max events per reaction
    #
    # Mr(Q) = min[s] Qs / Crs
    #
    M = [ min(Qs / Crs for Qs, Crs in zip(quantities, r.reagents) if Crs) for r in reactions]

    # reaction power
    #
    # Pr = Sr Mr
    #
    P = [ Sr * Mr for Sr, Mr in zip(S, M)]

    # demand for a specie
    #
    # Ds = sum[r] Pr Crs
    #
    D = [ sum(Pr * Crs for Pr, Crs in zip(P, s.cfs)) for s in species]

    # actual events per reaction
    #
    # Er = Pr min[s] Qs / Ds [if Crs]
    #
    E = [int(Pr * min( Qs / float(Ds) if Ds else 0 for Qs, Ds, Crs in zip(quantities, D, r.reagents) if Crs)) for Pr, r in zip(P, reactions)]

    # remove used reagents
    for e, r in zip(E, reactions):
      for specie, cf_in, cf_out in zip(species, r.reagents, r.products):
        quantities[specie.id] += (cf_out - cf_in) * int(e)

    # done
    return quantities

