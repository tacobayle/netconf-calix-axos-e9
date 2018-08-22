#!/bin/sh
python3 axos_netconf.py --fileip nc_ip.txt --object ont --action delete --fileparameters ont.yml
python3 axos_netconf.py --fileip nc_ip.txt --object policy_map  --action delete --fileparameters policy-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object ethernet_class_map  --action delete --fileparameters ethernet-class-map.yml
python3 axos_netconf.py --fileip nc_ip.txt --object tsp --action delete --fileparameters tsp.yml
python3 axos_netconf.py --fileip nc_ip.txt --object vlan --action delete --fileparameters vlan.yml
