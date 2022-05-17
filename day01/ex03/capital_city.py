import sys

def findCapitalCity(state):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if state in states:
        id_city = states[state]
        return capital_cities[id_city]
    return "Unknown state"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        str = findCapitalCity(sys.argv[1])
        print(str)