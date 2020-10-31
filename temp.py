from tabulate import tabulate
print(tabulate([
        ["value1", "value2"], ["value3", "value4"]],
               ["column 1","column 2"], tablefmt="grid"))