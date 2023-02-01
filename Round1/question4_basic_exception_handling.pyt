import sys

def main():
    qty = None
    cost = None

def fetch_quantity():
    """
    Returns a number, any number
    """
    ...
    return ...

def fetch_cost():
    """
    Returns a number, any number
    """

    ...
    return ...

def compute_cost_per_quantity():
    """
    Tries to call the quantity and cost from their respective methods.
    While cost per quantity computes the cost per quantity using cost and quantity.
    if any errors are raised by quantity and cost per quantity an error is raise and the program exits
    else if cost raises an error its absorbed 
    """
    try:
        qty = fetch_quantity()
        cost_per_quantity = cost/qty
    except:
        print('Something went wrong')
        sys.exit(1)
    else:
        cost = fetch_cost()
        

    return cost_per_quantity

cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a + b)