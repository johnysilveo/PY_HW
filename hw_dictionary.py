dict1 = {
    'apple': 3,
    'banana': 5,
    'orange': 2,
    'pear': 4,
    'grape': 6,
    'lemon': 1,
    'flamingo': 2,     # bird
    'ibis': 3          # bird
}
dict2 = {
    'banana': 7,        # shared
    'kiwi': 4,          # new fruit
    'apple': 1,         # shared
    'melon': 5,         # new fruit
    'grape': 1,         # shared
    'flamingo': 1,      # shared bird
    'lemon': 2,         # shared
    'leleka': 6         # ptah
}


def merge_dict(d1,d2):
    for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
        
