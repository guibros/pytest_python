import datetime
from Backing_Classes import *
from FuzzySets import Fuzzy
from typing import Dict

#typage par guillaume
#code modelisant la problematique du programme,
#la logique de resolution/optimisation est dans le module experta
class PartyPlanner(KnowledgeEngine):
    PARTY_NONE: str = 'NONE'
    PARTY_BIRTHDAY: str = 'Birthday'
    PARTY_ANNIVERSARY: str = 'Anniversary'
    PARTY_GRADUATION: str = 'Graduation'
    PARTY_GET_TOGETHER: str = 'Get Together'

    AGES_NONE: int = 0
    AGES_KIDS: int = 1
    AGES_EARLY_TENS: int = 2
    AGES_LATE_TENS: int = 3
    AGES_EARLY_TWENTIES: int = 4

    prices: Dict[str, dict] = {'Popcorn': {'Serves': 10, 'Price': 3.5}, 'Chips And Dip': {'Serves': 10, 'Price': 4},
              'Garlic Bread': {'Serves': 2, 'Price': 2.5}, 'Finger Sandwiches': {'Serves': 3, 'Price': 5.75},
              'Spring Rolls': {'Serves': 6, 'Price': 3.5}, 'Fondue': {'Serves': 50, 'Price': 50},
              'Chocolate Fountain': {'Serves': 100, 'Price': 157}, 'Cupcakes': {'Serves': 12, 'Price': 16.5},
              'Mini Pizzas': {'Serves': 3, 'Price': 6}, 'Mini Burgers': {'Serves': 1, 'Price': 2},
              'Birthday Cake': {'Serves': 8, 'Price': 30},

              'Water': {'Serves': 1, 'Price': 0}, 'Soda': {'Serves': 24, 'Price': 11},
              'Juice Boxes': {'Serves': 10, 'Price': 2.5}, 'Beer': {'Serves': 10, 'Price': 11},
              'Vodka': {'Serves': 7, 'Price': 23}, 'Whiskey': {'Serves': 7, 'Price': 34.5},
              'Absinthe': {'Serves': 4, 'Price': 4},

              'Hanging Decorations': {'Set': 6, 'Price': 10}, 'Bunting': {'Set': 1, 'Price': 10},
              'Happy Birthday Banners': {'Set': 1, 'Price': 11}, 'Confetti': {'Set': 2, 'Price': 5},
              'Pinata': {'Set': 1, 'Price': 12}, 'Center Pieces': {'Set': 1, 'Serves': 5, 'Price': 15},
              'Balloons': {'Set': 1, 'Price': 0.9}, 'Candles and Votives': {'Set': 48, 'Price': 39},
              'Party Poppers': {'Set': 20, 'Price': 3},

              'Beverage Napkins': {'Serves': 25, 'Price': 2.5}, 'Plastic Forks': {'Serves': 25, 'Price': 5},
              'Plastic Spoons': {'Serves': 25, 'Price': 5}, 'Plastic Knives': {'Serves': 25, 'Price': 5},
              'Plastic Plates': {'Serves': 9, 'Price': 5}, 'Paper Cups': {'Serves': 12, 'Price': 4},
              'Tablecloths': {'Serves': 1, 'Price': 2}}

    def __init__(self):
        super().__init__()
        self.num_guests = 0
        self.ages = PartyPlanner.AGES_NONE
        self.alcoholic_drinks = False
        self.date = datetime.date(2000, 1, 1)
        self.party_type = PartyPlanner.PARTY_NONE
        self.house_party = False
        self.budget = 0
        self.budget_class = ''

        self.suggested_foods = []
        self.suggested_menus = []
        self.suggested_drinks = []
        self.suggested_playlist = []
        self.suggested_themes = []
        self.suggested_decorations = []
        self.suggested_tableware = []

        self.final_foods_list_backtrack = []
        self.final_drinks_list_backtrack = []
        self.final_decorations_list_backtrack = []

        self.final_foods_list_fuzzy = []
        self.final_drinks_list_fuzzy = []
        self.final_decorations_list_fuzzy = []

        self.final_checklist = []

    @DefFacts()
    def init(self):
        yield Food('House Party', List(['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches', 'Spring Rolls',
                                        'Fondue', 'Chocolate Fountain']))
        yield Food('Kids Party', List(['Popcorn', 'Chips And Dip', 'Cupcakes', 'Finger Sandwiches', 'Mini Pizzas',
                                       'Mini Burgers']))
        yield Food('Birthday', List(['Birthday Cake']))

        yield Drinks('House Party', List(['Water', 'Soda']))
        yield Drinks('Kids Party', List(['Water', 'Soda', 'Juice Boxes']))
        yield Drinks('Alcohol', List(['Beer', 'Absinthe', 'Vodka', 'Whiskey']))

        # Fuzzy Facts
        yield Food('House Party_Very Low', List(['Popcorn', 'Chips And Dip', 'Garlic Bread']))
        yield Food('House Party_Low', List(['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches']))
        yield Food('House Party_Medium', List(['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                               'Spring Rolls']))
        yield Food('House Party_High', List(['Popcorn', 'Chips And Dip', 'Garlic Bread', 'Finger Sandwiches',
                                             'Spring Roll']))
        yield Food('House Party_Very High', List(['Popcorn', 'Chips And Dip', 'Garlic Bread',
                                                  'Finger Sandwiches', 'Spring Rolls', 'Fondue', 'Chocolate Fountain']))

        yield Drinks('House Party_Very Low', List(['Water', 'Soda']))
        yield Drinks('House Party_Low', List(['Water', 'Soda']))
        yield Drinks('House Party_Medium', List(['Water', 'Soda']))
        yield Drinks('Alcohol_Medium', List(['Beer', 'Absinthe']))
        yield Drinks('House Party_High', List(['Water', 'Soda']))
        yield Drinks('Alcohol_High', List(['Beer', 'Absinthe', 'Vodka']))
        yield Drinks('House Party_Very High', List(['Water', 'Soda']))
        yield Drinks('Alcohol_Very High', List(['Beer', 'Absinthe', 'Vodka', 'Whiskey']))

        # TODO implement Menu
        yield Menu('Menu_1', List([]))
        yield Menu('Menu_2', List([]))
        yield Menu('Menu_3', List([]))

        # yield MusicPlaylist('Kids Party', List(['The 1975-Chocolate', 'McFLY-Do Ya', 'PSY-Gangnam Style',
        # 										'One Direction-Best Song Ever', 'Years & Years-King',
        # 										'Coldplay-A Sky Full Of Stars', 'Sliento-Watch Me',
        # 										'Royal Blood-Figure It Out', 'LunchMoney Lewis-Bills',
        # 										'Buddy Holly & His Crickets-That\'ll Be The Day',
        # 										'Deep Purple-Smoke On The Water', 'Katy Perry-Roar',
        # 										'Toni Basil-Hey Mickey', 'The Muppets-Life\' a Happy Song',
        # 										'Taylor Swift-Blank Space', 'One Direction-What Makes You Beautiful',
        # 										'OMI-CHEERLEADER', 'Pharrel Williams-Happy', 'Taylor Swift-Wonderland']))
        # yield MusicPlaylist('Birthday Kids', List(['Selena Gomez-Birthday', 'Weird Al Yankovic-Happy Birthday']))
        # yield MusicPlaylist('Birthday Early Twenties', List(['Selena Gomez-Birthday', 'Sufjan Stevens-Happy Birthday',
        # 													 'Mya-It\'s My Birthday',
        # 						  							 '50 Cent-In Da Club', '2Chainz-Birthday Song',
        # 													 'Rihanna-Birthday Cake',
        # 						                             'Weird Al Yankovic-Happy Birthday', 'The Beatles-Birthday',
        # 						                             'David Joel and Eric Sage-Birthday Drinking Song',
        # 													 'Madonna-B\'day Song']))
        # yield MusicPlaylist('Graduation', List(['Halesy-Castle', 'Kygo & Selena Gomez-It Ain\'t Me',
        # 										'Ed Sheeran-Castle On The Hill',
        # 										'Wiz Khalifa & Charlie Puth-See You Again', 'Lady Gaga-Marry The Night',
        # 										'Rihanna-Never Ending', 'John Legend-Love Me Now', 'Ruth B-Lost Boy',
        # 										'Alessia Cara-Wild Things', 'MO-Final Sonng',
        # 										'Bruno Mars-Too Good To Say Goodbye', 'Beyonce-Run The World',
        # 										'Hayley Kiyoko-Given It All', 'Troye Sivan-YOUTH', ]))

        yield MusicPlaylist('Anniversary',
                            List(['https://open.spotify.com/user/1264690619/playlist/79NydVPZodhn3bG2LyKdrZ']))
        yield MusicPlaylist('Kids Party',
                            List(['https://open.spotify.com/user/bbc_playlister/playlist/6uRN7aisZdhMyJ18irmLkT']))
        yield MusicPlaylist('Graduation',
                            List(['https://open.spotify.com/user/mmmmpai/playlist/7GEDv08p82OGmUP9g0ITYO']))
        yield MusicPlaylist('Birthday',
                            List(['https://open.spotify.com/user/meghantoumey/playlist/62KLyvQEueGcHYXf6HgAlu']))
        yield MusicPlaylist('Birthday Kids', List(['https://open.spotify.com/album/3p9s4eTLHI1VMAgYWEKc3v']))
        yield MusicPlaylist('House Party',
                            List(['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXaXB8fQg7xif',
                                  'https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0IlCGIUGBsA']))
        yield MusicPlaylist('Party Late Tens',
                            List(['https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1N5uK98ms5p']))

        yield Themes('Kids Party', List(['Princess/Prince Theme', 'Disney Theme', 'Easter Egg Hunt', 'Pirate']))
        yield Themes('House Party', List(['Black and White', 'Formal Tea Party', 'Karaoke', 'Harry Potter',
                                          'Lord Of The Rings', 'Mad Scientist', 'Under The Stars', 'Under The Sea',
                                          'Fire and Ice']))

        yield Decorations('Birthday',
                          List(['Happy Birthday Banners', 'Balloons', 'Party Poppers', 'Gift Corner/Table']))
        yield Decorations('Birthday_Under 15', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                     'Gift Corner/Table', 'Pinata', 'Bunting']))
        yield Decorations('Anniversary', List(['Center Pieces', 'Confetti', 'Candles and Votives']))
        yield Decorations('Generic', List(['Confetti', 'Balloons', 'Hanging Decorations']))

        # Fuzzy Facts
        yield Decorations('Birthday_Very Low', List(['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']))
        yield Decorations('Birthday_Low', List(['Happy Birthday Banners', 'Balloons', 'Gift Corner/Table']))
        yield Decorations('Birthday_Medium', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                   'Gift Corner/Table']))
        yield Decorations('Birthday_High', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                 'Gift Corner/Table']))
        yield Decorations('Birthday_Very High', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                      'Gift Corner/Table']))

        yield Decorations('Birthday_Under 15_Very Low', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                              'Gift Corner/Table']))
        yield Decorations('Birthday_Under 15_Low', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                         'Gift Corner/Table']))
        yield Decorations('Birthday_Under 15_Medium', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                            'Gift Corner/Table', 'Pinata']))
        yield Decorations('Birthday_Under 15_High', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                          'Gift Corner/Table', 'Pinata', 'Bunting']))
        yield Decorations('Birthday_Under 15_Very High', List(['Happy Birthday Banners', 'Balloons', 'Party Poppers',
                                                               'Gift Corner/Table', 'Pinata', 'Bunting']))

        yield Decorations('Anniversary_Very Low', List(['Confetti']))
        yield Decorations('Anniversary_Low', List(['Confetti']))
        yield Decorations('Anniversary_Medium', List(['Center Pieces', 'Confetti']))
        yield Decorations('Anniversary_High', List(['Center Pieces', 'Confetti', 'Candles and Votives']))
        yield Decorations('Anniversary_Very High', List(['Center Pieces', 'Confetti', 'Candles and Votives']))

        yield Decorations('Generic_Very Low', List(['Balloons']))
        yield Decorations('Generic_Low', List(['Balloons']))
        yield Decorations('Generic_Medium', List(['Balloons', 'Confetti']))
        yield Decorations('Generic_High', List(['Balloons', 'Confetti', 'Hanging Decorations']))
        yield Decorations('Generic_Very High', List(['Balloons', 'Confetti', 'Hanging Decorations']))

        yield Tableware(List(['Beverage Napkins', 'Plastic Forks', 'Plastic Spoons', 'Plastic Knives', 'Plastic Plates',
                              'Paper Cups', 'Tablecloths']))

        yield Checklist(List(['Make An Invitation List',
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
                              'Have A Great Time']))

    def set_facts(self, num_guests: int, ages: int, alcoholic_drinks: bool, date: datetime, party_type: str, house_party: bool, budget: int):
        self.num_guests = num_guests
        self.ages = ages
        self.alcoholic_drinks = alcoholic_drinks
        self.date = date
        self.party_type = party_type
        self.house_party = house_party
        self.budget = budget
        self.budget_class = Fuzzy.fuzzify_over_n(budget, num_guests)

        self.declare(GuestsNumber(num_guests))
        self.declare(Ages(ages))
        self.declare(Alcoholic(alcoholic_drinks))
        self.declare(Date(date))
        self.declare(PartyType(party_type))
        self.declare(HouseParty(house_party))
        self.declare(Budget(budget))
        self.declare(BudgetClass(self.budget_class))

    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
           Food('House Party', 'foods' << W()))
    def suggest_foods_late_tens_get_together(self, foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))

    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
          Food('House Party', 'foods' << W()))
    def suggest_foods_early_twenties_get_together(self, foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
          Food('Kids Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
    def suggest_foods_kids_birthday(self, foods: List, birthday_foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        for item in birthday_foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
          Food('Kids Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
    def suggest_foods_early_tens_birthday(self, foods: List, birthday_foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        for item in birthday_foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
          Food('House Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
    def suggest_foods_late_tens_birthday(self, foods: List, birthday_foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        for item in birthday_foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))
        print(f"self.suggested_foods:{self.suggested_foods}")
        print(f"self.suggested_foods type:{type(self.suggested_foods)}")

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
          Food('House Party', 'foods' << W()), Food('Birthday', 'birthday_foods' << W()))
    def suggest_foods_early_twenties_birthday(self, foods: List, birthday_foods: List):
        for item in foods.get_list():
            self.suggested_foods.append(item)
        for item in birthday_foods.get_list():
            self.suggested_foods.append(item)
        self.declare(Done('Food'))

    @Rule(HouseParty(False),
          Menu('Menu_1', 'menu1' << W()), Menu('Menu_2', 'menu2' << W()), Menu('Menu_3', 'menu3' << W()))
    def suggest_menus(self, menu1: List, menu2: List, menu3: List):
        self.text = "'''This Program Can Not Predict Exactly What A Restaurant Might Offer In Terms Of Menus Of Food In " \
               "GeneralBut You Can Expect Prices Around 50$ Per Guest''' "
        print(self.text)

    # TODO review drinks suggestion different in house and out
    @Rule(HouseParty(True), Ages(AGES_KIDS),
          Drinks('Kids Party', 'drinks' << W()))
    def suggest_drinks_kids(self, drinks: List):
        for item in drinks.get_list():
            self.suggested_drinks.append(item)
        self.declare(Done('Drinks'))

    @Rule(HouseParty(True), Ages(AGES_EARLY_TENS),
          Drinks('Kids Party', 'drinks' << W()))
    def suggest_drinks_early_tens(self, drinks: List):
        for item in drinks.get_list():
            self.suggested_drinks.append(item)
        self.declare(Done('Drinks'))

    @Rule(HouseParty(True), Ages(AGES_LATE_TENS),
          Drinks('House Party', 'drinks' << W()))
    def suggest_drinks_late_tens(self, drinks: List):
        for item in drinks.get_list():
            self.suggested_drinks.append(item)
        self.declare(Done('Drinks'))

    @Rule(HouseParty(True), Ages(AGES_EARLY_TWENTIES), Alcoholic(False),
          Drinks('House Party', 'drinks' << W()))
    def suggest_drinks_early_twenties(self, drinks: List):
        for item in drinks.get_list():
            self.suggested_drinks.append(item)
        self.declare(Done('Drinks'))

    @Rule(HouseParty(True), Ages(AGES_EARLY_TWENTIES), Alcoholic(True),
          Drinks('House Party', 'drinks' << W()), Drinks('Alcohol', 'alcohol' << W()))
    def suggest_drinks_early_twenties_alcohol(self, drinks: List, alcohol: List):
        for item in drinks.get_list():
            self.suggested_drinks.append(item)
        for item in alcohol.get_list():
            self.suggested_drinks.append(item)
        self.declare(Done('Drinks'))
#music
    @Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS), MusicPlaylist('Birthday Kids', 'playlist' << W()))
    def suggest_music_birthday_kids(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
          MusicPlaylist('Birthday Kids', 'playlist' << W()))
    def suggest_music_birthday_early_tens(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
          MusicPlaylist('Birthday', 'playlist' << W()))
    def suggest_music_birthday_late_tens(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
          MusicPlaylist('Birthday', 'playlist' << W()))
    def suggest_music_birthday_early_twenties(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
          MusicPlaylist('Party Late Tens', 'playlist' << W()))
    def suggest_music_house_party_late_tens(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))
        print(f"self.suggested_playlist:{self.suggested_playlist}")

    @Rule(PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
          MusicPlaylist('House Party', 'playlist' << W()))
    def suggest_music_house_party_early_twenties(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_ANNIVERSARY),
          MusicPlaylist('Anniversary', 'playlist' << W()))
    def suggest_music_anniversary_party(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))

    @Rule(PartyType(PARTY_GRADUATION),
          MusicPlaylist('Graduation', 'playlist' << W()))
    def suggest_music_graduation_party(self, playlist: List):
        for item in playlist.get_list():
            self.suggested_playlist.append(item)
        self.declare(Done('Music'))
#theme
    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
          Themes('House Party', 'themes' << W()))
    def suggest_themes_house_party_late_tens(self, themes: List):
        for item in themes.get_list():
            self.suggested_themes.append(item)
        self.declare(Done('Themes'))

    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
          Themes('House Party', 'themes' << W()))
    def suggest_themes_house_party_early_twenties(self, themes: List):
        for item in themes.get_list():
            self.suggested_themes.append(item)
        self.declare(Done('Themes'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
          Themes('Kids Party', 'themes' << W()))
    def suggest_themes_birthday_kids(self, themes: List):
        for item in themes.get_list():
            self.suggested_themes.append(item)
        self.declare(Done('Themes'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
          Themes('Kids Party', 'themes' << W()))
    def suggest_themes_birthday_early_tens(self, themes: List):
        for item in themes.get_list():
            self.suggested_themes.append(item)
        self.declare(Done('Themes'))

    # decoration
    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_LATE_TENS),
          Decorations('Generic', 'decorations' << W()))
    def suggest_decorations_house_party_late_tens(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))


    @Rule(HouseParty(True), PartyType(PARTY_GET_TOGETHER), Ages(AGES_EARLY_TWENTIES),
          Decorations('Generic', 'decorations' << W()))
    def suggest_decorations_house_party_early_twenties(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))
        print(f"self.suggested_decorations:{self.suggested_decorations}")

    @Rule(HouseParty(True), PartyType(PARTY_GRADUATION),
          Decorations('Graduation', 'decorations' << W()))
    def suggest_decorations_graduation_party(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary', 'decorations' << W()))
    def suggest_decorations_anniversary_party(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_KIDS),
          Decorations('Birthday_Under 15', 'decorations' << W()))
    def suggest_decorations_birthday_kids(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TENS),
          Decorations('Birthday_Under 15', 'decorations' << W()))
    def suggest_decorations_birthday_early_tens(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_LATE_TENS),
          Decorations('Birthday', 'decorations' << W()))
    def suggest_decorations_birthday_late_tens(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True), PartyType(PARTY_BIRTHDAY), Ages(AGES_EARLY_TWENTIES),
          Decorations('Birthday', 'decorations' << W()))
    def suggest_decorations_birthday_early_twenties(self, decorations: List):
        for item in decorations.get_list():
            self.suggested_decorations.append(item)
        self.suggested_decorations.append('Theme Specific Decorations')
        self.declare(Done('Decorations'))

    @Rule(HouseParty(True),
          Tableware('tableware' << W()))
    def suggest_tableware(self, tableware):
        for item in tableware.get_list():
            self.suggested_tableware.append(item)
        self.declare(Done('Tableware'))

    @Rule(HouseParty(True), Done('Food'), Done('Drinks'), Done('Decorations'), Done('Tableware'), Done('Music'),
          Done('Themes'), Budget('budget' << W()))
    def create_list_of_suggestions_backtrack(self, budget: List):
        initial_cost = 0

        # Calculate cost of tableware
        for item in self.suggested_tableware:
            initial_cost += PartyPlanner.prices[item]['Price'] * self.num_guests / PartyPlanner.prices[item]['Serves']

        food_combinations = []
        food_combinations_prices = []
        drinks_combinations = []
        drinks_combinations_prices = []
        decorations_combinations = []
        decorations_combinations_prices = []

        tmp = []
        self.backtrack_food(0, 0, tmp, food_combinations, food_combinations_prices)
        tmp = []
        self.backtrack_drinks(0, 0, tmp, drinks_combinations, drinks_combinations_prices)
        tmp = []
        self.backtrack_decorations(0, 0, tmp, decorations_combinations, decorations_combinations_prices)

        take_foods = -1
        take_drinks = -1
        take_decorations = -1

        min_diff = 1000000
        for i in range(len(food_combinations)):
            for j in range(len(drinks_combinations)):
                for k in range(len(decorations_combinations)):
                    diff = abs(budget -
                               (initial_cost + food_combinations_prices[i] +
                                drinks_combinations_prices[j] + decorations_combinations_prices[k]))
                    if diff < min_diff:
                        min_diff = diff
                        take_foods = i
                        take_drinks = j
                        take_decorations = k

        self.final_foods_list_backtrack = food_combinations[take_foods]
        self.final_drinks_list_backtrack = drinks_combinations[take_drinks]
        self.final_decorations_list_backtrack = decorations_combinations[take_decorations]
        print(f"self.final_foods_list_backtrack:{self.final_foods_list_backtrack}")
        print(f"self.final_drinks_list_backtrack ={self.final_drinks_list_backtrack}")
        print(f"self.final_decorations_list_backtrack ={self.final_decorations_list_backtrack}")

    def backtrack_food(self, i, price, tmp, food_combinations, food_combinations_prices):
        if i == len(self.suggested_foods):
            food_combinations.append(tmp.copy())
            food_combinations_prices.append(price)
            return

        food = self.suggested_foods[i]
        if food == 'Fondue':
            get = int(self.num_guests / PartyPlanner.prices[food]['Serves'])
            if self.num_guests % PartyPlanner.prices[food]['Serves'] > 25:
                get += 1
            price_add = get * PartyPlanner.prices[food]['Price']
            food = food + ' x' + str(get) + ' each serving ' + str(PartyPlanner.prices[food]['Serves'])
            if get > 0:
                tmp.append(food)
                self.backtrack_food(i + 1, price + price_add, tmp, food_combinations, food_combinations_prices)
                tmp.pop()
        elif food == 'Chocolate Fountain':
            get = int(self.num_guests / PartyPlanner.prices[food]['Serves'])
            if self.num_guests % PartyPlanner.prices[food]['Serves'] > 25:
                get += 1
            price_add = get * PartyPlanner.prices[food]['Price']
            food = food + ' x' + str(get) + ' each serving ' + str(PartyPlanner.prices[food]['Serves'])
            if get > 0:
                tmp.append(food)
                self.backtrack_food(i + 1, price + price_add, tmp, food_combinations, food_combinations_prices)
                tmp.pop()
        else:
            price_add = (PartyPlanner.prices[food]['Price'] * self.num_guests / PartyPlanner.prices[food]['Serves'])
            food = food + ' x' + str(int(self.num_guests / PartyPlanner.prices[food]['Serves'])) + \
                   ' each serving ' + str(PartyPlanner.prices[food]['Serves'])

            tmp.append(food)
            self.backtrack_food(i + 1, price + price_add, tmp, food_combinations, food_combinations_prices)
            tmp.pop()

        self.backtrack_food(i + 1, price, tmp, food_combinations, food_combinations_prices)

    def backtrack_drinks(self, i, price, tmp, drinks_combinations, drinks_combinations_prices):
        #print(f"backtrack_drinks.self.suggested_drinks = {self.suggested_drinks}")
        if i == len(self.suggested_drinks):
            drinks_combinations.append(tmp.copy())
            drinks_combinations_prices.append(price)
            return

        drink = self.suggested_drinks[i]
        get = int(self.num_guests / PartyPlanner.prices[drink]['Serves'])
        if self.num_guests % PartyPlanner.prices[drink]['Serves'] > 0:
            get += 1
        price_add = (PartyPlanner.prices[drink]['Price'] * get)

        drink = drink + ' x' + str(get) + ' each serving ' + str(PartyPlanner.prices[drink]['Serves'])
        tmp.append(drink)
        self.backtrack_drinks(i + 1, price + price_add, tmp, drinks_combinations, drinks_combinations_prices)
        tmp.pop()
        self.backtrack_drinks(i + 1, price, tmp, drinks_combinations, drinks_combinations_prices)

    def backtrack_decorations(self, i, price, tmp, decorations_combinations, decorations_combinations_prices):
        if i == len(self.suggested_decorations):
            decorations_combinations.append(tmp.copy())
            decorations_combinations_prices.append(price)
            return

        decoration = self.suggested_decorations[i]
        tmp.append(decoration)
        price_add = 0
        if decoration == 'Hanging Decorations':
            price_add = 2 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Bunting':
            price_add = 6 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Happy Birthday Banners':
            price_add = 3 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Confetti':
            price_add = 3 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Pinata':
            price_add = PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Center Pieces':
            price_add = self.num_guests / 5 * PartyPlanner.prices[decoration]['Price'] / \
                        PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Balloons':
            price_add = 24 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Candles and Votives':
            price_add = 2 * self.num_guests / 5 * PartyPlanner.prices[decoration]['Price'] / \
                        PartyPlanner.prices[decoration]['Set']
        elif decoration == 'Party Poppers':
            price_add = 2 * PartyPlanner.prices[decoration]['Price'] / PartyPlanner.prices[decoration]['Set']
        self.backtrack_decorations(i + 1, price + price_add, tmp, decorations_combinations,
                                   decorations_combinations_prices)
        tmp.pop()
        self.backtrack_decorations(i + 1, price, tmp, decorations_combinations, decorations_combinations_prices)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), Food('House Party_Very Low', 'foods' << W()), NOT(PartyType(PARTY_BIRTHDAY)),
          Drinks('House Party_Very Low', 'drinks' << W()))
    def create_list_of_suggestions_fuzzy_very_low(self, foods: List, drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), Food('House Party_Very Low', 'foods' << W()), PartyType(PARTY_BIRTHDAY),
          Food('Birthday', 'birthday' << W()),
          Drinks('House Party_Very Low', 'drinks' << W()))
    def create_list_of_suggestions_fuzzy_very_low_birthday(self, foods: List, drinks: List, birthday: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in birthday.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), Food('House Party_Low', 'foods' << W()), NOT(PartyType(PARTY_BIRTHDAY)),
          Drinks('House Party_Low', 'drinks' << W()), Alcoholic(False))
    def create_list_of_suggestions_fuzzy_low(self, foods: List, drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), Food('House Party_Low', 'foods' << W()), PartyType(PARTY_BIRTHDAY),
          Food('Birthday', 'birthday' << W()),
          Drinks('House Party_Low', 'drinks' << W()), Alcoholic(False))
    def create_list_of_suggestions_fuzzy_low_birthday(self, foods: List, drinks: List, birthday: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in birthday.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), Food('House Party_Medium', 'foods' << W()), NOT(PartyType(PARTY_BIRTHDAY)),
          Drinks('House Party_Medium', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_Medium', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_medium(self, foods: List, drinks: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), Food('House Party_Medium', 'foods' << W()), PartyType(PARTY_BIRTHDAY),
          Food('Birthday', 'birthday' << W()),
          Drinks('House Party_Medium', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_Medium', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_medium_birthday(self, foods: List, drinks: List, birthday: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in birthday.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), Food('House Party_High', 'foods' << W()), NOT(PartyType(PARTY_BIRTHDAY)),
          Drinks('House Party_High', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_High', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_high(self, foods: List, drinks: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), Food('House Party_High', 'foods' << W()), PartyType(PARTY_BIRTHDAY),
          Food('Birthday', 'birthday' << W()),
          Drinks('House Party_High', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_High', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_high_birthday(self, foods: List, drinks: List, birthday: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in birthday.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), Food('House Party_Very High', 'foods' << W()), NOT(PartyType(PARTY_BIRTHDAY)),
          Drinks('House Party_Very High', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_Very High', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_very_high(self, foods: List, drinks: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), Food('House Party_Very High', 'foods' << W()), PartyType(PARTY_BIRTHDAY),
          Food('Birthday', 'birthday' << W()),
          Drinks('House Party_Very High', 'drinks' << W()), Alcoholic('alcohol' << W()),
          Drinks('Alcohol_Very High', 'alcoholic_drinks' << W()))
    def create_list_of_suggestions_fuzzy_very_high_birthday(self, foods: List, drinks: List, birthday: List, alcohol: List, alcoholic_drinks: List):
        for item in foods.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in birthday.get_list():
            self.final_foods_list_fuzzy.append(item)
        for item in drinks.get_list():
            self.final_drinks_list_fuzzy.append(item)

        if alcohol:
            for item in alcoholic_drinks.get_list():
                self.final_drinks_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_KIDS), Ages(AGES_EARLY_TENS)),
          Decorations('Birthday_Under 15_Very Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_low_birthday_under_15(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_KIDS), Ages(AGES_EARLY_TENS)),
          Decorations('Birthday_Under 15_Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_low_birthday_under_15(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_KIDS), Ages(AGES_EARLY_TENS)),
          Decorations('Birthday_Under 15_Medium', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_medium_birthday_under_15(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_KIDS), Ages(AGES_EARLY_TENS)),
          Decorations('Birthday_Under 15_High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_high_birthday_under_15(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_KIDS), Ages(AGES_EARLY_TENS)),
          Decorations('Birthday_Under 15_Very High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_high_birthday_under_15(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_LATE_TENS), Ages(AGES_EARLY_TWENTIES)),
          Decorations('Birthday_Very Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_low_birthday(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_LATE_TENS), Ages(AGES_EARLY_TWENTIES)),
          Decorations('Birthday_Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_low_birthday(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_LATE_TENS), Ages(AGES_EARLY_TWENTIES)),
          Decorations('Birthday_Medium', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_medium_birthday(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_LATE_TENS), Ages(AGES_EARLY_TWENTIES)),
          Decorations('Birthday_High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_high_birthday(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), PartyType(PARTY_BIRTHDAY), OR(Ages(AGES_LATE_TENS), Ages(AGES_EARLY_TWENTIES)),
          Decorations('Birthday_Very High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_high_birthday(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary_Very Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_low_anniversary(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary_Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_low_anniversary(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary_Medium', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_medium_anniversary(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary_High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_high_anniversary(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), PartyType(PARTY_ANNIVERSARY),
          Decorations('Anniversary_Very High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_high_anniversary(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very Low'), OR(PartyType(PARTY_GET_TOGETHER), PartyType(PARTY_GRADUATION)),
          Decorations('Generic_Very Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_low_generic(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Low'), OR(PartyType(PARTY_GET_TOGETHER), PartyType(PARTY_GRADUATION)),
          Decorations('Generic_Low', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_low_generic(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Medium'), OR(PartyType(PARTY_GET_TOGETHER), PartyType(PARTY_GRADUATION)),
          Decorations('Generic_Medium', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_medium_generic(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('High'), OR(PartyType(PARTY_GET_TOGETHER), PartyType(PARTY_GRADUATION)),
          Decorations('Generic_High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_high_generic(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True), Done('Tableware'), Done('Music'), Done('Themes'),
          BudgetClass('Very High'), OR(PartyType(PARTY_GET_TOGETHER), PartyType(PARTY_GRADUATION)),
          Decorations('Generic_Very High', 'decorations' << W()))
    def create_list_of_decorations_fuzzy_very_high_generic(self, decorations: List):
        for item in decorations.get_list():
            self.final_decorations_list_fuzzy.append(item)

    @Rule(HouseParty(True),
          Checklist('checklist' << W()))
    def create_checklist(self, checklist: List):
        for item in checklist.get_list():
            self.final_checklist.append(item)
