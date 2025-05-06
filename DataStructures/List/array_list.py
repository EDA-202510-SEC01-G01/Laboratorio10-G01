import random as r

def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def get_element(my_list, index):
    if index>=my_list["size"]:
        return None
    if index<0:
        return None
    else:
        return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, new_element):
    t_list=[]
    t_list.append(new_element)
    for i in my_list["elements"]:
        t_list.append(i)
    my_list["elements"]=t_list
    my_list["size"]+=1
    return my_list

def add_last(my_list, new_element):
    my_list["elements"].append(new_element)
    my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def last_element(my_list):
    return my_list["elements"][len(my_list["elements"])-1]

def is_empty(my_list):
    if my_list["elements"]==[]:
        return True
    else:
        return False

def remove_first(my_list):
    if my_list["size"]>=1:
        rst=my_list["elements"].pop(0)
    if my_list["size"]>=1:
        my_list["size"]-=1
    return rst

def remove_last(my_list):
    if my_list["size"]>=1:
        rst=my_list["elements"].pop(my_list["size"]-1)
    if my_list["size"]>=1:
        my_list["size"]-=1
    return rst

def insert_element(my_list, position, new_element):
    if my_list["size"]>=1:
        my_list["elements"].append(0)
        i=my_list["size"]
        while i >= position:
            my_list["elements"][i]=my_list["elements"][i-1]
            i-=1
        my_list[position]=new_element
    else:
        my_list["elements"].append(new_element)
    my_list["size"]+=1
    
    return my_list
        
def delete_element(my_list, position):
    my_list["elements"].pop(position)
    my_list["size"]-=1
    return my_list

def change_info(my_list, position, new_element):
    my_list["elements"][position]=new_element
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1==pos2:
        return my_list
    else:
        temp=my_list["elements"][pos1]
        my_list["elements"][pos1]=my_list["elements"][pos2]
        my_list["elements"][pos2]=temp
        return my_list

def sub_list(my_list, pos1, pos2):
    temp_list=[]
    if my_list["size"] >=1:
        for i in range(pos1, pos2):
            temp_list.append(my_list["elements"][i])
        newlist = {
            "elements": temp_list,
            "size": len(temp_list),
    }
    else:
        newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

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
        while j >= 0 and sort_crit(key, get_element(array, j))==True:
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
    mid = array['size']//2
    if array['size'] <= 1:
        return array
    else:
        izq = merge_sort(sub_list(array, 0, mid),sort_crit)
        der = merge_sort(sub_list(array, mid , array['size']),sort_crit)
    unido = merge(izq, der,sort_crit)
    return unido
    
        
def merge(izq, der, sort_crit):
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