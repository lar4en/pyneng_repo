#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100,300-305'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300,300-305'

parts = command1.split(' vlan ')
vlans_c1 = parts[1].split(',')

parts = command2.split(' vlan ')
vlans_c2 = parts[1].split(',')

vlans_c1 = set(vlans_c1)
vlans_c2 = set(vlans_c2)

common_vlans = vlans_c1.intersection( vlans_c2 )

print( common_vlans )


