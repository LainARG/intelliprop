import numpy as np
from math import log, exp

#Returns wether the input is valid and a message
def validate(input):
    if not ('latitud' in input):
        return (False, 'Missing latitud')
    if type(input['latitud']) != float:
        return (False, 'Latitud is not a float')
    if not ('longitud' in input):
        return (False, 'Missing longitud')
    if type(input['longitud']) != float:
        return (False, 'Longitud is not a float')
    if not ('casa' in input):
        return (False, 'Missing casa')
    if type(input['casa']) != int or (input['casa'] != 0 and input['casa'] != 1):
        return (False, 'Expected casa to be 0 or 1')
    if not ('depto' in input):
        return (False, 'Missing depto')
    if type(input['depto']) != int or (input['depto'] != 0 and input['depto'] != 1):
        return (False, 'Expected depto to be 0 or 1')
    if input['casa'] + input['depto'] != 1:
        return (False, 'Expected casa and depto to be opposites')
    if not ('habitaciones' in input):
        return (False, 'Missing habitaciones')
    if type(input['habitaciones']) != int or input['habitaciones'] < 0:
        return (False, 'Expected habitaciones to be a non-negative integer')
    if not ('ambientes' in input):
        return (False, 'Missing ambientes')
    if type(input['ambientes']) != int or input['ambientes'] < 0:
        return (False, 'Expected ambientes to be a non-negative integer')
    if input['ambientes'] < input['habitaciones']:
        return (False, 'Expected ambientes >= habitaciones')
    if not ('garage' in input):
        return (False, 'Missing garage')
    if type(input['garage']) != int or (input['garage'] != 0 and input['garage'] != 1):
        return (False, 'Expected garage to be 0 or 1')
    if not ('banos' in input):
        return (False, 'Missing banos')
    if type(input['banos']) != int or input['banos'] < 0:
        return (False, 'Expected banos to be a non-negative integer')
    if not ('metros_cubiertos' in input):
        return (False, 'Missing metros cubiertos')
    if type(input['metros_cubiertos']) != int or input['metros_cubiertos'] <= 0:
        return (False, 'Expected metros_cubiertos to be a positive integer')
    if not ('metros_totales' in input):
        return (False, 'Missing metros_totales')
    if type(input['metros_totales']) != int or input['metros_totales'] <= 0:
        return (False, 'Expected metros_totales to be a positive integer')
    if input['metros_totales'] < input['metros_cubiertos']:
        return (False, 'Expected metros_totales >= metros_cubiertos')
    if not ('a_estrenar' in input):
        return (False, 'Missing a_estrenar')
    if type(input['a_estrenar']) != int or (input['a_estrenar'] != 0 and input['a_estrenar'] != 1):
        return (False, 'Expected a_estrenar to be 0 or 1')
    if not ('pileta' in input):
        return (False, 'Missing pileta')
    if type(input['pileta']) != int or (input['pileta'] != 0 and input['pileta'] != 1):
        return (False, 'Expected pileta to be 0 or 1')
    if not ('baulera' in input):
        return (False, 'Missing baulera')
    if type(input['baulera']) != int or (input['baulera'] != 0 and input['baulera'] != 1):
        return (False, 'Expected baulera to be 0 or 1')
    return (True, 'JSON has all keys')

def parse(input):
    return np.array([float(input['latitud']),
                     float(input['longitud']),
                     float(input['casa']),
                     float(input['depto']),
                     float(input['habitaciones']),
                     float(input['ambientes']),
                     float(input['garage']),
                     float(input['banos']),
                     float(input['metros_cubiertos']),
                     float(input['metros_totales']),
                     float(input['a_estrenar']),
                     float(input['pileta']),
                     float(input['baulera'])])

def add_features(input):
    return np.array([input[0],
                     input[1],
                     input[2],
                     input[3],
                     input[4],
                     input[5],
                     input[6],
                     input[7],
                     log(input[8]),
                     log(input[9]),
                     input[10],
                     input[11],
                     input[12],
                     input[0]*input[0],
                     input[0]*input[1],
                     input[1]*input[1],
                     input[0]*input[0]*input[0],
                     input[0]*input[0]*input[1],
                     input[0]*input[1]*input[1],
                     input[1]*input[1]*input[1],
                     input[0]*input[0]*input[0]*input[0],
                     input[0]*input[0]*input[0]*input[1],
                     input[0]*input[0]*input[1]*input[1],
                     input[0]*input[1]*input[1]*input[1],
                     input[1]*input[1]*input[1]*input[1],
                     input[0]*input[0]*input[0]*input[0]*input[0],
                     input[0]*input[0]*input[0]*input[0]*input[1],
                     input[0]*input[0]*input[0]*input[1]*input[1],
                     input[0]*input[0]*input[1]*input[1]*input[1],
                     input[0]*input[1]*input[1]*input[1]*input[1],
                     input[1]*input[1]*input[1]*input[1]*input[1],
                     input[0]*input[0]*input[0]*input[0]*input[0]*input[0],
                     input[0]*input[0]*input[0]*input[0]*input[0]*input[1],
                     input[0]*input[0]*input[0]*input[0]*input[1]*input[1],
                     input[0]*input[0]*input[0]*input[1]*input[1]*input[1],
                     input[0]*input[0]*input[1]*input[1]*input[1]*input[1],
                     input[0]*input[1]*input[1]*input[1]*input[1]*input[1],
                     input[1]*input[1]*input[1]*input[1]*input[1]*input[1]])