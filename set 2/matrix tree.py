
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/matrix-tree/problem

""" 


def tree_traversing(parameters):
    
    m = 10 ** 9 + 7
    
    dict1, dict2, root, result_now, edges_count, backtrack_list = parameters
    
    list_child = dict1[root]
    child = list_child[0]
    result_now =  result_now * (w[child] - w[root])
    result_now = result_now % m
    edges_count += 1
            
    # deleting from dict1
    if len(dict1[root]) == 1:
         del dict1[root]
    else:
        dict1[root].remove(child)
                
    # deleting from dict2
    if len(dict2[child]) == 1:
        del dict2[child]
    else:
        dict2[child].remove(root)
            
    backtrack_list.append(root)
    root = child
    
    return (dict1, dict2, root, result_now, edges_count, backtrack_list)  



def find_determinant(n, w, d1, d2):
    
    m = 10 ** 9 + 7
    final_result  = w[1] % m
    assume_root = 1
    backtrack = []
    edges = 0
    
    while len(d1) > 0:
        if assume_root in d1:
            
            arguments = [d1, d2, assume_root, final_result, edges, backtrack]
            d1, d2, assume_root, final_result, edges, backtrack = tree_traversing(arguments)
            
            
        elif assume_root in d2:

            arguments = [d2, d1, assume_root, final_result, edges, backtrack]
            d2, d1, assume_root, final_result, edges, backtrack = tree_traversing(arguments)
            
            
        elif len(backtrack) > 0:
            assume_root = backtrack.pop() # last element assume_root = backtrack.pop(-1)
        else:
            break
        
    return final_result



if __name__ == "__main__":
    
    n = int(input())
    w = input().split()

    w = { k: int(v) for k, v in enumerate (w, start=1) }
    
    d1 = {}
    d2 = {}
    
    for i in range(n-1):
        a,b = input().split()
        a, b = [int(i) for i in (a,b)]
        
        # a is parent
        # b is child 
        
        # dictionary item structure is parent: [children]
        # d1
        d1[a] = d1.get(a, []) + [b]
        # d2
        d2[b] = d2.get(b, []) + [a]
    
    final_result = find_determinant(n, w, d1, d2)
    print(final_result)


