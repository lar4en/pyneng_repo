#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
"""

import math
from sys import argv

# input_string = raw_input('\nEnter IP-network (<network>/<length>): ')
input_string = argv[1]

network_inp, length_inp = input_string.split('/')
length_inp = int(length_inp)

# Mask Manipulation
if length_inp:
    mask = 0xFFFFFFFF >> (32 - length_inp )
    mask = mask << (32 - length_inp )
else:
    mask = 0

mod         = [mask,0,0,0]
mask_octets = [   0,0,0,0]
for i in range( len( mask_octets ) ):
    mask_octets[i] = int( math.floor( mod[i] / math.pow(256, 3-i) ) )
    if i < 3:
        mod[i+1]  = mod[i] % math.pow(256, 3-i )

# Network Manipulation
octets_network = network_inp.split('.')
for i in range( len(octets_network) ):
    octets_network[i] = int(octets_network[i])

print( '\nHost:' )
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )
print( "{:08b} {:08b} {:08b} {:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )

network = "{:08b}{:08b}{:08b}{:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3])
network = int(network, 2)
network = network >> (32 - length_inp)
network = network << (32 - length_inp)

mod[0] = network
for i in range( len(octets_network) ):
    octets_network[i] = int( math.floor( mod[i] / math.pow(256, 3-i) ) )
    if i < 3:
        mod[i+1] = mod[i] % math.pow(256, 3-i)

# OUTPUT
print( '\nNetwork:')
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )
print( "{:08b} {:08b} {:08b} {:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )

print( '\nMask:' )
print( "/{}".format(length_inp) )
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format(   mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )
print( "{:08b} {:08b} {:08b} {:08b}\n".format( mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )

