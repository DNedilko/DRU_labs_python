# def count_let(let, list):
#     for i in list:
#         if

def str_to_dict(some_str):
    some_dict={}
    for i in some_str:
        some_dict[i]=some_str.count(i)
    return some_dict

print(str_to_dict('rEally_loNG_maSaGE_foR Check'))