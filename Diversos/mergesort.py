
def merge(llist, rlist):
    """
    Merge two lists into an ordered list.
    """
    final = []
    while llist or rlist:
            # This verification is necessary for not try to compare
            # a NoneType with a valid type.
            if len(llist) and len(rlist):
                if llist[0] < rlist[0]:
                    final.append(llist.pop(0))
                else:
                    final.append(rlist.pop(0))
   
                   # This two conditionals here, is for the case when the two lists
                   # have diferent sizes. This save us of an error trying to acess
                   # an index out of range.
            if not len(llist):
                if len(rlist): final.append(rlist.pop(0))
   
            if not len(rlist):
                if len(llist): final.append(llist.pop(0))
   
    return final
   
def merge_sort(lista):
    """
    Sort the list passed by argument with merge.
    """
    if len(lista) < 2:
        return lista
    mid = len(lista) / 2
    return merge(merge_sort(lista[:mid]), merge_sort(lista[mid:]))

def Text(vetor):
    for i in text:
        vetor_aux.append(i)
    return vetor_aux

caso = int(input())
vetor_aux = []
for i in range(caso):
    text = str(input()).split()


Text(vetor_aux)
merge_sort(vetor_aux)
