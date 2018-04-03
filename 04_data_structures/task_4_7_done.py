#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'


MAC = MAC.replace(':', '')
BIN = bin( int(MAC, 16) )
print( "{:b}".format( int(MAC,16) ) )

HEX = hex( int(BIN, 2) )
print(HEX)

