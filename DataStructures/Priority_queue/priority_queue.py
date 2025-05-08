from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as ipq

def new_heap(is_min_pq = True): #Jsantanilla
    heap = {'elements': lt.new_list(),
            'size': 0,
            'cmp_function': None}
    lt.add_last(heap['elements'], None)
    if is_min_pq == True:
        heap['cmp_function'] = default_compare_lower_value
    else: 
        heap['cmp_function'] = default_compare_higher_value
def default_compare_higher_value():
    pass
def default_compare_lower_value(nodo1, nodo2): #Jsantanilla
    llave1 = ipq.get_key(nodo1)
    llave2 = ipq.get_key(nodo2)
    if llave1 <= llave2:
        return True
    else: 
        return False
def priority(my_heap, nodo1, nodo2):
    cmp = my_heap["cmp_function"](nodo1, nodo2)
    if cmp > 0:
        return True
    return False
def insert(my_heap, key, value): #Jsantanilla
    dato = ipq.new_pq_entry(key, value)
    lt.add_last(my_heap['elements'], dato)
    pos = size(my_heap)
    my_heap = swim(my_heap, pos)
    my_heap['size'] +=1
    return  my_heap

def swim(my_heap, pos): #Jsantanilla
    while pos > 1:
        padre = pos // 2
        if pos == 1 or priority(my_heap, padre, pos) == True :
            break
        else:
            lt.exchange(my_heap['elements'], padre, pos)
            pos = padre
    return my_heap
            
def size(my_heap):
    return my_heap["size"]
    
def is_empty(my_heap): #Jsantanilla
    if my_heap['size'] == 0:
        return True
    return False

def get_first_priority(my_heap):
    if is_empty(my_heap)==True:
        return None
    else:
        return lt.get_element(my_heap["elements"], 1)
    

def remove(my_heap):
    raiz=get_first_priority(my_heap)
    lt.exchange(my_heap["elements"], 1, my_heap["elements"]["size"]-1)
    lt.remove_last(my_heap["elements"])
    my_heap = sink(my_heap, 1)
    my_heap['size'] -=1
    return raiz
    
    
    

def sink(my_heap, pos):
    while pos < my_heap["size"]:
        hijo1 = pos*2
        hijo2 = (pos*2)+1
        if pos == my_heap["size"] or (priority(my_heap, pos, hijo1) == True and priority(my_heap, pos, hijo2) == True):
            break
        else:
            kh1=ipq.get_key(hijo1)
            kh2=ipq.get_key(hijo2)
            if my_heap["cmp_function"]==default_compare_lower_value:
                hijo_exchange=min(kh1, kh2)
            else:
                hijo_exchange=max(kh1, kh2)
            lt.exchange(my_heap['elements'], pos, hijo_exchange)
            pos = hijo_exchange
    return my_heap