import csv
import timeit
from BTrees.OOBTree import OOBTree
from colorama import Fore, init

init(autoreset=True)

def load_items_data(filename):
    items = []
    with open(filename, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            items.append({
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            })
    return items

def add_item_to_tree(tree, item):
    tree[(item["Price"], item["ID"])] = item

def add_item_to_dict(items_dict, item):
    items_dict[item["ID"]] = item

def range_query_tree(tree, min_price, max_price):
    hi = (max_price, float("inf"))
    lo = (min_price, -float("inf"))
    return [v for _, v in tree.items(lo, hi)]

def range_query_dict(items_dict, min_price, max_price):
    return [it for it in items_dict.values() if min_price <= it["Price"] <= max_price]

def compare_structures(filename, min_price=10, max_price=100, repeats=100):
    items = load_items_data(filename)

    tree = OOBTree()
    items_dict = {}

    for it in items:
        add_item_to_tree(tree, it)
        add_item_to_dict(items_dict, it)

    def time_tree():
        return range_query_tree(tree, min_price, max_price)

    def time_dict():
        return range_query_dict(items_dict, min_price, max_price)

    oobtree_time = timeit.timeit(time_tree, number=repeats)
    dict_time = timeit.timeit(time_dict, number=repeats)

    print(Fore.GREEN + f"Total range_query time for OOBTree: {oobtree_time:.6f} seconds")
    print(Fore.RED   + f"Total range_query time for Dict:   {dict_time:.6f} seconds")
    print(Fore.YELLOW + ("OOBTree is faster for range queries!"
                         if oobtree_time < dict_time else
                         "Dict is faster for range queries!"))

if __name__ == "__main__":
    compare_structures("generated_items_data.csv")
