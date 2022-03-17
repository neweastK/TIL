# import sys
# sys.stdin = open("input.txt")

def in_order(v):
    global tree
    global order
    if tree[v] :
        in_order(tree[v][0])
        order.append(v)
        in_order(tree[v][1])
    else :
        order.append(v)


def make_tree(N):
    tree = [0]*(N+1)
    for i in range(1,N+1) :
        if 2*i+1 > N :
            tree[i] = (2*i,0)
            break
        else :
            tree[i] = (2 * i, 2*i+1)

    return tree



# for tc in range(T):
N = int(input())
order = [0]
tree = make_tree(N)
print(tree)
in_order(1)
print(order)
res = [0]*(N+1)
for i in range(1,N+1) :
    res[order[i]] = i

print(res)