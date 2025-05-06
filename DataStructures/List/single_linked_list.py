import random as r

def new_list():
    newlist = {
        "first": None,
        "last" : None,
        "size" : 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else: 
            temp = temp['next']
            count += 1
    if not is_in_array:
        count -=1
    return count

def add_first(my_list, element):
    if my_list['size'] == 0:
        my_list['first'] = {'info': element,
                            'next':None}
        my_list['last'] = my_list['first'] #Jsantanilla - Convierte element en el primer y ultimo dato
        my_list['size'] += 1
    else:
        first_anterior = my_list['first']
        my_list['first'] = {'info': element,
                            'next':first_anterior} #Jsantanilla - Convierte element en el primer dato y asigna el primer dato anterior como el siguiente
        my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    if my_list['size'] == 0:
        my_list['first'] = {'info': element,
                            'next':None}
        my_list['last'] = my_list['first'] #Jsantanilla - Convierte element en el primer y ultimo dato
        my_list['size'] += 1
        return my_list
    else: 
        my_list['last']['next'] = {'info':element, 
                                    'next':None} #Jsantanilla - Relaciona element con el ultimo elemento actual de la lista
        my_list['last'] = my_list['last']['next'] #Jsantanilla - Convierte element en el ultimo elemento de la lista y añade 1
        my_list['size'] += 1
    return my_list

def size(my_list):
    cantidad = my_list['size'] #Jsantanilla - Saca el tamaño de la lista, de la variable size y lo retorna
    return cantidad

def first_element(my_list):
    if my_list['size'] != 0:
        primero = my_list['first']['info'] #Jsantanilla - Saca primer elemento de la lista, de la variable first y lo retorna
        return primero
    else:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error

def last_element(my_list):
    if my_list['size'] != 0:
        primero = my_list['last']['info'] #Jsantanilla - Saca ultimo elemento de la lista, de la variable last y lo retorna
        return primero
    else:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error

def remove_first(my_list):
    if my_list['size'] == 1:#Jsantanilla - Valida cuando solo hay un elemento para eliminar el dato last
        elemento = my_list['first']['info']
        my_list ['first'] = None
        my_list ['last'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] != 0 and my_list['size'] != 1: #Jsantanilla - Guarda el siguiente en una variable, la asigna a first y borra relacion con el anterior.
        elemento = my_list['first']['info']
        siguiente = my_list['first']['next']
        my_list['first']['next'] = None
        my_list['first'] = siguiente
        my_list['size'] -= 1
        return elemento
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error
    return my_list
    
def remove_last(my_list):
    if my_list['size'] == 1:#Jsantanilla - Valida cuando solo hay un elemento para eliminar el dato first
        elemento = my_list['last']['info']
        my_list ['first'] = None
        my_list ['last'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] != 0 and my_list['size'] != 1: 
        elemento = my_list ['last']['info']
        nodo = my_list['first']
        while nodo['next'] != my_list['last']: #Jsantanilla - Corta relacion con last desde el dato anterior y asigna uno nuevo
            nodo = nodo['next']
        my_list['last'] = nodo
        nodo['next'] = None
        my_list['size'] -= 1
        return elemento
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range') #Jsantanilla - Retorna error
    return my_list

def is_empty(my_list):
    if my_list['size'] == 0: #Jsantanilla - Valida con la variable size el tamaño de la lista
        return True
    else:
        return False

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 1
    nodo = my_list['first']
    if my_list['size'] == 1:
        my_list = add_first(my_list, element) #Jsantanilla - Valida que haya más de un solo elemento 
        posicion+=1
    else:
        while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y añade el nuevo elemento
        if nodo != my_list['last']:
            nodo_anterior = nodo
            nodo_siguiente = nodo['next']
            nodo_anterior['next'] = {'info': element,
                               'next':nodo_siguiente}
            my_list['size'] +=1
        else:
            my_list = add_last(my_list, element)#Jsantanilla - Valida que cuando se quiere insertar en el ultimo elemento
    return my_list

def delete_element(my_list,pos):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 0
    nodo = my_list['first']
    if my_list['size'] == 1:
        remove_first(my_list) #Jsantanilla - Valida que haya más de un solo elemento 
    else:
        while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y elimina el elemento
        if nodo != my_list['last'] and nodo !=my_list["first"]:
            nodo_anterior = nodo
            nodo_siguiente = nodo['next']
            nodo_anterior['next'] = nodo_siguiente
            my_list['size'] -=1
        elif nodo==my_list["last"]:
            remove_last(my_list)#Jsantanilla - Valida que cuando se quiere insertar en el ultimo elemento
        elif nodo==my_list["first"]:
            remove_first(my_list)
    return my_list

def change_info(my_list,pos,new_info):
    if pos < 0 or pos > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    posicion = 1
    nodo = my_list['first']
    while posicion != pos and nodo['next'] != None:
            nodo = nodo['next']     #Jsantanilla - Cuenta posiciones y cambia la informacion
    nodo['info'] = new_info
    return my_list

def exchange (my_list,pos1,pos2):
    if pos1 < 0 or pos1 > size(my_list)-1 or pos2 < 0 or pos2 > size(my_list):#Jsantanilla - Retorna error
        raise Exception('IndexError: list index out of range')
    if pos1 == pos2:
        return my_list
    else:
        posicion = 0
        nodo = my_list['first']
        exchange = False
        while exchange != True: #Jsantanilla - Valida que el cambio no este hecho
            if posicion == pos1:
                info1 = nodo['info']
                nodo1 = nodo
            if posicion == pos2: 
                info2 = nodo['info']
                nodo2 = nodo
            elif posicion >= pos1 and posicion >= pos2:
                nodo1['info'] = info2
                nodo2['info'] = info1
                exchange = True   
            if exchange !=True:
                nodo = nodo['next']
            posicion += 1
        return my_list  
    
def sub_list(my_list, pos, pos2):
    if pos < 0 or pos >= size(my_list) or pos2 > size(my_list) or pos > pos2:
        raise Exception('IndexError: list index out of range')

    nueva_lista = {'first': None, 'last': None, 'size': 0}
    nodo = my_list['first']
    posicion = 0

    while nodo is not None:
        if pos <= posicion < pos2:
            add_last(nueva_lista, nodo['info'])
        nodo = nodo['next']
        posicion += 1

    return nueva_lista
def default_sort_criteria(elem1, elem2):
    is_sorted = False
    if elem1 < elem2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    i=0
    while i != my_list["size"]:
        menor=None
        for e in range(i, my_list["size"]):
            if sort_crit(get_element(my_list, e), get_element(my_list, i))==True:
                if menor==None:
                    menor=get_element(my_list, e)
                    pos_menor=e
                elif sort_crit(get_element(my_list, e), menor)==True:
                    menor=get_element(my_list, e)
                    pos_menor=e
        if menor!=None:
            exchange(my_list, i, pos_menor)
        i+=1

    return my_list

def insertion_sort(array, sort_crit):
    for i in range (1, array["size"]):
        key = get_element(array, i)
        j = i - 1
        while j >= 0 and sort_crit(key, get_element(array, j)) == True:
            exchange(array, j+1,j)
            j -=1
    return array



def shell_sort(array, sort_crit):
    n = array['size']
    h = 1
    while h < n:
        h = h* 3 + 1
    while h > 0:
        for i in range(h,n):
            key = get_element(array, i)
            j = i
            while j >= h and sort_crit(key, get_element(array, j-h))==True:
                exchange(array, j,j-h)
                j -= h
        h //=3
    return array         

def merge_sort(array,sort_crit):
    lista = new_list()
    mid = array['size']//2
    if array['size'] <= 1:
        return array
    else:
        izq = merge_sort(sub_list(array, 0, mid))
        der = merge_sort(sub_list(array, mid , array['size']))
    unido = merge(izq, der, sort_crit)
    for i in range(0,unido['size']):
        add_last(lista, get_element(unido, i))
    return lista
    
        
def merge(izq, der,sort_crit):
    retorno = new_list()
    i = 0
    j = 0
    while i < izq['size'] and j < der['size']:
        if sort_crit(get_element(izq, i), get_element(der, j)):
            add_last(retorno, get_element(izq, i))
            i+= 1        
        else:
            add_last(retorno, get_element(der, j))
            j+=1
    while i < izq['size']:
        add_last(retorno, get_element(izq, i))
        i+= 1  
    while j < der['size']:
        add_last(retorno, get_element(der, j))
        j+= 1  
    return retorno

def quick_sort(my_list, sort_crit, lo, hi): 

    if lo!=hi:
        pivot=r.randint(lo, hi)
        
        i=lo
        j=hi
        
        while j>=i:
            while i<=hi and get_element(my_list, i)<=get_element(my_list, pivot):
                if i>j:
                    break
                i+=1
            while j>=lo and get_element(my_list, j)>get_element(my_list, pivot):
                if i>j:
                    break
                j-=1
            if i<j:
                if i>hi:
                    exchange(my_list, i-1, j)
                elif j<lo:
                    exchange(my_list, i, j+1)
                else:
                    exchange(my_list, i, j)
        exchange(my_list, pivot, j)
        #print(my_list)
        if lo < j:
            quick_sort(my_list, sort_crit, lo, j)
        if i < hi:
            quick_sort(my_list, sort_crit, i, hi)
        return my_list