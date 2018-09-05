# netconf-calix-axos-e9
prequisites:
++ python3 installed
++ python module ncclient installed
pip install ncclient
please checkout the following for more information:
https://github.com/ncclient/ncclient
++ ipaddress python module installed
++ python jinja2 module installed

Main srcript to run is axos_netconf.py

Argurment of the script:
--fileip needs to define a file with a list of IP addresses - one IP per line
--username username can be used to specify a username, if not, it will default to sysadmin
--password password can be used to specify a password, if not, it will default to sysadmin
--object defines an object to interact with: ['vlan', 'tsp', 'ont', 'ethernet_class_map', 'policy_map']
--action defines an action: ['show', 'add', 'delete'], if not, it will default to show
--fileparameters defines a file which contains a list of parameters related to an object
--filelog needs to define a file for log

Examples on how to start the script:

python3 axos_netconf.py --fileip nc_ip.txt --object vlan --action add --fileparameters vlan.yml
python3 axos_netconf.py --fileip nc_ip.txt --object tsp --action add --fileparameters tsp.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ethernet_class_map  --action add --fileparameters ethernet-class-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object policy_map  --action add --fileparameters policy-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ont --action add --fileparameters ont.yml

python3 axos_netconf.py --fileip nc_ip.txt --object ont --action delete --fileparameters ont.yml
python3 axos_netconf.py --fileip nc_ip.txt --object policy_map  --action delete --fileparameters policy-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ethernet_class_map  --action delete --fileparameters ethernet-class-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object tsp --action delete --fileparameters tsp.yml
python3 axos_netconf.py --fileip nc_ip.txt --object vlan --action delete --fileparameters vlan.yml

Examples of Yaml file (--fileparameters):

++ vlan.yml

---
-
  description: netconf-600
  id: 600
  mode: N2ONE
-
  description: netconf-601
  id: 601
  mode: N2ONE
-
  description: netconf-602
  id: 602
  mode: N2ONE
-
  description: netconf-603
  id: 603
  mode: N2ONE
-
  description: netconf-604
  id: 604
  mode: N2ONE
-
  description: netconf-605
  id: 605
  mode: N2ONE
-
  description: netconf-606
  id: 606
  mode: N2ONE
-
  description: netconf-607
  id: 607
  mode: N2ONE
-
  description: netconf-608
  id: 608
  mode: N2ONE
-
  description: netconf-609
  id: 609
  mode: N2ONE
-
  description: netconf-701,702
  id: 701,702
  mode: N2ONE
-
  description: netconf-805-810
  id: 805-810
  mode: N2ONE
-
  description: netconf-905,910-915
  id: 905,910-915
  mode: N2ONE

++ tsp.yml

---
-
  name: netconf_tsp1
  vlan: 601-605,608
-
  name: netconf_tsp2
  vlan: 600,609


++ ethernet-class-map.yml

---
-
  name: netconf-eth-class-map1
  flow:
    -
      index: 1
      description: flow1
      rule:
        -
          index: 1
          description: rule1
          match:
            - any: 'true'
        -
          index: 2
          description: rule2
          match:
            - vlan: 600
        -
          index: 3
          description: rule3
          match:
            - untagged: 'true'
        -
          index: 4
          description: rule4
          match:
            - ethertype: '0x8863'
    -
      index: 2
      description: flow2
      rule:
        -
          index: 1
          description: rule1
          match:
            - pcp: 5
            - vlan: 605
-
  name: netconf-eth-class-map2
  flow:
    -
      index: 1
      description: flow1
      rule:
        -
          index: 1
          description: rule1
          match:
            - vlan: 602


++ policy-map.yml

---
-
  name: netconf_pm_1
  class-map-type: ethernet
  class-map-name: netconf-eth-class-map1
  flow:
    -
      id: 1
      action:
        - set-ctag-pcp: 6
        - set-stag-pcp: 5
    -
      id: 2
      action:
        - add-ctag: 100
-
  name: netconf_pm_2
  class-map-type: ethernet
  class-map-name: netconf-eth-class-map2
  flow:
    -
      id: 1
      action:
        - set-stag-pcp: 6


++ ont.yml

---
-
  id: 1
  description: ontnetconf1
  profile: GP1000X
  serial-number: 478AFA
-
  id: 25
  description: ontnetconf2
  profile: GP1000X
  serial-number: 478AFF
