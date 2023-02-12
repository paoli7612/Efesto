from prettytable import PrettyTable

def display(results, withN=False):
    table = PrettyTable()
    if withN:
        table.field_names = ["Titolo", "Artista", "n"]
    else:
        table.field_names = ["Titolo", "Artista"]
    for t in results:
        table.add_row(t)
    print(table)