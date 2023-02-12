from prettytable import PrettyTable

def display(results, withN=False):
    table = PrettyTable()
    if withN:
        table.field_names = ["Titolo", "Artista", "n", "path"]
    else:
        table.field_names = ["Titolo", "Artista", "score", "path"]
    for t in results:
        t = list(t)
        t.append("canzoni/" + t[1] + "." + t[0] + ".canzone.txt")
        table.add_row(t)
    print(table)

    i = int(input("Scegline una (0 annulla): "))
    if not i:
        return
    i -= 1
    print(open("canzoni/" + results[i][1] + "." + results[i][0] + ".canzone.txt", encoding='utf-8').read())