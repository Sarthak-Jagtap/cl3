# MAP FUNCTION
def mapper(line):
    year, temp = line.strip().split(",")
    return int(year), float(temp)

# REDUCE FUNCTION
def reducer(mapped_data):
    data = {}

    for year, temp in mapped_data:
        if year not in data:
            data[year] = []
        data[year].append(temp)

    avg_temp = {}
    for year in data:
        avg_temp[year] = sum(data[year]) / len(data[year])

    return avg_temp


# MAIN
if __name__ == "__main__":

    # Read data
    with open("weather.txt", "r") as f:
        lines = f.readlines()

    # MAP PHASE
    mapped = [mapper(line) for line in lines]

    # REDUCE PHASE
    reduced = reducer(mapped)

    print("Average Temperature per Year:")
    for year, temp in reduced.items():
        print(year, ":", temp)

    # Find hottest & coolest
    hottest = max(reduced, key=reduced.get)
    coolest = min(reduced, key=reduced.get)

    print("\nHottest Year:", hottest)
    print("Coolest Year:", coolest)
