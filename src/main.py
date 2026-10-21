def sort_waste(item):
    plastic = ["bottle", "bag"]
    paper = ["newspaper", "box"]
    glass = ["jar", "glass"]
    if item in plastic:
        return "plastic"
    if item in paper:
        return "paper"
    if item in glass:
        return "glass"
    return "other"

if __name__ == "__main__":
    print(sort_waste("bottle"))
