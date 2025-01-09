import copy
# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3g.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_6.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

eulerian_adj_list = {}
edge_list = []
for entry in input:
    node = entry.split(':')
    print(node)
    eulerian_adj_list[node[0]] = [x for x in node[1].split(' ')[1:]]
    for i in node[1].split(' ')[1:]:
        edge_list.append([node[0],i])


def eulerian_path(adj_lst,edge_lst):
    nodes = {}
    for edge in edge_list:
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
    cycle = [start_node]
    while edge_lst:
        while [cycle[-1],adj_lst[cycle[-1]][0]] in edge_lst:
            curr_edge = [cycle[-1],adj_lst[cycle[-1]][0]]
            adj_lst[curr_edge[0]].pop(0)
            edge_lst.remove(curr_edge)
            cycle.append(curr_edge[1])
            if cycle[-1] == end_node and not adj_lst[cycle[-1]]:
                break
            if not adj_lst[cycle[-1]]:
                break
        if edge_lst:
            while len(cycle) > 1:
                adj_lst[cycle[0]].append(cycle[1])
                edge_lst.append([cycle[0],cycle[1]])
                cycle.pop(0)
            cycle = [start_node]
    return cycle

output_list = eulerian_path(eulerian_adj_list,edge_list)
print(output_list)


# print(output_list)
# output = '->'.join([str(x) for x in output_list])
# with open('Chapter_3\\TB3_Output_files\\BA3G_output.txt', 'w') as f:
#         f.write(output)

output = ' '.join([str(x) for x in output_list])
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_6_output.txt", 'w') as f:
         f.write(output)