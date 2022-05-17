import sys

def findCapitalCity(s):
    state = register(s).strip()
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
    return ""

def findState(cc):
    capital_city = register(cc).strip()
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
        return ""
    for key in states:
        if states[key] == id_city:
            return key
    return ""

def register(arg):
    res = arg.lower()
    res = res.title()
    return res

if __name__ == '__main__':
    if len(sys.argv) == 2:
        args = sys.argv[1].split(',')
        for arg in args:
            state = findState(arg)
            if arg.strip() == "":
                continue
            if state != "":
                print(register(arg).strip(), "is the capital of" , state)
            else:
                capital_city = findCapitalCity(arg)
                if capital_city != "":
                    print(capital_city, "is the capital of" , register(arg).strip())
                else:
                    print(arg.strip(), "is neither a capital city nor a state")