import random
from typing import Dict

from card import Card


class User:
    def __init__(self, name: str):
        pass

    def add_card(self, card: Card):
        pass

    def is_collection_complete(self) -> bool:
        pass

    def discard_card(self, card: Card):
        pass

    def count_all_duplicates(self) -> int:
        pass

    # __str__ già implementato
    def __str__(self) -> str:
        s = f"User: {self.name}\n"
        s += "Collection is " + ("NOT " if not self.is_collection_complete() else "") + "completed\n"
        s += "[Deck]\n"
        for card in self.deck:
            s += str(card) + "\n"
        s += "[Duplicates]\n"
        for card in self.duplicates:
            s += f"{card} : {self.dup_counter[card.code]}\n"
        return s


if __name__ == '__main__':
    c1 = Card(1, "c1")
    c2 = Card(2, "c2")
    user = User("Marco")
    user.add_card(c1)
    user.add_card(c2)
    print(f"Test1: {user.count_all_duplicates()} should be 0")
    print(f"Test2: {user.is_collection_complete()} should be False")
    user.add_card(c2)
    user.add_card(c2)
    user.add_card(c2)
    print(f"Test3: {user.count_all_duplicates()} should be 3")
    user.discard_card(c2)
    print(f"Test4: {user.count_all_duplicates()} should be 2")
    print(f"Test5: {c2 in user.duplicates} should be True")
    user.discard_card(c2)
    user.discard_card(c2)
    print(f"Test6: {c2 in user.duplicates} should be False")
    print(f"Test7: {user.count_all_duplicates()} should be 0")
