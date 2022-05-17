import sys

def findState(capital_city):
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
    id_city = ""
    for key in capital_cities:
        if capital_cities[key] == capital_city:
            id_city = key
    if id_city == "":
        return "Unknown capital city"
    for key in states:
        if states[key] == id_city:
            return key
    return "Error"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        str = findState(sys.argv[1])
        print(str)