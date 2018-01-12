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


mel_lst = make_melon_types()
def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{name} pairs with: ".format(name=melon.name)
        for pair_item in melon.pairing:
            print "- {pair}".format(pair=pair_item)


print_pairing_info(mel_lst)
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

make_melon_type_lookup(mel_lst)
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



