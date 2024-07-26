import random


slot_types = ["A", "B", "C", "D", "E", "F", "G"]


def random_slot():
    return random.choice(slot_types)
