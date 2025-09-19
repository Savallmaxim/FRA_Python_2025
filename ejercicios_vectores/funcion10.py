def buscar_numero(array, numero):
    for i in range(len(array)):
        if array[i] == numero:
            return i   
    return -1   