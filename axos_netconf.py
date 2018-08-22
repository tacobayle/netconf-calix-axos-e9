from ncclient import manager
import argparse
from nb_ip import string_is_ip
import os
from axos_netconf_xml import *
#
# print help
#
laction = ['show', 'add', 'delete']
lobject = ['vlan', 'tsp', 'ont', 'ethernet_class_map', 'policy_map']
print('--fileip needs to define a file with a list of IP addresses - one IP per line')
print('--username username can be used to specify a username, if not, it will default to sysadmin')
print('--password password can be used to specify a password, if not, it will default to sysadmin')
print('--object defines an object to interact with: ' + str(lobject))
print('--action defines an action: ' + str(laction) + ', if not, it will default to show')
print('--fileparameters defines a file which contains a list of parameters related to an object')
print('--filelog needs to define a file for log')
print()
print('-'*50)
print()
#
# Define all the variables
#
parser = argparse.ArgumentParser("convert")
parser.add_argument("--fileip", help="fileip needs to define a file with a list of IP addresses - one IP per line", required=True)
parser.add_argument("--username", help="Username of the chassis", required=False)
parser.add_argument("--password", help="Password of the chassis", required=False)
parser.add_argument("--object", help="defines an object to interact with", required=True)
parser.add_argument("--action", help="object needs to define an object", required=True)
parser.add_argument("--fileparameters", help="fileparameters needs to define a file with a list of parameters related to the object", required=False)
#parser.add_argument("--filelog", help="filelog needs to define a file for log", required=True)
args = parser.parse_args()
#
if not args.username:
  username = 'sysadmin'
else:
  username = args.username
#
if not args.password:
  password = 'sysadmin'
else:
  password = args.password
#
fileip = args.fileip
if not os.path.exists(fileip):
  print('file ' + fileip + 'does not exist')
  print('*'*50 + ' !!! ERROR !!! ' + '*'*50)
  exit()
#
object = args.object
if object not in lobject:
  print('object not supported')
  print('*'*50 + ' !!! ERROR !!! ' + '*'*50)
  exit()
#
action = args.action
if action not in laction:
  print('action not supported')
  print('*'*50 + ' !!! ERROR !!! ' + '*'*50)
  exit()
else:
  classxml = eval('nc_' + object + '()')
if action == 'add' or action == 'delete':
  fileparameters = args.fileparameters
  if not os.path.exists(fileparameters):
    print('file ' + fileparameters + 'does not exist')
    print('*'*50 + ' !!! ERROR !!! ' + '*'*50)
    exit()
  classnetconf = nc_common()
  classnetconf.ymlfile = fileparameters
  classxml.ymldata = classnetconf.loadymlfile()
  jinjafile = 'xmljinja2/' + action + '_' + object + '.j2'
  classnetconf.file = jinjafile
  classnetconf.vars = classxml.loadparam()
  if action == 'add':
    xml = classnetconf.add()
  if action == 'delete':
    xml = classnetconf.delete()
#
#
#
with open(fileip, 'r') as f:
  for ip in f:
    print('OLT ip is: ' + ip.strip('\n'))
    print('')
    if not string_is_ip(ip.strip('\n')):
      print('*'*50 + ' !!! ERROR !!! ' + '*'*50)
    else:
      with manager.connect(host=ip.strip('\n'), port=830, username=username, password=password, hostkey_verify=False) as m:
        if action == 'add' or action == 'delete':
          print('Request is:')
          print(xml)
          print('-'*20)
          print('')
          output = m.edit_config(target='running', config=xml)
          print('Response is:')
          print(output)
        if action == 'show':
          tup1 = ('subtree', classxml.show_xml)
          print('Request is:')
          print(tup1)
          print('-'*20)
          print('')
          output = m.get_config(source='running', filter=tup1).data_xml
          print('Response is:')
          print(output)
    print('-'*30)
    print('')
