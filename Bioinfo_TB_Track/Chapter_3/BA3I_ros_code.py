# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3i.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_11.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

k = int(input[0])

def bin_kmersfinder(k):
    bin_kmers = []
    for i in range(2**k):
        num = bin(i)[2:]
        while len(num) < k:
            num = '0' + num
        bin_kmers.append(num)
    return bin_kmers

def debruijn_kmers(kmer_list):
    debruijn_adj_lst = {}
    for kmer in kmer_list:
        if kmer[:-1] in debruijn_adj_lst:
            debruijn_adj_lst[kmer[:-1]].append(kmer[1:])
        else:
            debruijn_adj_lst[kmer[:-1]] = [kmer[1:]]

    return debruijn_adj_lst

def euler_cycle(adj_lst):
    edge_lst = []
    for key in adj_lst:
        edge_lst += [[key,i] for i in adj_lst[key]]

    start_nodes = [x for x in adj_lst]
    start_nodes.remove(next(iter(adj_lst)))
    cycle = [next(iter(adj_lst))]
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

def k_uni_circ_string(string_set):
    output = string_set[0]
    for string in string_set[1:-(k-1)]:
        output += string[-1]
    
    return output

kmers = bin_kmersfinder(k)
print(kmers)
db_graph = debruijn_kmers(kmers)
print(db_graph)
cycle = euler_cycle(db_graph)
print(cycle)
output = k_uni_circ_string(cycle)

print(output)

# output = ' '.join([str(x) for x in output_list])
with open('Chapter_3\\TB3_Output_files\\BA3I_output.txt', 'w') as f:
        f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30187_11_output.txt", 'w') as f:
         f.write(output)