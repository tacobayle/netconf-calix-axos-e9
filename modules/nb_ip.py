import ipaddress
import socket
#
def string_is_ip(string):
  '''
  check if string is a valid IP
  '''
  try:
    ipaddress.ip_address(socket.gethostbyname(string))
    return True
  except:
    print('!!! Warning !!! ' + string + ': Not a valid IP address')
    return False
#
#
def input_check_ip_default(text, default):
  '''
  ask for an input and propose a default value
  check if it is a valid IP
  '''
  while True:
    ip = str(input(text + '[' + default + ']: ') or default)
    try:
      ipaddress.ip_address(ip)
      break
    except:
      print('!!! Warning !!! Not a valid IP address')
  return ip
#
#
def input_check_ip_prefix_unique(text,list):
  '''
  ask for an input
  check if it is a valid IP with prefix (not network or broadcast address)
  check if it does not exist in list
  return ip, prefix, netmask, network, list (including the new IP)
  '''
  while True:
    string = input(text)
    try:
      ip = str(ipaddress.IPv4Interface(string)).split('/')[0]
      prefix = str(ipaddress.IPv4Interface(string)).split('/')[1]
      netmask = str(ipaddress.IPv4Interface(string).with_netmask).split('/')[1]
      network = str(ipaddress.IPv4Interface(string).network)
      if (prefix == '32' or
         ip == str(ipaddress.IPv4Network(network).network_address) or
         ip == str(ipaddress.IPv4Network(network).broadcast_address)):
        foo
      else:
        if ip not in list:
          list.append(ip)
          break
        else:
          print('!!! Warning !!! IP already used')
    except:
      print('!!! Warning !!! Not a valid IP address with a prefix like: "192.168.1.1/24"')
  return ip, prefix, netmask, network, list
#
#
def input_check_gw_default(text, default, network):
  '''
  ask for an input and propose a default value
  check if it belongs to the appropriate subnet
  return IP
  '''
  while True:
    string = str(input(text + ', [' + default + ']: ') or default)
    try:
      lhosts = list(ipaddress.IPv4Network(network).hosts())
      if ipaddress.ip_address(string) in lhosts:
        break
      else:
        foo
    except:
      print('!!! Warning !!! Not a valid IP address for the gateway, it should belong to: ' + network)
  return string
#
#
def input_check_ip_unique(text,list):
  '''
  ask for an input
  check if it is a valid IP
  check if it does not exist in list
  return ip, list 
  '''
  while True:
    string = input(text)
    try:
      ip = ipaddress.ip_address(string)
      if ip in list:
        print('!!! Warning !!! IP already used')
        foo
      else:
        list.append(ip)
        break
    except:
      print('!!! Warning !!! Not a valid IP address with a prefix like: "192.168.1.1"')
  return ip, list
