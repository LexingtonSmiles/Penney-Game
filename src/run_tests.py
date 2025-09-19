from permutation1 import make_files1
from tabulate import tabulate
#from permutation3 import make_files3

#make_files1(tot_n=200, max_decks=10, seed = 0)

#make_files3(tot_n=2000000, max_decks=10000, seed = 0)

# Run and collect performance results
#results = []
#results.append(make_files1(tot_n=9, max_decks=2, seed=0))
#results.append(make_files3(tot_n=9, max_decks=2, seed=0))

# Convert list of dicts to table format
#headers = results[0].keys()        # column headers
#rows = [list(r.values()) for r in results]  # each row is a list of values

# Print the table
#print("\n📊 Read/Write Performance Table:")
#print(tabulate(rows, headers=headers, tablefmt="github"))

# Run and collect performance results
results = []
results.append(make_files1(tot_n=9, max_decks=2, seed=0))

# Build the pivoted table
table_rows = [
    ["File Size", stats["average_size_bytes"], stats["median_file_size"], stats["std_file_size"]],
    ["Write Time", stats["average_write_time"], stats["median_write_time"], stats["std_write_time"]],
    ["Read Time", stats["average_read_time"], stats["median_read_time"], stats["std_read_time"]]
]

headers = ["Metric", "Average", "Median", "Std"]

print(tabulate(table_rows, headers=headers, tablefmt="grid", floatfmt=".3f"))
