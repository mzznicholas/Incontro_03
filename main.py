import random

from card import Card
from user import User

users: list[User] = []
cards: list[Card] = []


#  ritorna una carta presa a caso nel set passato come parametro
def pick_random_card(s: set[Card]) -> Card:
    return random.choice(list(s))


def get_interesting_cards(user1, user2) -> set[Card]:
    pass


def count_possible_trades(user1, user2) -> int:
    pass


def make_random_trade(user1: User, user2: User):
    pass


def trade_all_interesting_duplicates(user1: User, user2: User):
    pass


def main():
    marco = User("Marco")
    sara = User("Sara")

    users.append(marco)
    users.append(sara)

    for i in range(1, 11):
        cards.append(Card(i, "carta" + str(i)))

    for i in range(4):
        for z in range(3):
            users[0].add_card(cards[i])
            users[1].add_card(cards[i + 5])

    marco.add_card(cards[4])
    marco.add_card(cards[9])

    sara.add_card(cards[8])

    print(f" -> Marco's duplicates: {marco.count_all_duplicates()} (should be 8)")
    print(f" -> Sara's duplicates: {sara.count_all_duplicates()} (should be 9)")

    print(f" -> Is Marco's collection completed?: {marco.is_collection_complete()} (should be False)")
    print(f" -> Is Sara's collection completed?: {sara.is_collection_complete()} (should be False)")

    trade_all_interesting_duplicates(users[0], users[1])

    # print(marco) # rimuovi il commento se necessario
    print("-" * 10)
    # print(sara) # rimuovi il commento se necessario

    print(f" -> Marco's duplicates: {marco.count_all_duplicates()} (should be 4)")
    print(f" -> Sara's duplicates: {sara.count_all_duplicates()} (should be 5)")

    print(f" -> Is Marco's collection completed?: {marco.is_collection_complete()} (should be True)")
    print(f" -> Is Sara's collection completed?: {sara.is_collection_complete()} (should be False)")


if __name__ == '__main__':
    main()
