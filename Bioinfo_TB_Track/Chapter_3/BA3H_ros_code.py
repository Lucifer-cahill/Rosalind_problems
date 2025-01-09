# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3h.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_7.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

k = int(input[0])
kmer_comp = input[1].split(' ')

def debruijn_kmers(kmer_list):
    debruijn_adj_lst = {}
    for kmer in kmer_list:
        if kmer[:-1] in debruijn_adj_lst:
            debruijn_adj_lst[kmer[:-1]].append(kmer[1:])
        else:
            debruijn_adj_lst[kmer[:-1]] = [kmer[1:]]

    return debruijn_adj_lst

def eulerian_path(adj_lst):
    edge_lst = []
    for key in adj_lst:
        edge_lst += [[key,i] for i in adj_lst[key]]

    nodes = {}
    for edge in edge_lst:
        if edge[0] not in nodes:
            nodes[edge[0]] = [1,0]
        else: 
            nodes[edge[0]][0] += 1
        if edge[1] not in nodes:
            nodes[edge[1]] = [0,1]
        else:
            nodes[edge[1]][1] += 1
    for node in nodes:
        if nodes[node][0] > nodes[node][1]:
            start_node = node
        if nodes[node][0] < nodes[node][1]:
            end_node = node
            if end_node not in adj_lst:
                adj_lst[end_node] = []

    print(start_node,end_node)
    path = [start_node]
    while edge_lst:
        while [path[-1],adj_lst[path[-1]][0]] in edge_lst:
            curr_edge = [path[-1],adj_lst[path[-1]][0]]
            adj_lst[curr_edge[0]].pop(0)
            edge_lst.remove(curr_edge)
            path.append(curr_edge[1])
            if path[-1] == end_node and not adj_lst[path[-1]]:
                break
            if not adj_lst[path[-1]]:
                break
        if edge_lst:
            while len(path) > 1:
                adj_lst[path[0]].append(path[1])
                edge_lst.append([path[0],path[1]])
                path.pop(0)
            path = [start_node]
    return path

def genome_path(string_set):
    output = string_set[0]
    for string in string_set[1:]:
        output += string[-1]
    
    return output

debruijn_graph = debruijn_kmers(kmer_comp)

print(debruijn_graph)

eul_path = eulerian_path(debruijn_graph)

print(eul_path)

output = genome_path(eul_path)

print(output)
# print(output_list)

# output = ' '.join([str(x) for x in output_list])
# with open('Chapter_3\\TB3_Output_files\\BA3H_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_7_output.txt", 'w') as f:
         f.write(output)