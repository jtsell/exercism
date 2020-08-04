def raindrops(number):
    raindict = {3: "Pling", 5: "Plang", 7: "Plong"}
    drops = str()
    for i, j in raindict.items():
        if number % i is 0:
            drops += j
    if drops is "":
        drops = str(number)
    return drops

