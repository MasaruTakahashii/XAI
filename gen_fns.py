
def ethToProcess(x):
    return float(x) / 10**18

def process_to_wei(n):
    return int(n * (10**18))

def merkle_root(nodes):
    while len(nodes) > 1:
        temp_nodes = []
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])

        for i in range(0, len(nodes), 2):
            h = sha3_array([nodes[i], nodes[i+1]])
            temp_nodes.append(h)
        nodes = temp_nodes
    return nodes[0]


