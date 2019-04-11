# Returns YES if class is cancelled, NO otherwise.
def angryProfessor(k, a):
    present = 0
    for time in a:
        if time <= 0:
            present += 1
    if present >= k:
        return "NO"
    return "YES"