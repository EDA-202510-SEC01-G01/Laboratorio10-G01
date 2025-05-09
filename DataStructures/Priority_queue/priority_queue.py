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
    return heap
def default_compare_higher_value(nodo1, nodo2):
    llave1 = ipq.get_key(nodo1)
    llave2 = ipq.get_key(nodo2)
    if llave1 >= llave2:
        return True
    else: 
        return False
def default_compare_lower_value(nodo1, nodo2): #Jsantanilla
    print(nodo1)
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
    existe = False
    dato_existente = None
    if is_empty(my_heap) == False:
        for i in range(1,my_heap['size']):
            dato2 = lt.get_element(my_heap['elements'], i)
            if dato2['key'] == key:
                existe = True
                dato_existente = dato2
                break
    if existe == True:
        dato_existente['value'] = value
    else:
        lt.add_last(my_heap['elements'], dato)
        my_heap['size'] +=1
        print(my_heap)
        pos = size(my_heap)
        my_heap = swim(my_heap, pos)
    print(my_heap)
    return  my_heap

def swim(my_heap, pos): #Jsantanilla
    dato = lt.get_element(my_heap['elements'], pos)
    while pos > 1:
        pos_padre = pos // 2
        padre = lt.get_element(my_heap['elements'], pos_padre)
        if pos == 1 or priority(my_heap, padre, dato) == True:
            break
        else:
            lt.exchange(my_heap['elements'], pos_padre, pos)
            dato = padre
            pos = pos_padre
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
        dato = lt.get_element(my_heap["elements"], 1)
        return dato['value']
    

def remove(my_heap):
    if is_empty(my_heap)==True:
        return None
    else:
        raiz = get_first_priority(my_heap)
        last_pos = lt.size(my_heap["elements"])-1
        lt.exchange(my_heap["elements"], 1, last_pos)
        lt.remove_last(my_heap["elements"])
        
        my_heap['size'] -= 1
        sink(my_heap, 1)
            
        return raiz
    
def sink(my_heap, pos):
    while pos < my_heap["size"]:
        hijo1 = pos*2
        hijo2 = (pos*2)+1
        if pos >= my_heap["size"] or (priority(my_heap, pos, hijo1) == True and priority(my_heap, pos, hijo2) == True):
            break
        else:
            elem1 = lt.get_element(my_heap["elements"], hijo1)
            elem2 = lt.get_element(my_heap["elements"], hijo2)
            kh1 = ipq.get_key(elem1)
            kh2 = ipq.get_key(elem2)
            if my_heap["cmp_function"]==default_compare_lower_value:
                hijo_exchange=min(kh1, kh2)
            else:
                hijo_exchange=max(kh1, kh2)
            
            if hijo_exchange==kh1:
                lt.exchange(my_heap['elements'], pos, hijo1)
            else:
                lt.exchange(my_heap['elements'], pos, hijo2)
            pos = hijo_exchange
    return my_heap