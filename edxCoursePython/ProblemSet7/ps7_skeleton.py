import math
import random


class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """

    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        float1, float2 = location
        self.location = (float(float1), float(float2))

    def get_number_of_species(self, animal):
        if not animal in self.species_types:
            return 0
        else:
            return self.species_types[animal]

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species_name):
        if not species_name in self.species_types:
            pass
        elif self.species_types[species_name] == 1:
            del self.species_types[species_name]
        else:
            self.species_types[species_name] -= 1


# a = AdoptionCenter("asdasda",{},(1,1))
# print a.get_location()

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """

    def __init__(self, name, desired_species):
        self.desired_species = desired_species
        self.name = name

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """

    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        count = 0.0
        for animal_considered in self.considered_species:
            count += 0.3 * adoption_center.get_number_of_species(animal_considered)
        return float(Adopter.get_score(self, adoption_center) + count)


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """

    def __init__(self, name, desired_species, feared_species=""):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        score = float(
            Adopter.get_score(self, adoption_center) - adoption_center.get_number_of_species(self.feared_species) * 0.3)
        return 0.0 if score < 0 else score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """

    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for alergic_animal in self.allergic_species:
            if adoption_center.get_number_of_species(alergic_animal) > 0:
                return 0.0
        return float(Adopter.get_score(self, adoption_center))


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """

    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        lowest_alergy_effectivness = 1.0
        for alergic_animal in self.allergic_species:
            if adoption_center.get_number_of_species(alergic_animal) > 0:
                effectivness = self.medicine_effectiveness[alergic_animal]
                if effectivness < lowest_alergy_effectivness:
                    lowest_alergy_effectivness = effectivness
        return float(Adopter.get_score(self, adoption_center) * lowest_alergy_effectivness)


# a = MedicatedAllergicAdopter("baba","cat", ["cat", "dog"], {"cat": 0.5, "dog": 0.6})
# print a.get_score(AdoptionCenter("asdas", {"cat": 2, "god": 13}, (1,2)))


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        float1, float2 = location
        self.location = (float(float1), float(float2))

    def get_score(self, adoption_center):
        x1, y1 = self.location
        x2, y2 = adoption_center.location
        distance = float(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
        adopter_Score = float(Adopter.get_score(self, adoption_center))
        if distance < 1:
            return adopter_Score
        elif (distance < 3) and (distance >= 1):
            return adopter_Score * (random.uniform(0.7, 0.9))
        elif (distance < 5) and (distance >= 3):
            return adopter_Score * (random.uniform(0.5, 0.7))
        elif distance >= 5:
            return adopter_Score * (random.uniform(0.1, 0.5))


# a= SluggishAdopter("blq", "cat",(1,1))
# print a.get_score(AdoptionCenter("asdas", {"cat": 12, "god": 13}, (1,1)))

import operator


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    center_scores = []
    for center in list_of_adoption_centers:
        center_scores.append((center, adopter.get_score(center)))
    center_scores.sort(key=operator.itemgetter(1), reverse=True)
    return [i[0] for i in center_scores]


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    adoptor_scores = []
    for adoptor in list_of_adopters:
        adoptor_scores.append((adoptor, adoptor.get_score(adoption_center)))
    adoptor_scores.sort(key=lambda x: x[0].get_name(),reverse=False)
    adoptor_scores.sort(key=operator.itemgetter(1), reverse=True)
    if len(adoptor_scores) < n:
        print  [(i[0].get_name(),i[1]) for i in adoptor_scores]
        return [i[0] for i in adoptor_scores]
    result = []
    for i in range(0, n):
        result.append(adoptor_scores[i][0])
    return result


adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("BTwo", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("ASix", "Cat", "Dog")

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2 ,"Cat":12}, (1, 1))

# how to test get_ordered_adoption_center_list
for i in get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 12):
    print i.get_name()
    # you can print the name and score of each item in the list returned
