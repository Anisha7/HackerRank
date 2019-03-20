# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    A = abs(z - x)
    B = abs(z - y)
    if (A == B):
        return "Mouse C"
    if (A > B):
        return "Cat B"
    return "Cat A"