import math
import queue
from collections import Counter
from queue import PriorityQueue

# inverted index file format:
# word.field: [document,frequency(raw count),[positions]],[document,frequency(raw count),[positions]],...,[document,frequency(raw count),[positions]]
# .
# .
# .
# word.field: [document,frequency(raw count),[positions]],[document,frequency(raw count),[positions]],...,[document,frequency(raw count),[positions]]
# word.field entries sorted alphabetically (A-Z), postings sorted by ascending document number
# IF_PATH = '../index/inverted_file.txt'
IF_PATH = '../index/comp_inverted_file.txt'
UNCOMPRESSED = 0
COMPRESSED_SINGLE_FREQ = 1

class Document:
    def __init__(self, rank, number):
        self.rank = rank
        self.number = number
    def __cmp__(self, other):
        return cmp(-self.rank, -other.rank)
    def __lt__(self, other):
        return (-self.rank < -other.rank)
    def __eq__(self, other):
        return (self.rank == other.rank)

def dot_product(v1, v2):
    result = 0    
    for c1,c2 in zip(v1,v2):
        result += (c1*c2)
    return result

def norm(v):
    result = 0
    for c in v:
        result += (c**2)
    return math.sqrt(result)

def cos_rank(d, q):
    if len(d) == 1:
        return abs(d[0]-q[0])
    else:
        return (dot_product(d, q)/(norm(d)*norm(q)))

def weight_1_doc(f_ij, n, n_i):
    return f_ij * math.log2(n/n_i)

def weight_1_query(f_iq, maxif_iq, n, n_i):
    return ((1+(f_iq/maxif_iq))/2) * (math.log2(n/n_i))

def weight_2_doc(f_ij):
    return (1+math.log2(f_ij))

def weight_2_query(n, n_i):
    return math.log2(1+(n/n_i))

def weight_3_doc_query(f, n, n_i):
    return (1+math.log2(f))*math.log2(n/n_i)

# query parameter format: [word.field1, word.field2,...,word.field_n], sorted alphabetically(A-Z)
def max_frequency(query):
    return Counter(query).most_common(1)[0][1]

# query parameter format: [word.field1, word.field2,...,word.field_n], sorted alphabetically(A-Z)
def frequency(query, w):
    return Counter(query)[w]

def parse_inverted_file(path, query, compression_mode):
    ils = []    
    f = open(path, 'r')    
    query_pointer = 0
    doc_id = 1
    for line in f:
        if line[0:line.index(':')] == query[query_pointer]:
            ils.append([query[query_pointer]])
            posting = line[line.index(':')+3:-3] if compression_mode == UNCOMPRESSED else line[line.index(':')+2:-1]
            #print(posting)
            postings = posting.split('],[') if compression_mode == UNCOMPRESSED else posting.split(',')
            #print(postings)
            for p in postings:
                data = p.split(',', 2) if compression_mode == UNCOMPRESSED else p
                #data = p.split(',')
                #print(data)
                if compression_mode == UNCOMPRESSED:
                    #ils[-1].append((int(data[0]),int(data[1]),int(data[2])))
                    ils[-1].append((int(data[0]),int(data[1]),[]))                    
                    #print(data[2][1:-1])                    
                    data2 = data[2][1:-1].split(',')
                    #print(data2)
                    for d2 in data2:
                        #print(d2)
                        ils[-1][-1][2].append(int(d2))
                else:
                    if p == postings[0]:
                        doc_id = int(data)
                    else:
                        doc_id += (int(data[:-1]))
                    ils[-1].append((doc_id,1,[]))
            query_pointer += 1
            while(query_pointer < len(query) and query[query_pointer] == query[query_pointer-1]):
                query_pointer += 1
            if(query_pointer) >= len(query):
                break
    f.close()
    return ils

# query parameter format: [word.field1, word.field2,...,word.field_n], sorted alphabetically(A-Z)
def process_query(query, weight_scheme, compression_mode):
    # TODO fetch n (number of documents)
    # test
    n = 16
    # OK ils = [['palavra',(2,4),(3,6),(4,8),(5,5),(10,4),(11,3),(13,3),(14,5)],['p2',(1,7),(4,9),(5,5),(11,3),(13,3),(14,2)],['blabla',(4,7),(5,9),(9,2),(11,5),(12,3),(14,7)]]
    # OK ils = [['blabla',(4,7),(5,9),(9,2),(11,5),(12,3),(14,7)],['p2',(1,7),(4,9),(5,5),(11,3),(13,3),(14,2)]]
    #

    ils = parse_inverted_file(IF_PATH, query, compression_mode)    
    queue = PriorityQueue()
    # no results
    if len(ils) == 0:
        return queue
    query_vector = []
    if weight_scheme == 0: # no tf-idf
        query_vector = len(ils)*[1]
    elif weight_scheme == 1:
        maxif_iq = max_frequency(query)
        for i in range(len(ils)):
            query_vector.append(weight_1_query(frequency(query, ils[i][0]), maxif_iq, n, len(ils[i])-1))
    elif weight_scheme == 2:
        for i in range(len(ils)):
            query_vector.append(weight_2_query(n, len(ils[i])-1))
    elif weight_scheme == 3:
        for i in range(len(ils)):
            query_vector.append(weight_3_doc_query(frequency(query, ils[i][0]), n, len(ils[i])-1))

    # document-at-a-time evaluation    
    i = 0
    j = len(ils)*[1]
    doc_pointer = 1
    advanced = False    
    while(True):
        while(i<len(ils)):
            # print('j_i ', j[i], ' i ',i)
            if(j[i] >= len(ils[i])):
                break
            if(ils[i][j[i]][0]>doc_pointer):
                doc_pointer = ils[i][j[i]][0]
                advanced = i>0
            elif(ils[i][j[i]][0]<doc_pointer):
                while(j[i] < len(ils[i]) and ils[i][j[i]][0]<doc_pointer):
                    j[i] += 1
                if(j[i] >= len(ils[i])):
                    break
                if(ils[i][j[i]][0]>doc_pointer):
                    doc_pointer = ils[i][j[i]][0]
                    advanced = i>0
            i += 1
        else:
            # true if the document #doc_pointer contains all query terms
            if(i == len(ils) and not advanced):
                rank = 0                
                document_vector = []
                if(weight_scheme == 0): # no tf-idf
                    document_vector = len(ils)*[1]
                elif weight_scheme == 1:
                    for m in range(len(ils)):
                        document_vector.append(weight_1_doc(ils[m][j[m]][1], n, len(ils[m])-1))
                elif weight_scheme == 2:
                    for m in range(len(ils)):
                        document_vector.append(weight_2_doc(ils[m][j[m]][1]))
                elif weight_scheme == 3:
                    for m in range(len(ils)):
                        document_vector.append(weight_3_doc_query(ils[m][j[m]][1], n, len(ils[m])-1))
                rank = cos_rank(document_vector, query_vector)                
                print(document_vector)
                print(query_vector)
                print('doc_pointer :', doc_pointer)
                d = Document(rank, doc_pointer)
                queue.put(d)
                doc_pointer += 1
                for k in range(len(j)):
                    j[k] += 1
            i = 0
            advanced = False
            continue
        break
    return queue

def queue_to_list(queue):
    results = []
    while(not queue.empty()):
        d = queue.get()
        results.append((d.number, d.rank))
    return results

# k = len(list1) = len(list2)
def spearman_correlation(list1, list2, k):
    if k == 0:
        return 0
    total = 0
    ids1 = [x[0] for x in list1]
    ids2 = [x[0] for x in list2]
    ids_positions1 = [(x,i+1) for i,x in enumerate(ids1)]
    ids_positions2 = [(x,i+1) for i,x in enumerate(ids2)]
    ids_positions_sorted1 = sorted(ids_positions1, key = lambda x: x[0])
    ids_positions_sorted2 = sorted(ids_positions2, key = lambda x: x[0])
    for e1,e2 in zip(ids_positions_sorted1, ids_positions_sorted2):
        total += ((e1[1]-e2[1])**2)
    return (1 - (6*total)/((k*((k**2)-1))))

# k = len(list1) = len(list2)
def kendal_tau(list1, list2, k):
    if k == 0:
        return 0
    ids1 = [x[0] for x in list1]
    ids2 = [y[0] for y in list2]
    pairs1 = [(x,y) for i,x in enumerate(ids1) for j,y in enumerate(ids1) if x != y and i < j]
    pairs2 = [(x,y) for i,x in enumerate(ids2) for j,y in enumerate(ids2) if x != y and i < j]
    delta = len(set(pairs1) ^ set(pairs2))
    tau = 1 - ((2*delta)/(k*(k-1)))
    return tau


# test
def print_results(l):
    for r in l:
        print(r[0],': ',r[1])
'''
rank0 = process_query(['blabla', 'p2'],0,'uncompressed')
l0 = queue_to_list(rank0)
print_results(l0)
rank1 = process_query(['blabla', 'p2'],1,'uncompressed')
l1 = queue_to_list(rank1)
print_results(l1)
rank2 = process_query(['blabla', 'p2'],2,'uncompressed')
l2 = queue_to_list(rank2)
print_results(l2)
rank3 = process_query(['blabla', 'p2'],3,'uncompressed')
l3 = queue_to_list(rank3)
print_results(l3)

print(spearman_correlation(l0, l1, 4))
print(spearman_correlation(l1, l2, 4))
print(spearman_correlation(l2, l3, 4))
print(spearman_correlation(l1, l3, 4))

print(kendal_tau(l0, l1, 4))
print(kendal_tau(l1, l2, 4))
print(kendal_tau(l2, l3, 4))
print(kendal_tau(l1, l3, 4))

kt_1 = [(1,4), (3,6), (7,2),(4,7),(5,1)]
kt_2 = [(3,6), (7,2), (1,4),(5,1),(4,7)]
print(kendal_tau(kt_1,kt_2,5))

ils2 = parse_inverted_file('inverted', ['blabla', 'p2'], 'uncompressed')
print(ils2)
'''
rank1 = process_query(['produto.fralda', 'produto.pampers'],1,UNCOMPRESSED)
l1 = queue_to_list(rank1)
print_results(l1)

rank2 = process_query(['produto.glicemia'],1,1)
l2 = queue_to_list(rank2)
print_results(l2)


