############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller=False):
        """Initialize a melon."""

        self.pairing = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(code='musk', first_harvest='1998', color='green',
                     is_seedless=True, is_bestseller=True, name='Muskmelon')
    cas = MelonType(code='cas', first_harvest='2003', color='orange',
                    is_seedless=True, name='Casaba')
    cren = MelonType(code='cren', first_harvest='1996', color='green',
                     is_seedless=False, name='Crenshaw')
    yel_wat = MelonType(code='yw', first_harvest='2013', color='yellow',
                        is_seedless=False, is_bestseller=True, name='Yellow Watermelon')

    musk.add_pairing('mint')
    cas.add_pairing('strawberry')
    cas.add_pairing('mint')
    cren.add_pairing('proscuitto')
    yel_wat.add_pairing('ice cream')

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yel_wat)


    return all_melon_types  # this returns list of objects, is this the only way to pass these melons to the other functs?

# mel_lst = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{name} pairs with: ".format(name=melon.name)
        for pair_item in melon.pairing:
            print "- {pair}".format(pair=pair_item)

# print_pairing_info(mel_lst)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    mel_dict = {}

    for melon in melon_types:
        mel_dict[melon.code] = {}
        mel_dict[melon.code]["First Harvest"] = melon.first_harvest
        mel_dict[melon.code]['Color'] = melon.color
        mel_dict[melon.code]['Seedless'] = melon.is_seedless
        mel_dict[melon.code]['Bestseller'] = melon.is_bestseller
        mel_dict[melon.code]['Name'] = melon.name

    return mel_dict

# make_melon_type_lookup(mel_lst)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__ (self, name, code, shape_rat, color_rat, field, harvester):
        """Initialize a harvested melon"""
        self.name = name
        self.code = code
        self.shape_rat = shape_rat
        self.color_rat = color_rat
        self.field = field
        self.harvester = harvester

    def is_sellable(self, shape_rat, color_rat, field):
        """check sellability"""

        if self.shape_rat > 5 and self.color_rat > 5 and field != 3:
            return True
        else:
            return False

def make_melons():
    """Returns a list of Melon objects."""

    #melon_types
    melon_lst = []

    #hardcode
    m1 = Melon('Melon 1', 'yw', 8, 7, 2, 'Sheila')
    m2 = Melon('Melon 2', 'yw', 3, 4, 2, 'Sheila')
    m3 = Melon('Melon 3', 'yw', 9, 8, 3, 'Sheila')
    m4 = Melon('Melon 4', 'cas', 10, 6, 35, 'Sheila')
    m5 = Melon('Melon 5', 'cren', 8, 9, 35, 'Michael')
    m6 = Melon('Melon 6', 'cren', 8, 2, 35, 'Michael')
    m7 = Melon('Melon 7', 'cren', 2, 3, 4, 'Michael')
    m8 = Melon('Melon 8', 'musk', 6, 7, 4, 'Michael')
    m9 = Melon('Melon 9', 'yw', 7, 10, 3, 'Sheila')


    melon_lst.append(m1)
    melon_lst.append(m2)
    melon_lst.append(m3)
    melon_lst.append(m4)
    melon_lst.append(m5)
    melon_lst.append(m6)
    melon_lst.append(m7)
    melon_lst.append(m8)
    melon_lst.append(m9)


    return melon_lst

mel2_lst = make_melons()

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellability = melon.is_sellable(melon.shape_rat, melon.color_rat, melon.field)

        if sellability == True:
            print "Congrats! {} harvested by {} from {} is sellable!".format(melon.name, melon.harvester, melon.field)
        else:
            print "RIP, {} harvested by {} from {} is NOT sellable!".format(melon.name, melon.harvester, melon.field)

get_sellability_report(mel2_lst)