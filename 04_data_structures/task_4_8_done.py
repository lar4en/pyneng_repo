#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1/22'

import math

input_string = input('\nEnter IP-network (<network>/<length>): ')

network_inp, length_inp = input_string.split('/')

octets_network = network_inp.split('.')
for i in range( len(octets_network) ):
    octets_network[i] = int(octets_network[i])

print( '\nNetwork:' )
print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )
print( "{:08b} {:08b} {:08b} {:08b}".format( octets_network[0], octets_network[1], octets_network[2], octets_network[3]) )

print( '\nMask:' )
print( "/{}".format(length_inp) )

if int(length_inp):
    mask = 0xFFFFFFFF >> (32 - int(length_inp) )
else:
    mask = 0
mask = int("{:032b}".format(mask)[::-1], 2)

mod         = [mask,0,0,0]
mask_octets = [   0,0,0,0]
for i in range( len( mask_octets ) ):
    mask_octets[i] = int( math.floor( mod[i] / math.pow(256, 3-i) ) )
    if i < 3:
        mod[i+1]  = mod[i] % math.pow(256, 3-i )

print( '{:<8d} {:<8d} {:<8d} {:<8d}'.format(   mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )
print( "{:08b} {:08b} {:08b} {:08b}\n".format( mask_octets[0], mask_octets[1], mask_octets[2], mask_octets[3] ) )


