#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

import math

input_string = input('\nEnter IP-network (<network>/<length>): ')

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

print ('\nHost:')
print ('{:<8d} {:<8d} {:<8d} {:<8d}'.format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )
print ("{:08b} {:08b} {:08b} {:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )

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
print( '\nNetwork:' )
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )
print( "{:08b} {:08b} {:08b} {:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )

print( '\nMask:')
print( "/{}".format(length_inp) )
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format(   mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )
print( "{:08b} {:08b} {:08b} {:08b}\n".format( mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )

