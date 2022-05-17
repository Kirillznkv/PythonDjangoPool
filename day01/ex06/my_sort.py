def output(d):
    for el in d:
        print(el[0])

def my_sort(d):
    sorted_tuple = sorted(d.items(), key=lambda x: x[0])
    sorted_tuple = sorted(sorted_tuple, key=lambda x: x[1])
    return sorted_tuple

if __name__ == '__main__':
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    sorted_d = my_sort(d)
    output(sorted_d)