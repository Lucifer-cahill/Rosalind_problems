# data = open('ID_LGIS\\rosalind_lgis.txt').read()
data = open('sample.txt').read()
input = data.split('\n')
n = int(input[0])
permu = [int(x) for x in input[1].split(' ')]

def longest_inc_subseq(arr,n):
    subseq_lst = [[arr[0]]]
    subseq_lst_new = []
    low_num = n
    for i in arr:
        flag = False
        print(i,'____________',len(subseq_lst))
        # subseq_lst = subseq_lst_new.copy()
        for lst in subseq_lst:
            if i > lst[-1]:
                lst.append(i)
                continue
            if i < lst[0]:
                if [i] not in subseq_lst:
                    subseq_lst.append([i])
                continue
            if i > lst[0]:
                j = 1
                while i > lst[j]:
                    j += 1
                if i == lst[j]:
                    break
                if lst[:j] + [i] not in subseq_lst:
                    subseq_lst.append(lst[:j] + [i])

        # subseq_lst.append([i])
                
        ender = []
        for lst in subseq_lst:
            if lst[-1] not in ender:
                ender.append(lst[-1])
        
        pot_seq_dict = {key: [] for key in ender}

        for lst in subseq_lst:                               
            if len(lst) >= len(pot_seq_dict[lst[-1]]):
                pot_seq_dict[lst[-1]] = lst    
        
        print(pot_seq_dict)

        # subseq_lst = list(pot_seq_dict.values())

        for lst in subseq_lst:
            print(lst) 

    len_lst = [len(x) for x in subseq_lst]
    max_seq = subseq_lst[len_lst.index(max(len_lst))]
                
    return max_seq

def new_longest_inc_subseq(arr,n):


    return


def longest_dec_subseq(arr):
    subseq_lst = []
    subseq_lst_new = []
    for i in arr:
        # print(i,'________________')
        # subseq_lst = subseq_lst_new.copy()
        subseq_lst.append([i])
        for lst in subseq_lst:
            if i < lst[-1]:
                lst.append(i)
                continue
            if i > lst[0]:
                continue
            if i < lst[0]:
                j = 1
                while i < lst[j]:
                    j += 1
                if i == lst[j]:
                    break
                if lst[:j] + [i] not in subseq_lst:
                    subseq_lst.append(lst[:j] + [i])

        # ender = []
        # for lst in subseq_lst:
        #     if lst[-1] not in ender:
        #         ender.append(lst[-1])
        
        # max_len_dict = {key: [] for key in ender}

        # for lst in subseq_lst:
        #     if len(lst) > len(max_len_dict[lst[-1]]):
        #         max_len_dict[lst[-1]] = lst

        # subseq_lst = list(max_len_dict.values())   
        
        # for lst in subseq_lst:
        #     print(lst) 

    len_lst = [len(x) for x in subseq_lst]
    max_seq = subseq_lst[len_lst.index(max(len_lst))]
                
    return max_seq

def longest_inc_subseq_ai(arr):
    if not arr:
        return []
    
    n = len(arr)
    lengths = [1] * n  # lengths[i] will hold the length of the longest increasing subsequence ending with arr[i]
    predecessors = [-1] * n  # predecessors[i] will hold the index of the predecessor of arr[i] in the LIS
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
    # Find the index of the maximum length
    max_length_index = lengths.index(max(lengths))
    
    # Reconstruct the LIS
    lis = []
    while max_length_index != -1:
        lis.append(arr[max_length_index])
        max_length_index = predecessors[max_length_index]
    
    return lis[::-1]


inc_list = longest_inc_subseq(permu,n)      
print(inc_list)
inc_list_ai = longest_inc_subseq_ai(permu)      
print(inc_list_ai)
# dec_list = longest_dec_subseq(permu)      
# print(dec_list)



# output = '\n'.join([' '.join([str(x) for x in inc_list]),' '.join([str(x) for x in dec_list])])
# # # print(output)
# with open('ID_LGIS\\LGIS_output.txt', 'w') as f:
#         f.write(output)

