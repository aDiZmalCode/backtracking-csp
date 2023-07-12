# open graph file to be read
f = open('./src/graph.txt','r')

# first line is number of vertices, conver to integer
numVertices = int(f.readline(1))

# color domain
colors = ["Red", "Green", "Blue", "Yellow", "Violet", "Gray", "Orange"]

# vertices must be 2 and more, and 20 or less
if numVertices >= 2 and numVertices <= 20:
    for row in f:
        vertexAdjacent = row.split(' ')
        
        for item in vertexAdjacent:
            vertex = vertexAdjacent[0]
            adjacent = vertexAdjacent[1:]
        

