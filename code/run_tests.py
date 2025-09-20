from permutation1 import make_files1
from permutation3 import make_files3
from permutation5 import make_files5
from permutation7 import make_files7
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

# Markdown file to save everything
md_filename = "all_test_results.md"

with open(md_filename, "w") as f:
    f.write("# Performance Test Results\n\n")

    # Test 1
    print("Test 1:")
    perm1 = table(make_files1(tot_n=500000, max_decks=10000, seed=0))
    print(perm1)
    perm3 = table(make_files3(tot_n=500000, max_decks=10000, seed=0))
    print(perm3)
    f.write("## Permutation 1\n\n")
    f.write(perm1 + "\n\n")
    f.write("## Permutation 3\n\n")
    f.write(perm3 + "\n\n")

    # Test 2
    print("Test 2:")
    print(perm3)  # reuse perm3 result
    perm5 = table(make_files5(tot_n=500000, max_decks=10000, seed=0))
    print(perm5)
    f.write("## Permutation 5\n\n")
    f.write(perm5 + "\n\n")

    # Test 3
    print("Test 3:")
    print(perm5)
    perm7 = table(make_files7(tot_n=500000, max_decks=10000, seed=0))
    print(perm7)
    f.write("## Permutation 7\n\n")
    f.write(perm7 + "\n\n")

#print(f"\n All test tables saved to {md_filename}")

