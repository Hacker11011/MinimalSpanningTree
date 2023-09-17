def generate(num_vertexes, chance):
    import random
    edges = []
    if chance == 100:
        for i in range(num_vertexes):
            for j in range(num_vertexes):
                edges.append([random.randint(1, 1000000), i, j])

    else:
        for i in range(num_vertexes):
            for j in range(num_vertexes):
                if random.randint(1, 100) <= chance and i != j:
                    edges.append([random.randint(1, 1000000), i, j])

    return edges