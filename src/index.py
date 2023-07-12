# open graph file to be read
f = open('./src/graph.txt','r')
# first line is number of vertices, conver to integer
vertices = int(f.readline(1))
 
i = 0
arr = []
while i <= vertices:
    line = f.readline()
    arr = line.split(" ")
    i += 1

