#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Задание 4.3

(Задача на основе примеров в разделе)

В этой задаче нельзя использовать условие if.

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk),
  * пример текста запроса: 'Enter interface mode (access/trunk): '
* номере интерфейса (тип и номер, вида Gi0/3)
  * пример текста запроса: 'Enter interface type and number: '
* номер VLANа (для режима trunk будет вводиться список VLANов)
  * пример текста запроса: 'Enter vlan(s): '

В зависимости от выбранного режима, на стандартный поток вывода,
должна возвращаться соответствующая конфигурация access или trunk
(шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса,
а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_4_3.py
Enter interface mode (access/trunk): access
Enter interface type and number: Fa0/6
Enter vlan(s): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_4_3.py
Enter interface mode (access/trunk): trunk
Enter interface type and number: Fa0/7
Enter vlan(s): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
"""

access_template = [' switchport mode access',
                   ' switchport access vlan %s',
                   ' switchport nonegotiate',
                   ' spanning-tree portfast',
                   ' spanning-tree bpduguard enable']

trunk_template = [' switchport trunk encapsulation dot1q',
                  ' switchport mode trunk',
                  ' switchport trunk allowed vlan %s']

import re

interface_template = {
    'access': access_template,
    'trunk': trunk_template
}

interface_mode = raw_input('Enter interface mode (access/trunk): ')
interface_number = raw_input('Enter interface type and number: ')
vlans = raw_input('Enter vlan(s): ')

number_string  = interface_number[re.search("\d", interface_number).start()::]
inttype_string = interface_number[0:re.search("\d", interface_number).start()].lower() 

if inttype_string.startswith('f'):
    inttype_string = 'FastEthernet'
elif inttype_string.startswith('g'):
    inttype_string = 'GigabitEthernet'
elif inttype_string.startswith('t'):
    inttype_string = 'TenGigabitEthernet'
else:
    inttype_string = 'Ethernet'

if type( interface_template.get(interface_mode) ) is list:
    result = "\ninterface " + inttype_string + number_string + "\n"
    commands = '\n'.join( interface_template.get(interface_mode) ) % str(vlans)
    result = result + commands + '\nend\n'
else:
    result = '\nUnknown interface mode \'{}\'\n'.format(interface_mode)

print result


