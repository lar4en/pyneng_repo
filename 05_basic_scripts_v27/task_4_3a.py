#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Задание 4.3a

В этой задаче нельзя использовать условие if.

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

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

question_variants = {
    'access': 'Enter VLAN number: ',
    'trunk':  'Enter allowed VLANs: '
}

interface_mode   = raw_input('Enter interface mode (access/trunk): ')

if type( interface_template.get(interface_mode) ) is list:
    interface_number = raw_input('Enter interface type and number: ')
    vlans            = raw_input( question_variants.get(interface_mode) )
    
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
    
    result = "\ninterface " + inttype_string + number_string + "\n"
    commands = '\n'.join( interface_template.get(interface_mode) ) % str(vlans)
    result = result + commands + '\nend\n'
    print result
else:
    print '\nUnknown interface mode \'{}\'!\n'.format(interface_mode)

