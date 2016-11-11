

import codecs
# read the file, generate graph
def read_input(rpath):
    g = {}
    i = 0
    with codecs.open(rpath, 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            i = i + 1
 #           if i > 100000:
 #               break
            line = line.strip()
            items = line.split(',')
            if len(items) < 3:
                
                print(line.encode('utf-8'))
            id1 = int(items[1])
            id2 = int(items[2])
            if id1 not in g:
                g[id1] = []
            if id2 not in g:
                g[id2] = []
            if id2 not in g[id1]:
                g[id1].append(id2)
            if id1 not in g[id2]:
                g[id2].append(id1)
    return g




def bfs(g, source, d):
    visited = {source: 0}
    queue = [source]
    dist = 0
    while queue:
        current = queue.pop(0)
        dist += 1
        if dist > d:
            break
        for node in g[current]:
            if node not in visited:
                visited[node] = dist
                queue.append(node)
    return visited
                
    
import sys

if __name__ == '__main__':
#    input_path = sys.argv[1]
    input_path = 'batch_payment.txt'
    g = read_input(input_path)
#    floyd_warshall(d,v)
    
