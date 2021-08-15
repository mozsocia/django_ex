import copy


def split_dict_to_multiple(input_dict, max_limit=200):
    """Splits dict into multiple dicts with given maximum size. 
    Returns a list of dictionaries."""
    chunks = []
    curr_dict = {}
    for k, v in input_dict.items():
        if len(curr_dict.keys()) < max_limit:
            curr_dict.update({k: v})
        else:
            chunks.append(copy.deepcopy(curr_dict))
            curr_dict = {k: v}
    # update last curr_dict
    chunks.append(curr_dict)
    return chunks


arr = {

    'name1': "moz",
    'age1': 18,
    'name2': "moz",
    'age2': 18,
    'name3': "moz",
    'age3': 18,
    'name4': "moz",
    'age4': 18,

}


print(split_dict_to_multiple(arr, 2))

print('-----------------')

from itertools import islice

def chunks(data, SIZE=10000):
   it = iter(data)
   for i in range(0, len(data), SIZE):
      yield {k:data[k] for k in islice(it, SIZE)}

      
rs  = list(chunks(arr,2))
print(rs)

print('-----------------')

for i in chunks(arr,2):
    print(i)
