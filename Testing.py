from a2 import Card, Player, Pickup2Card, Pickup4Card, HumanPlayer, ComputerPlayer, Deck, ReverseCard, SkipCard
import a2_support

# Set Up Uno Game
anna = ComputerPlayer("Anna Truffet")
players = [anna, HumanPlayer("Henry O'Brien"),ComputerPlayer("Josh Arnold")]

deck = Deck([Card(1, "red"), Card(2, "blue"), Card(3, "red"), Card(4, "green")])

game = a2_support.UnoGame(deck, players)


def test_reverse_card():
    print("reverse", '*'*10)
    card = ReverseCard(0, "red")
    print( game.current_player().get_name() )
    # 'Anna Truffet'
    print(game.next_player().get_name())
    # "Henry O'Brien"
    print(game.next_player().get_name())
    # 'Josh Arnold'
    print(game.next_player().get_name())
    # 'Anna Truffet'
    print("Reverse", '-'*10)
    card.play(anna, game)
    print(game.next_player().get_name())
    # 'Josh Arnold'
    print(game.next_player().get_name())
    # "Henry O'Brien"
    print(game.next_player().get_name())
    # 'Anna Truffet'


def test_skip_card():
    print("skip", '*' * 10)
    card = SkipCard(0, "blue")
    print(game.current_player().get_name() == 'Anna Truffet')
    card.play(anna, game)
    print(game.current_player().get_name() == "Henry O'Brien")


def test_pickup2():
    print(game.next_player().get_deck().get_cards() == [])
    card = Pickup2Card(0, "red")
    card.play(anna, game)
    print(game.next_player().get_deck().get_cards() == [Card(3, 'red'), Card(4, 'green')] )


def test_deck():
    # Setup
    card = Card(12, "red")
    special_card = Pickup2Card(0, "red")
    blue_card = ReverseCard(0, "blue")
    cards = [card, special_card, blue_card]
    deck = Deck(cards)

    # Testing
    print("Get Cards:", deck.get_cards()) #== [Card(12, 'red'), Pickup2Card(0, 'red'), ReverseCard(0, 'blue')])
    print("Amount:", deck.get_amount() == 3)

    print("Top:", deck.top()) #ReverseCard(0, blue)

    print()
    new_card = SkipCard(0, "green")
    deck.add_card(new_card)
    deck.add_cards([card, special_card, blue_card])
    print("new amount:", deck.get_amount() == 7)

    print("New Deck:", deck.get_cards())  # [Card(12, red), Pickup2Card(0, red), ReverseCard(0, blue), SkipCard(0, green), Card(12, red), Pickup2Card(0, red),ReverseCard(0, blue)])

    print("Pick:", deck.pick())  # [ReverseCard(0, blue)]
    print("Pick 2:", deck.pick(amount=2)) # [Pickup2Card(0, red), Card(12, red)]
    deck.shuffle()
    print("New Deck", deck.get_cards()) #[SkipCard(0, green), Card(12, red), Pickup2Card(0, red),ReverseCard(0, blue)]


test_reverse_card()
#test_skip_card
#test_pickup2()
#test_deck()





