from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import array_list as ar
from DataStructures.Map import map_entry as me
    
def new_map(num_elements, load_factor, prime = 109345121): 
    i = 0
    capacity = 0
    capacity = mf.next_prime(num_elements // load_factor)
    scale = rd.randint(1, prime -1)
    shift = rd.randint(0, prime-1)
    table = ar.new_list()
    for j in range (0, int(capacity)):
        ar.add_last(table, {'key': None, 'value':None})
    retorno = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0     
    }
    return retorno
    
def put(map, key, value):
    hash = mf.hash_value(map, key)
    hay_llave, lugar = find_slot(map, key, hash)
    ar.change_info(map['table'], lugar, {'key': key, 'value': value})
    if hay_llave != True:
        map['size'] += 1
    map['current_factor'] = map['size'] / map['capacity']
    if map['current_factor'] >= map['limit_factor']:
        rehash(map)
    return map
    
def contains(map, key):
    hash = mf.hash_value(map, key)
    hay_llave, lugar = find_slot(map, key, hash)
    return hay_llave   

def remove(map, key):
    hash = mf.hash_value(map, key)
    hay_llave, lugar = find_slot(map, key, hash)
    if hay_llave == True:
        ar.delete_element(map['table'], lugar)
        map['size'] -= 1
    map['current_factor'] = map['size'] / map['capacity']
    return map

def get(map, key):
    hash = mf.hash_value(map, key)
    hay_llave, lugar = find_slot(map, key, hash)
    if hay_llave == True:
        return ar.get_element(map['table'], lugar)['value']
    else: 
        return None
def size(map):
    size = map['size']
    return size
    
def is_empty(map):
    empty = False
    if size(map) == 0:
        empty = True
        return empty

def key_set(map):
    lista = ar.new_list()
    for cada_dato in map['table']['elements']:
        if cada_dato['key'] != None:
            ar.add_last(lista, cada_dato['key'])
    return lista

def value_set(map):
    lista = ar.new_list()
    for cada_dato in map['table']['elements']:
        if cada_dato['key'] != None:
            ar.add_last(lista, cada_dato['value'])
    return lista

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = ar.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, ar.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = ar.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False


def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def rehash(map):
    lista_llaves = key_set(map)
    lista_valores = value_set(map)
    nueva_tabla = new_map(map['capacity'], 0.7)
    nueva_capacidad = nueva_tabla['capacity']
    map['capacity'] = nueva_capacidad
    map['current_factor'] = 0
    map['size'] = 0
    map['table'] = nueva_tabla['table']
    for i in range(0, ar.size(lista_llaves)):
        put(map, ar.get_element(lista_llaves,i), ar.get_element(lista_valores,i))