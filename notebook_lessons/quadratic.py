
def run():
    """Allows you to input coefficents to a quadratic equation,  
       solve for the roots of the quadratic eqaution, and
       evaluate the quadratic equation at its calculated roots.
    """
    a, b, c = input_coefficients()
    print()
    print(f"You entered the equation y = {a}x^2 +{b}x + {c}")
    root_1, root_2 = find_roots(a, b, c)
    print(f"the roots of this equation are {root_1} and {root_2}")
    value_1 = evaluate(a, b, c, root_2)
    value_2 = evaluate(a, b, c, root_1)
    print()
    print("Now we can check to make sure this is correct.")
    print(f"{a}x^2 +{b}x + {c} = {value_1} at x = {root_1}")
    print(f"{a}x^2 +{b}x + {c} = {value_2} at x = {root_2}")


def find_roots(a, b, c):
    
    """Given the quadratic a*x**2 + b*x + c, return the values
       of x that evaluate the quadratic to 0."""
    
    fixed_numerator = (b**2.0 - 4.0 * a * c)**0.5
    fixed_denominator = 2.0*a
    root_1 = (-b + fixed_numerator)/fixed_denominator
    root_2 = (-b - fixed_numerator)/fixed_denominator
    return root_1, root_2

def evaluate(a, b, c, x):
    
    """Given the quadratic equation y = a*x**2 + b*x + c at x,
       evaluate the equation at x and return y."""
    
    y = a*x**2.0 + b*x + c
    
    return y

def input_coefficients():
    
    """Returns usere input for a, b, c to 
    determine a quadratic equation y = ax^2 + bx + c
    """
    
    print("Please enter coefficients for quadratic equation")
    print(" given by ax^2 + bx + c")
    print()
    a = float(input("Please enter a: "))
    b = float(input("Please enter b: "))
    c = float(input("Please enter c: "))
    
    return a, b, c
