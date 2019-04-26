
CURRENT_STORE = []


def read():
    return CURRENT_STORE, 200


def add(numbers):
    number = numbers.get("number", None)
    CURRENT_STORE.append(number)
    return 201


