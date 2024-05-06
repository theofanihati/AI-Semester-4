maps= {'A': set (['B', 'H']),
       'B': set (['A', 'C', 'H']),
        'C': set (['B', 'D', 'E']),
        'D': set (['C', 'E', 'F', 'G', 'H']),
        'E': set (['C', 'D']),
        'F': set (['D', 'G']),
        'G': set (['F', 'D', 'H']),
        'H': set (['A', 'B', 'D', 'G']),}

def BFS_shortest_line(maps, start, goal):
    explored = [];
    queue = [[start]];

    if start == goal:
        return "Awal adalah tujuan";

    while queue:
        line = queue.pop(0);
        node = line[-1];

        if node not in explored:
            neighbours = maps[node];

            for neighbour in neighbours:
                new_line = list(line);
                new_line.append(neighbour);
                queue.append(new_line);

                if neighbour == goal:
                    return new_line; 

            explored.append(node);

    return "Mohon maaf node yang kalian pilih tidak ada";

start = input("Masukkan awal: ");
goal = input("Masukkan akhir: ");

print(BFS_shortest_line(maps, start, goal));
