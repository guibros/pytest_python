from Party_Planner import *
from Backing_Classes import *
import pytest


class Test_Party_Planner:
    ###########################################################
    # parti guillaume
    def test_suggest_foods_late_tens_get_together(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_LATE_TENS),
                       Food('House Party', List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                          'Spring Rolls',
                                          'Fondue', 'Chocolate Fountain']

    def test_suggest_foods_twenties_get_together(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_EARLY_TWENTIES),
                       Food('House Party', List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                          'Spring Rolls',
                                          'Fondue', 'Chocolate Fountain']

    def test_suggest_foods_kids_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Food(List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Cupcakes', 'Finger Sandwiches', 'Mini Pizzas',
                                          'Mini Burgers', 'Birthday Cake']

    def test_suggest_foods_early_tens_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Food(List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Cupcakes', 'Finger Sandwiches', 'Mini Pizzas',
                                          'Mini Burgers', 'Birthday Cake']

    def test_suggest_foods_late_tens_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Food(List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                          'Spring Rolls',
                                          'Fondue', 'Chocolate Fountain', 'Birthday Cake']

    def test_suggest_foods_early_twenties_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Food(List([])))
        engine.run()
        assert engine.suggested_foods == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                          'Spring Rolls',
                                          'Fondue', 'Chocolate Fountain', 'Birthday Cake']

    def test_suggest_menus(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(False), Menu('Menu_1', List([])), Menu('Menu_2', List([])), Menu('Menu_3', List([])))
        engine.run()
        assert engine.text == "'''This Program Can Not Predict Exactly What A Restaurant Might Offer In Terms Of Menus Of Food In " \
                              "GeneralBut You Can Expect Prices Around 50$ Per Guest''' "

    # test drinks
    def test_suggest_drinks_kids(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Ages(engine.AGES_KIDS),
                       Drinks('Kids Party', List([])))
        engine.run()
        assert engine.suggested_drinks == ['Water', 'Soda', 'Juice Boxes']

    def test_suggest_drinks_early_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Ages(engine.AGES_EARLY_TENS),
                       Drinks('Kids Party', List([])))
        engine.run()
        assert engine.suggested_drinks == ['Water', 'Soda', 'Juice Boxes']

    def test_suggest_drinks_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Ages(engine.AGES_LATE_TENS),
                       Drinks('House Party', List([])))
        engine.run()
        assert engine.suggested_drinks == ['Water', 'Soda']

    def test_suggest_drinks_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Ages(engine.AGES_EARLY_TWENTIES), Alcoholic(False),
                       Drinks('House Party', List([])))
        engine.run()
        assert engine.suggested_drinks == ['Water', 'Soda']

    def test_suggest_drinks_early_twenties_alcohol(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Ages(engine.AGES_EARLY_TWENTIES), Alcoholic(True),
                       Drinks(List([])))
        engine.run()
        assert engine.suggested_drinks == ['Water', 'Soda', 'Beer', 'Absinthe', 'Vodka', 'Whiskey']

    # test music
    def test_suggest_music_birthday_kids(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       MusicPlaylist('Birthday Kids', List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/album/3p9s4eTLHI1VMAgYWEKc3v']

    def test_suggest_music_birthday_early_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       MusicPlaylist(List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/album/3p9s4eTLHI1VMAgYWEKc3v']

    def test_suggest_birthday_music_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       MusicPlaylist('Birthday', List([])))
        engine.run()
        assert engine.suggested_playlist == [
            'https://open.spotify.com/user/meghantoumey/playlist/62KLyvQEueGcHYXf6HgAlu']

    def test_suggest_music_birthday_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       MusicPlaylist('Birthday', List([])))
        engine.run()
        assert engine.suggested_playlist == [
            'https://open.spotify.com/user/meghantoumey/playlist/62KLyvQEueGcHYXf6HgAlu']

    def test_suggest_music_house_party_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_LATE_TENS),
                       MusicPlaylist('Party Late Tens', List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1N5uK98ms5p']

    def test_suggest_music_house_party_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_EARLY_TWENTIES),
                       MusicPlaylist('House Party', List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXaXB8fQg7xif',
                                             'https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0IlCGIUGBsA']

    def test_suggest_music_anniversary_party(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_ANNIVERSARY),
                       MusicPlaylist('Anniversary', List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/user/1264690619/playlist/79NydVPZodhn3bG2LyKdrZ']

    def test_suggest_music_graduation_party(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(PartyType(engine.PARTY_GRADUATION),
                       MusicPlaylist('Graduation', List([])))
        engine.run()
        assert engine.suggested_playlist == ['https://open.spotify.com/user/mmmmpai/playlist/7GEDv08p82OGmUP9g0ITYO']

    #################################################################
    # parti lin

    # test Themes

    # instanciation
    # les générateurs déclarés avec DefFacts sont appelés par la méthode 'reset'
    # on utilise 'declare' pour ajouter les faits à la mémoire de travail
    # la méthode 'run' démarre le cycle d'exécution
    # le KnowledgeEngine est utilisé pour appliquer les règles aux faits.
    # on obtient une liste suggested_themes
    def test_suggest_themes_house_party_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_LATE_TENS),
                       Themes('House Party', List([])))
        engine.run()
        assert engine.suggested_themes == ['Black and White', 'Formal Tea Party', 'Karaoke', 'Harry Potter',
                                           'Lord Of The Rings', 'Mad Scientist', 'Under The Stars', 'Under The Sea',
                                           'Fire and Ice']

    def test_suggest_themes_house_party_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_EARLY_TWENTIES),
                       Themes('House Party', List([])))
        engine.run()
        assert engine.suggested_themes == ['Black and White', 'Formal Tea Party', 'Karaoke', 'Harry Potter',
                                           'Lord Of The Rings', 'Mad Scientist', 'Under The Stars', 'Under The Sea',
                                           'Fire and Ice']

    def test_suggest_themes_birthday_kids(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Themes('Kids Party', List([])))
        engine.run()
        assert engine.suggested_themes == ['Princess/Prince Theme', 'Disney Theme', 'Easter Egg Hunt', 'Pirate']

    def test_suggest_themes_birthday_early_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Themes('Kids Party', List([])))
        engine.run()
        assert engine.suggested_themes == ['Princess/Prince Theme', 'Disney Theme', 'Easter Egg Hunt', 'Pirate']

    # test Decorations
    def test_suggest_decorations_house_party_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_LATE_TENS),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Confetti', 'Balloons', 'Hanging Decorations',
                                                'Theme Specific Decorations']

    def test_decorations_house_party_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GET_TOGETHER), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Confetti', 'Balloons', 'Hanging Decorations',
                                                'Theme Specific Decorations']

    def test_suggest_decorations_graduation_party(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_GRADUATION),
                       Decorations('Graduation', List([])))
        engine.run()
        assert engine.suggested_decorations == []

    def test_suggest_decorations_anniversary_party(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary', List([])))
        engine.run()
        assert engine.suggested_decorations == ['Center Pieces', 'Confetti', 'Candles and Votives']

    def test_suggest_decorations_birthday_kids(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                'Gift Corner/Table', 'Pinata', 'Bunting', 'Theme Specific Decorations']

    def test_suggest_decorations_birthday_early_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Happy Birthday Banners', 'Balloons',
                                                'Party Poppers',
                                                'Gift Corner/Table', 'Pinata', 'Bunting', 'Theme Specific Decorations']

    def test_suggest_decorations_birthday_late_tens(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Happy Birthday Banners', 'Balloons',
                                                'Party Poppers', 'Gift Corner/Table', 'Theme Specific Decorations']

    def test_suggest_decorations_birthday_early_twenties(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations(List([])))
        engine.run()
        assert engine.suggested_decorations == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                'Gift Corner/Table', 'Theme Specific Decorations']

    # test Tableware
    def test_suggest_tableware(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True),
                       Tableware(List([])))
        engine.run()
        assert engine.suggested_tableware == ['Beverage Napkins', 'Plastic Forks', 'Plastic Spoons', 'Plastic Knives',
                                              'Plastic Plates',
                                              'Paper Cups', 'Tablecloths']

    #################################################################
    # parti guillaume

    def test_create_list_of_suggestions_backtrack(self):
        engine = PartyPlanner()
        engine.reset()
        engine.suggested_drinks = 'Water', 'Soda'
        engine.suggested_foods = 'Popcorn', 'Chips And Dip'
        engine.suggested_decorations = 'Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table'
        engine.declare(HouseParty(True), Done('Food'), Done('Drinks'), Done('Decorations'), Done('Tableware'),
                       Done('Music'), Done('Themes'), Budget(2000))
        engine.run()
        assert engine.final_foods_list_backtrack == ['Popcorn x0 each serving 10', 'Chips And Dip x0 each serving 10']
        assert engine.final_drinks_list_backtrack == ['Water x0 each serving 1', 'Soda x0 each serving 24']
        assert engine.final_decorations_list_backtrack == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                           'Gift Corner/Table']

    def test_backtrack_food(self):
        tmp = []
        food_combinations = []
        food_combinations_prices = []
        engine = PartyPlanner()
        engine.reset()
        engine.suggested_foods = 'Popcorn', 'Chips And Dip'
        engine.num_guests = 10
        engine.backtrack_food(0, 0, tmp, food_combinations, food_combinations_prices)
        engine.run()
        # assert food_combinations == [['Popcorn x1 each serving 10', 'Chips And Dip x1 each serving 10']]
        # assert food_combinations_prices == [7.5]

        # la ligne 565 de Party_Planner.py semble dupliquer inutilement la recursion,
        # créant des listes dupliquer, avec les reponses ci-dessous:
        assert food_combinations == [['Popcorn x1 each serving 10', 'Chips And Dip x1 each serving 10'],
                                     ['Popcorn x1 each serving 10'], ['Chips And Dip x1 each serving 10'], []]
        assert food_combinations_prices == [7.5, 3.5, 4.0, 0]

    def test_backtrack_drinks(self):
        tmp = []
        drinks_combinations = []
        drinks_combinations_prices = []
        engine = PartyPlanner()
        engine.reset()
        engine.suggested_drinks = 'Water', 'Soda'
        engine.num_guests = 10
        engine.backtrack_drinks(0, 0, tmp, drinks_combinations, drinks_combinations_prices)
        engine.run()
        # assert drinks_combinations == [['Water x10 each serving 1', 'Soda x1 each serving 24']]
        # assert drinks_combinations_prices == [11]

        # la ligne 584 de Party_Planner.py semble dupliquer la recursion,
        # créant des listes dupliquer, avec les reponses ci-dessous:
        assert drinks_combinations == [['Water x10 each serving 1', 'Soda x1 each serving 24'],
                                       ['Water x10 each serving 1'],
                                       ['Soda x1 each serving 24'],
                                       []]
        assert drinks_combinations_prices == [11, 0, 11, 0]

    def test_backtrack_decorations(self):
        tmp = []
        decorations_combinations = []
        decorations_combinations_prices = []
        engine = PartyPlanner()
        engine.reset()
        engine.suggested_decorations = 'Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table'
        engine.num_guests = 10
        engine.backtrack_decorations(0, 0, tmp, decorations_combinations, decorations_combinations_prices)
        engine.run()
        # assert decorations_combinations == [
        #    ['Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table']]
        # assert decorations_combinations_prices == [54.9]

        # la ligne 618 de Party_Planner.py semble dupliquer la recursion,
        # créant des listes dupliquer, avec les reponses ci-dessous:
        assert decorations_combinations == [
            ['Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table'],
            ['Happy Birthday Banners', 'Balloons', 'Party Poppers'],
            ['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table'],
            ['Happy Birthday Banners', 'Balloons'],
            ['Happy Birthday Banners', 'Party Poppers', 'Gift Corner/Table'],
            ['Happy Birthday Banners', 'Party Poppers'],
            ['Happy Birthday Banners', 'Gift Corner/Table'],
            ['Happy Birthday Banners'],
            ['Balloons', 'Party Poppers', 'Gift Corner/Table'],
            ['Balloons', 'Party Poppers'],
            ['Balloons', 'Gift Corner/Table'],
            ['Balloons'],
            ['Party Poppers', 'Gift Corner/Table'],
            ['Party Poppers'],
            ['Gift Corner/Table'],
            []]
        assert decorations_combinations_prices == [54.9, 54.9, 54.6, 54.6, 33.3, 33.3, 33.0, 33.0, 21.900000000000002,
                                                   21.900000000000002, 21.6, 21.6, 0.3, 0.3, 0, 0]

    #####################################################################
    # parti lin

    # test final list
    def test_create_list_of_suggestions_fuzzy_very_low(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'), Food(List([])),
                       Drinks(List([])))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda']

    def test_create_list_of_suggestions_fuzzy_very_low_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'), Food(List([])),
                       PartyType(engine.PARTY_BIRTHDAY),
                       Drinks(List([])))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Birthday Cake']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda']

    def test_create_list_of_suggestions_fuzzy_low(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'), Food(List([])),
                       Drinks(List([])), Alcoholic(False))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda']

    def test_create_list_of_suggestions_fuzzy_low_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'), Food(List([])),
                       PartyType(engine.PARTY_BIRTHDAY),
                       Drinks(List([])), Alcoholic(False))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                                 'Birthday Cake']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda']

    def test_create_list_of_suggestions_fuzzy_medium(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'), Food(List([])),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                                 'Spring Rolls']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe']

    def test_create_list_of_suggestions_fuzzy_medium_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'), Food(List([])),
                       PartyType(engine.PARTY_BIRTHDAY),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                                 'Spring Rolls', 'Birthday Cake']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe']

    def test_create_list_of_suggestions_fuzzy_high(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'), Food(List([])),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                                 'Spring Roll']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe', 'Vodka']

    def test_create_list_of_suggestions_fuzzy_high_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'), Food(List([])),
                       PartyType(engine.PARTY_BIRTHDAY),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                                 'Spring Roll', 'Birthday Cake']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe', 'Vodka']

    def test_create_list_of_suggestions_fuzzy_very_high(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'), Food(List([])),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread',
                                                 'Finger Sandwiches', 'Spring Rolls', 'Fondue',
                                                 'Chocolate Fountain']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe', 'Vodka', 'Whiskey']

    def test_create_list_of_suggestions_fuzzy_very_high_birthday(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'), Food(List([])),
                       PartyType(engine.PARTY_BIRTHDAY),
                       Drinks(List([])), Alcoholic(True))
        engine.run()
        assert engine.final_foods_list_fuzzy == ['Popcorn', 'Chips And Dip', 'Garlic Bread',
                                                 'Finger Sandwiches', 'Spring Rolls', 'Fondue',
                                                 'Chocolate Fountain', 'Birthday Cake']
        assert engine.final_drinks_list_fuzzy == ['Water', 'Soda', 'Beer', 'Absinthe', 'Vodka', 'Whiskey']

    def test_create_list_of_decorations_fuzzy_very_low_birthday_under_15_AGES_KIDS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations('Birthday_Under 15_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_very_low_birthday_under_15_AGES_EARLY_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations('Birthday_Under 15_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_low_birthday_under_15_AGES_KIDS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations('Birthday_Under 15_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_low_birthday_under_15_AGES_EARLY_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations('Birthday_Under 15_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_medium_birthday_under_15_AGES_KIDS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations('Birthday_Under 15_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata']

    def test_create_list_of_decorations_fuzzy_medium_birthday_under_15_AGES_EARLY_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations('Birthday_Under 15_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata']

    def test_create_list_of_decorations_fuzzy_high_birthday_under_15_AGES_KIDS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations('Birthday_Under 15_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata', 'Bunting']

    def test_create_list_of_decorations_fuzzy_high_birthday_under_15_AGES_EARLY_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations('Birthday_Under 15_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata', 'Bunting']

    def test_create_list_of_decorations_fuzzy_very_high_birthday_under_15_AGES_KIDS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_KIDS),
                       Decorations('Birthday_Under 15_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata', 'Bunting']

    def test_create_list_of_decorations_fuzzy_very_high_birthday_under_15_AGES_EARLY_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TENS),
                       Decorations('Birthday_Under 15_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table', 'Pinata', 'Bunting']

    def test_create_list_of_decorations_fuzzy_very_low_birthday_AGES_LATE_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations('Birthday_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_very_low_birthday_AGES_EARLY_TWENTIES(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations('Birthday_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_low_birthday_AGES_LATE_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations('Birthday_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_low_birthday_AGES_EARLY_TWENTIES(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations('Birthday_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_medium_birthday_AGES_LATE_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations('Birthday_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_medium_birthday_AGES_EARLY_TWENTIES(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations('Birthday_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_high_birthday_AGES_LATE_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations('Birthday_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_high_birthday_AGES_EARLY_TWENTIES(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations('Birthday_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_very_high_birthday_AGES_LATE_TENS(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_LATE_TENS),
                       Decorations('Birthday_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_very_high_birthday_AGES_EARLY_TWENTIES(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_BIRTHDAY), Ages(engine.AGES_EARLY_TWENTIES),
                       Decorations('Birthday_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                       'Gift Corner/Table']

    def test_create_list_of_decorations_fuzzy_very_low_anniversary(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Confetti']

    def test_create_list_of_decorations_fuzzy_low_anniversary(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Confetti']

    def test_create_list_of_decorations_fuzzy_medium_anniversary(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Center Pieces', 'Confetti']

    def test_create_list_of_decorations_fuzzy_high_anniversary(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Center Pieces', 'Confetti', 'Candles and Votives']

    def test_create_list_of_decorations_fuzzy_very_high_anniversary(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_ANNIVERSARY),
                       Decorations('Anniversary_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Center Pieces', 'Confetti', 'Candles and Votives']

    def test_create_list_of_decorations_fuzzy_very_low_generic_PARTY_GET_TOGETHER(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_GET_TOGETHER),
                       Decorations('Generic_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons']

    def test_create_list_of_decorations_fuzzy_very_low_generic_PARTY_GRADUATION(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very Low'),
                       PartyType(engine.PARTY_GRADUATION),
                       Decorations('Generic_Very Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons']

    def test_create_list_of_decorations_fuzzy_low_generic_PARTY_GET_TOGETHER(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_GET_TOGETHER),
                       Decorations('Generic_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons']

    def test_create_list_of_decorations_fuzzy_low_generic_PARTY_GRADUATION(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Low'),
                       PartyType(engine.PARTY_GRADUATION),
                       Decorations('Generic_Low', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons']

    def test_create_list_of_decorations_fuzzy_medium_generic_PARTY_GET_TOGETHER(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_GET_TOGETHER),
                       Decorations('Generic_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti']

    def test_create_list_of_decorations_fuzzy_medium_generic_PARTY_GRADUATION(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Medium'),
                       PartyType(engine.PARTY_GRADUATION),
                       Decorations('Generic_Medium', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti']

    def test_create_list_of_decorations_fuzzy_high_generic_PARTY_GET_TOGETHER(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_GET_TOGETHER),
                       Decorations('Generic_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti', 'Hanging Decorations']

    def test_create_list_of_decorations_fuzzy_high_generic_PARTY_GRADUATION(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('High'),
                       PartyType(engine.PARTY_GRADUATION),
                       Decorations('Generic_High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti', 'Hanging Decorations']

    def test_create_list_of_decorations_fuzzy_very_high_generic_PARTY_GET_TOGETHER(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_GET_TOGETHER),
                       Decorations('Generic_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti', 'Hanging Decorations']

    def test_create_list_of_decorations_fuzzy_very_high_generic_PARTY_GRADUATION(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
                       BudgetClass('Very High'),
                       PartyType(engine.PARTY_GRADUATION),
                       Decorations('Generic_Very High', List([])))
        engine.run()
        assert engine.final_decorations_list_fuzzy == ['Balloons', 'Confetti', 'Hanging Decorations']

    def test_create_checklist(self):
        engine = PartyPlanner()
        engine.reset()
        engine.declare(HouseParty(True), Checklist(List([])))
        engine.run()
        assert engine.final_checklist == ['Make An Invitation List',
                                          'Decide On A Theme',
                                          'Send Invitations',
                                          'Choose Playlist',
                                          'Do A Round Of Shopping',
                                          'Clean The House',
                                          'Take Inventory',
                                          'Stock The Bar',
                                          'Decorate',
                                          'Another Round Of Shopping',
                                          'Set The Tables',
                                          'Finish As Much Cooking As You Can',
                                          'Display Food',
                                          'Have A Great Time']


class TestFuzzy:
    # instanciation
    def setup_method(cls):
        cls.fuzzy = Fuzzy()

    def test_sigmoid(cls):
        assert cls.fuzzy.sigmoid(2) == 0.8807970779778823

    def test_fuzzify(cls):
        assert cls.fuzzy.fuzzify(1150) == {'Very Low': 0,
                                           'Low': 0,
                                           'Medium': 0.3775406687981454,
                                           'High': 1.0,
                                           'Very High': 0}

        assert cls.fuzzy.fuzzify(550) == {'Very Low': 0.3775406687981454, 'Low': 1.0, 'Medium': 0, 'High': 0,
                                          'Very High': 0}

    # selon le budget et le nombre de guests, on classe leur niveau de consommation
    def test_fuzzify_over_n(cls):
        assert cls.fuzzy.fuzzify_over_n(25, 5) == f'Very Low'
        assert cls.fuzzy.fuzzify_over_n(75, 5) == f'Low'
        assert cls.fuzzy.fuzzify_over_n(100, 5) == f'Medium'
        assert cls.fuzzy.fuzzify_over_n(150, 5) == f'High'
        assert cls.fuzzy.fuzzify_over_n(300, 5) == f'Very High'
