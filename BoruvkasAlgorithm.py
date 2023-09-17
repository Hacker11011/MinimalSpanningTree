from RandomGraphGenerator import generate
from time import perf_counter

edges = []

# Input
if not edges:
    if input("Random? y/n: ") == "y":
        num_vertices = int(input("Number of vertices: "))
        chance = int(input("Chance any two vertexes are connected in percents: "))
        start = perf_counter()
        edges = generate(num_vertices, chance)
        end = perf_counter()
        print(f"Generated random graph in {end-start}s")

    elif input("Manual Input? y/n: ") == "y":
        num_vertices = int(input("Number of vertices: "))
        for i in range(num_vertices):
            print("Write a neighbour of vertex ", i, ", followed by the distance - if there are no more neighbours press enter")
            while True:
                inp = input("-> ")
                if not inp:
                    break
                inp = inp.split()
                # Pokud hrana ještě není v grafu - přidat ji do grafu
                if (int(inp[1]), (i, int(inp[0]))) not in edges and (int(inp[1]), (int(inp[0]), i)) not in edges:
                    edges.append((int(inp[1]), (i, int(inp[0]))))


start = perf_counter()
edges = sorted(edges)
end = perf_counter()
print(f"Sorted in {end-start}s")
components = [[x] for x in range(num_vertices)]
tree = []

start = perf_counter()

while len(components) != 1:
    current = edges[0]
    edges.pop(0)

    for component in components:
        if current[1] in component:
            x_component = component

        if current[2] in component:
            y_component = component

    if x_component != y_component:
        tree.append(current)
        components.remove(y_component)
        x_component.extend(y_component)

end = perf_counter()
print(f"Found MST in {end-start}s")
