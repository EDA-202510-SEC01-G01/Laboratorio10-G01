from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import array_list as ar
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me

def new_map(num_elements, load_factor,prime=109345121):
    
    table=ar.new_list()
    capacity=mf.next_prime(num_elements/load_factor)
    while table["size"]<capacity:
        ar.add_last(table, sl.new_list())
    
    retorno={
        "prime": prime,
        "capacity": capacity,
        "scale": rd.randint(1, prime-1),
        "shift": rd.randint(0, prime-1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }
    
    return retorno

def rehash(my_map):
    mapa_nuevo = new_map(my_map["capacity"], 0.5)
    lista_llaves = key_set(my_map)
    lista_valores = value_set(my_map)
    for i in range(0, my_map["size"]):
        elemento=ar.get_element(lista_llaves,i)
        llave=ar.get_element(lista_valores,i)
        put(mapa_nuevo, elemento, llave)
    my_map.update(mapa_nuevo)
    return my_map
    

def put(my_map, key, value):
    hash=mf.hash_value(my_map, key)
    list_in_pos=ar.get_element(my_map["table"], hash)
    if sl.is_empty(list_in_pos)==True:
        entrada=me.new_map_entry(key, value)
        sl.add_last(list_in_pos, entrada)
        my_map["size"]+=1
    else:
        exist=False
        for i in range(0, list_in_pos["size"]):
            entrada_actual=sl.get_element(list_in_pos, i)
            if entrada_actual["key"]==key:
                exist=True
                entrada_actual["value"]=value
        if exist==False:
            entrada=me.new_map_entry(key, value)
            sl.add_last(list_in_pos, entrada)
    my_map["current_factor"]=my_map["size"]/my_map["capacity"]
    if my_map["current_factor"]>my_map["limit_factor"]:
        my_map=rehash(my_map)
        
    return my_map

def contains(my_map, key):
    hash=mf.hash_value(my_map, key)
    list_in_pos=ar.get_element(my_map["table"], hash)
    exist=False
    for i in range(0, list_in_pos["size"]):
        entrada_actual=sl.get_element(list_in_pos, i)
        if entrada_actual["key"]==key:
            exist=True
    return exist

def get(my_map, key):
    rst=None
    hash=mf.hash_value(my_map, key)
    list_in_pos=ar.get_element(my_map["table"], hash)
    for i in range(0, list_in_pos["size"]):
        entrada_actual=sl.get_element(list_in_pos, i)
        if entrada_actual["key"]==key:
            rst=entrada_actual["value"]
    return rst

def remove(my_map, key):
    hash=mf.hash_value(my_map, key)
    list_in_pos=ar.get_element(my_map["table"], hash)
    for i in range(0, list_in_pos["size"]):
        entrada_actual=sl.get_element(list_in_pos, i)
        if entrada_actual["key"]==key:
            sl.delete_element(list_in_pos, i)
            if list_in_pos["size"]==0:
                my_map["size"]-=1
    return my_map
    
def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    rst=False
    if my_map["size"]==0:
        rst=True
    return rst

def key_set(my_map):
    rst=ar.new_list()
    for i in range(0, my_map["capacity"]):
        list_in_pos=ar.get_element(my_map["table"], i)
        for e in range(0, list_in_pos["size"]):
            llave=sl.get_element(list_in_pos, e)
            llave=llave["key"]
            if llave not in rst["elements"]:
                ar.add_last(rst, llave)

    return rst

def value_set(my_map):
    elements=[]
    size=0
    for i in range(0, my_map["capacity"]):
        list_in_pos=ar.get_element(my_map["table"], i)
        for e in range(0, list_in_pos["size"]):
            value=sl.get_element(list_in_pos, e)
            value=value["value"]
            if value not in elements:
                elements.append(value)
                size+=1
    rst= {
        "elements":elements,
        "size":size
    }
    
    return rst