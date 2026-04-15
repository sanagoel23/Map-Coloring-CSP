import time

graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']
result = {}

def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def backtrack():
    if len(result) == len(graph):
        return True

    for region in graph:
        if region not in result:
            for color in colors:
                if is_valid(region, color):
                    result[region] = color
                    if backtrack():
                        return True
                    del result[region]
            return False

# ⏱ START TIMER HERE
start = time.time()

if backtrack():
    print("Solution Found:")
    for region in result:
        print(region, "→", result[region])
else:
    print("No solution exists")

# ⏱ END TIMER HERE
end = time.time()

print("Execution Time:", end - start, "seconds")
