from permutation1 import make_files1
from permutation3 import make_files3
from permutation5 import make_files5
from tabulate import tabulate

# Run and collect performance results
def table(fun):
    results = fun

# Build the pivoted table
    table_rows = [
        ["File Size", results["average_size_bytes"], results["median_file_size"], results["std_file_size"]],
        ["Write Time", results["average_write_time"], results["median_write_time"], results["std_write_time"]],
        ["Read Time", results["average_read_time"], results["median_read_time"], results["std_read_time"]]
    ]

    headers = ["Metric", "Average", "Median", "Std"]

    return tabulate(table_rows, headers=headers, tablefmt="grid", floatfmt=".3f")

#Test 1:
print(f'Test 1:')
table(make_files1(tot_n = 500000, max_decks = 1000, seed = 0))
table(make_files3(tot_n = 500000, max_decks = 1000, seed = 0))

#Test 2:
print(f'Test 1:')
table(make_files3(tot_n = 500000, max_decks = 1000, seed = 0))
table(make_files5(tot_n = 500000, max_decks = 1000, seed = 0))


#Test 3:
print(f'Test 1:')

