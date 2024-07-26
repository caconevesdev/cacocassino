from dataclasses import dataclass
from typing import List
from core.utils import random_slot


@dataclass
class Game:
    slots: List[List[str]]

    def spin_roulette(self):
        self.slots = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
        ]

    def draw(self):
        for l in self.slots:
            for c in l:
                print(f"[ {c} ]", end="")
            print("")

    def verify(self):
        result_slug = False

        # verify horizontals
        count_horizontal = 0
        for l in self.slots:
            if l[0] == l[1] and l[0] == l[2]:
                result_slug = f"horizontal-{count_horizontal}"
            count_horizontal += 1

        # verify diagonal from top to bottom
        count_diagonal = 0
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal += 1

        if dlist[0] == dlist[1] and dlist[0] == dlist[2]:
            result_slug = f"diagonal-t-b"

        # verify diagonal from bottom to top
        count_diagonal = 2
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal -= 1

        if dlist[0] == dlist[1] and dlist[0] == dlist[2]:
            result_slug = f"diagonal-b-t"

        return result_slug
