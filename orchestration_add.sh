#!/bin/sh
python3 axos_netconf.py --fileip nc_ip.txt --object vlan --action add --fileparameters vlan.yml
python3 axos_netconf.py --fileip nc_ip.txt --object tsp --action add --fileparameters tsp.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ethernet_class_map  --action add --fileparameters ethernet-class-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object policy_map  --action add --fileparameters policy-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ont --action add --fileparameters ont.yml
