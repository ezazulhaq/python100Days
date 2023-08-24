from prettytable import PrettyTable

pt = PrettyTable()
pt.align = "l"
pt.min_table_width = 30

pt.field_names = ["Name", "Age"]
pt.add_row(["Alice", 21])
pt.add_row(["Bob", 22])
pt.add_row(["Charlie", 23])
pt.add_row(["Charlie", 23])
pt.add_row(["Dave", 24])

print(pt)
