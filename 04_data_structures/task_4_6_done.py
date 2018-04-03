#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

words = ospf_route.split()

if words[0] == 'O':
    proto = 'OSPF'
else:
    proto = 'Other'

for i in range( len(words) ):
    words[i] = words[i].replace( '[', '')
    words[i] = words[i].replace( ']', '')
    words[i] = words[i].replace(',', '')
    words[i] = words[i].replace(',', '')

output = """Protocol:\t\t{:20}
Prefix:\t\t\t{:20}
AD/Metric:\t\t{:20}
Next-Hop:\t\t{:20}
Last update:\t\t{:20}
Outbound Interface:\t{:20}""".format(proto, words[1], words[2], words[4], words[5], words[6])


print(output)


