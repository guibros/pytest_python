from Party_Planner import *
import math
import datetime


def classify(amount):
    return 1 / (1 + math.exp(-amount))


planner = PartyPlanner()
planner.reset()


# GUI- interface graphique
def numguest():
    print("Combien de personne?")
    choix = None
    while choix is not int:
        try:
            choix = int(input("Veuillez entrer un nombre entier :"))
            break
        except:
            print("L,entrée n'est pas un nombre entier")
    return choix


def group_ages():
    print("Quel groupe d'age?")
    print("1 - enfant")
    print("2 - debut adolescence")
    print("3 - fin adolescence")
    print("4 - debut vingtaine")
    choix = None
    while choix not in [1, 2, 3, 4]:
        try:
            choix = int(input("Choisir entre les groupes 1 à 4 :"))
            if choix in [1, 2, 3, 4]:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
        except:
            print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant au groupe choisit")
    if choix == 1:
        return PartyPlanner.AGES_KIDS
    elif choix == 2:
        return PartyPlanner.AGES_EARLY_TENS
    elif choix == 3:
        return PartyPlanner.AGES_LATE_TENS
    elif choix == 4:
        return PartyPlanner.AGES_EARLY_TWENTIES


def alcool_choice():
    print("Avec ou sans alcool?")
    print("1 - Avec")
    print("2 - Sans")
    choix = None
    while choix not in [1, 2]:
        try:
            choix = int(input("Choisir entre 1-Avec ou 2-Sans :"))
            if choix in [1, 2]:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
        except:
            print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
    if choix == 1:
        return True
    elif choix == 2:
        return False


def date_choice():
    print("Quelle est la date de l'événement?")
    year = None
    month = None
    day = None
    while year is not int:
        try:
            year = int(input("Choisir l'année :"))
            if 2000 < year < 2040:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer une année valide entre 2001 et 2039")
        except:
            print("Le choix n'est pas valide\n veuillez entrer un chiffre entier")
    while month is not int:
        try:
            month = int(input("Choisir le chiffre du mois associé :"))
            if 0 < month < 13:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer une mois valide entre 1 et 12")
        except:
            print("Le choix n'est pas valide\n veuillez entrer un chiffre entier")
    while day is not int:
        try:
            day = int(input("Choisir le chiffre du jour associé :"))
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if 0 < day < 32:
                    break
                else:
                    print("Le choix n'est pas valide\n veuillez entrer une journée valide entre 1 et 31")
            elif month in [4, 6, 9, 11]:
                if 0 < day < 31:
                    break
                else:
                    print("Le choix n'est pas valide\n veuillez entrer une journée valide entre 1 et 30")
            else:
                if 0 < day < 29:
                    break
                else:
                    print("Le choix n'est pas valide\n veuillez entrer une journée valide entre 1 et 28")
        except:
            print("Le choix n'est pas valide\n veuillez entrer un chiffre entier")
    return datetime.date(year, month, day)


def party_type():
    print("Quel type d'evenement?")
    print("1 - Fete de naissance")
    print("2 - anniversaire")
    print("3 - graduation")
    print("4 - get together")
    choix = None
    while choix not in [1, 2, 3, 4]:
        try:
            choix = int(input("Choisir entre les groupes 1 à 4 :"))
            if choix in [1, 2, 3, 4]:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
        except:
            print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant au groupe choisit")
    if choix == 1:
        return PartyPlanner.PARTY_BIRTHDAY
    elif choix == 2:
        return PartyPlanner.PARTY_ANNIVERSARY
    elif choix == 3:
        return PartyPlanner.PARTY_GRADUATION
    elif choix == 4:
        return PartyPlanner.PARTY_GET_TOGETHER


def house_party():
    print("Es-ce un evenement maison?")
    print("1 - oui")
    print("2 - non")
    choix = None
    while choix not in [1, 2]:
        try:
            choix = int(input("Choisir entre 1-oui ou 2-non :"))
            if choix in [1, 2]:
                break
            else:
                print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
        except:
            print("Le choix n'est pas valide\n veuillez entrer le chiffre correspondant a la categorie choisit")
    if choix == 1:
        return True
    elif choix == 2:
        return False


def budget_set():
    print("Combien de budget?")
    choix = None
    while choix is not int:
        try:
            choix = int(input("Veuillez entrer un nombre entier :"))
            break
        except:
            print("L'entrée n'est pas un nombre entier")
    return choix


# ACTIVATION DE L'INTERFACE GRAPHIQUE

def gui_console():
    num_guests = numguest()
    ages = group_ages()
    alcool = alcool_choice()
    date = date_choice()
    party = party_type()
    houseparty = house_party()
    budget = budget_set()

    print(
        f"DONNÉES: \n nombre d'invités: {num_guests} \n catégories d'ages: {ages}\n alcool: {alcool}\n date: {date}\n "
        f"type evenement: {party}\n evenement maison: {houseparty}\n budget: {budget}")

    planner.set_facts(num_guests, ages, alcool, date, party, houseparty, budget)


gui_console()

# date = datetime.date(2018, 5, 29)
# planner.set_facts(20, PartyPlanner.AGES_EARLY_TWENTIES, True, date, PartyPlanner.PARTY_GET_TOGETHER, True, 50)
# planner.set_facts(20, PartyPlanner.AGES_EARLY_TWENTIES, True, date, PartyPlanner.PARTY_GET_TOGETHER, True, 2000)
# planner.set_facts(20, PartyPlanner.AGES_LATE_TENS, True, date, PartyPlanner.PARTY_BIRTHDAY, True, 50)
planner.run()

print(planner.final_foods_list_fuzzy)
print(planner.final_drinks_list_fuzzy)
print(planner.final_decorations_list_fuzzy)
print(planner.final_checklist)
print(planner.budget_class)
# print('Food:', planner.suggested_foods)
# print('Drinks:', planner.suggested_drinks)
print('Music:', planner.suggested_playlist)
print('Tableware:', planner.suggested_tableware)
# print('Theme:', planner.suggested_themes)
# print('Decorations:', planner.suggested_decorations)

# fuzzy = FuzzyLogic.Fuzzy()
# budget = 2000
# planner = PartyPlanner()
# planner.reset()
# planner.set_facts(10, PartyPlanner.AGES_EARLY_TWENTIES, True, 1, PartyPlanner.PARTY_BIRTHDAY, True, 2000)
# print(planner.budget_class)
# planner.run()
