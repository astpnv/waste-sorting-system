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

def search_waste(query):
    items = ["bottle", "bag", "newspaper", "box", "jar", "glass"]
    return [i for i in items if query in i]

def get_container(category):
    colors = {"plastic": "yellow", "paper": "blue", "glass": "green"}
    return colors.get(category, "gray")

if __name__ == "__main__":
    print(sort_waste("bottle"))
