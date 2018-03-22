#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

#for item in (get_partitions(['a','b','c','d'])):
#     print(item)

# The codes below are the answer I made and they worked!!!
def all_partitions(cows):
    cowsset = {key for key in cows}
    all_partitions = []
    for item in get_partitions(cowsset):
        all_partitions.append(item)
    return all_partitions
    
def brute_force_cow_transport(cows, wl):
    all = all_partitions(cows)
    possible_part = []
    weight = 0
    for partition in all:
        weights = []
        for trip in partition:
            for name in trip:
                weight += cows[name]
            weights.append(weight)
            weight = 0
        if max(weights) <= wl:
            possible_part.append(partition)
    s = sorted(possible_part, key = lambda p: len(p))
    return s[0]
