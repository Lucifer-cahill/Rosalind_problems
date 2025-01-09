import copy
# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3f.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_2.txt").read()
data = open('sample.txt').read()
input = data.split('\n')

eulerian_adj_list = {}
edge_list = []
for entry in input:
    node = entry.split(':')
    eulerian_adj_list[int(node[0])] = [int(x) for x in node[1].split(' ')[1:]]
    for i in node[1].split(' ')[1:]:
        edge_list.append([int(node[0]),int(i)])


def euler_cycle(adj_lst,edge_lst):
    start_nodes = [x for x in adj_lst]
    start_nodes.remove(0)
    cycle = [0]
    while edge_lst:
        while [cycle[-1],adj_lst[cycle[-1]][0]] in edge_lst:
            curr_edge = [cycle[-1],adj_lst[cycle[-1]][0]]
            adj_lst[curr_edge[0]].pop(0)
            edge_lst.remove(curr_edge)
            cycle.append(curr_edge[1])
            if not adj_lst[cycle[-1]]:
                break
        for node in cycle:
            if len(adj_lst[node]) != 0 and node in start_nodes:
                start_nodes.remove(node)
                index = cycle.index(node)
                for i in range(index):
                    adj_lst[cycle[0]].append(cycle[1])
                    edge_lst.append([cycle[0],cycle[1]])
                    cycle.pop(0)
                break
    return cycle

output_list = euler_cycle(eulerian_adj_list,edge_list)
    
print(output_list)


# print(output_list)
output = '->'.join([str(x) for x in output_list])
with open('Chapter_3\\TB3_Output_files\\BA3F_output.txt', 'w') as f:
        f.write(output)

# output = ' '.join([str(x) for x in output_list])
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_2_output.txt", 'w') as f:
#          f.write(output)