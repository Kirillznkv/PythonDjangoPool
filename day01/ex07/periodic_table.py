import sys

def getLines(filename):
    with open(filename, 'r') as f:
        fstr = f.read()
    return fstr.split('\n')

def getHeadHtml():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table {
                border: 3px solid #424242;
                table-layout: fixed;
                border-collapse: collapse;
                width: 100%;
            }
            th {
                border: 1px solid #424242;
            }
            td {
                border: 1px solid #424242;
            }
        </style>
        <title>day01ex07</title>
    </head>'''
    return html

def getBodyBeginHtml():
    html = "<body>\n"
    return html

def getMarkupMap():
    map_markup = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    ]
    return map_markup

def getCell(line):
    parts = line.split('=')
    name = (parts[0]).strip()
    parts = (parts[1]).split(',')
    html = "<h4>" + name + "</h4>\n<ul>\n"
    i = 0
    for pair in parts:
        if i ==0:
            i = 1
            continue
        html += "<li>"
        if i ==1:
            html += "No "
        html += pair.split(':')[1].strip()
        if i == 4:
            html += " electron"
        html += "</li>\n"
        i += 1
    html += "</ul\n>"
    return html


def getTabelHtml(lines):
    map_markup = getMarkupMap()
    inx_data = 0
    html = "<table>\n"
    for i in range(9):
        html += "<tr>\n"
        for j in range(19):
            html += '<td style="border: 1px solid black; padding:10px">\n'
            if map_markup[i][j] and inx_data < 88 and lines[inx_data].strip() != "":#del
                html += getCell(lines[inx_data])
                inx_data += 1
            html += "</td>\n"
        html += "</tr>\n"
    return html

def getEndHtml():
    html = "</tabel>\n</body>\n</html>\n"
    return html

def getHtml(lines):
    html = getHeadHtml()
    html += getBodyBeginHtml()
    html += getTabelHtml(lines)
    html += getEndHtml()
    return html

def printToFile(filename, html):
    f = open(filename, 'w')
    f.write(html)

if __name__ == '__main__':
    lines = getLines("./periodic_table.txt")
    html = getHtml(lines)
    printToFile("tabel.html", html)