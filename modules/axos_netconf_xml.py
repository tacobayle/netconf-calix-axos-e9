import os
import jinja2
import yaml
#
class nc_ont:
#
  show_xml = '''<base:config xmlns:base="http://www.calix.com/ns/exa/base">
      <base:system>
        <ont xmlns="http://www.calix.com/ns/exa/gpon-interface-base"></ont>
      </base:system>
    </base:config>'''
#
  def loadparam(self):
#    ont_id = []
#    ont_descr = []
#    ont_profile = []
#    ont_sn = []
#    for item in self.ymldata:
#      ont_id.append(item['id'])
#      ont_descr.append(item['description'])
#      ont_profile.append(item['profile'])
#      ont_sn.append(item['serial-number'])
#    ont_vars = {'ont_param': zip(ont_id, ont_descr, ont_profile, ont_sn)}
    ont_vars = self.ymldata 
    return ont_vars
#
class nc_policy_map:
#
  show_xml = '''<base:config xmlns:base="http://www.calix.com/ns/exa/base">
      <base:profile>
        <base:policy-map/>
      </base:profile>
    </base:config>'''
#
  def loadparam(self):
    pm_vars = self.ymldata
    return pm_vars
#
class nc_ethernet_class_map:
#
  show_xml = '''<base:config xmlns:base="http://www.calix.com/ns/exa/base">
      <base:profile>
        <base:class-map/>
      </base:profile>
    </base:config>'''
#
  def loadparam(self):
    ecm_vars = self.ymldata
    return ecm_vars
#
class nc_tsp:
#
  show_xml = '''<base:config xmlns:base="http://www.calix.com/ns/exa/base">
      <base:profile>
        <base:transport-service-profile/>
      </base:profile>
    </base:config>'''
#
  def loadparam(self):
    tsp_name = []
    tsp_vlan_list = []
    for item in self.ymldata:
      tsp_name.append(item['name'])
      vlan_tmp = item['vlan'].split(',')
      tsp_vlan = []
      for data in vlan_tmp:
        if '-' in data:
          vlan_low = int(data.split('-')[0])
          vlan_high = int(data.split('-')[1]) + 1
          for vlan in range(vlan_low,vlan_high):
            tsp_vlan.append(vlan)
        else:
          tsp_vlan.append(data)
      tsp_vlan_list.append(tsp_vlan)
      tsp_vars = zip(tsp_name, tsp_vlan_list)
    return tsp_vars
#
class nc_vlan:
#
  show_xml = '''<base:config xmlns:base="http://www.calix.com/ns/exa/base">
    <base:system>
      <base:vlan/>
    </base:system>
  </base:config>'''
#
  def loadparam(self):
    vlan_yml = self.ymldata
    vlan_vars = []
    for item in vlan_yml:
      vlan_tmp = str(item['id']).split(',')
      for vlan_id in vlan_tmp:
        if '-' in vlan_id:
          vlan_low = int(vlan_id.split('-')[0])
          vlan_high = int(vlan_id.split('-')[1]) + 1
          dictvlan = {}
          for vlan in range(vlan_low,vlan_high):
            dictvlan = {}
            dictvlan['description'] = item['description']
            dictvlan['mode'] = item['mode']
            dictvlan['id'] = vlan
            vlan_vars.append(dictvlan)
        else:
          dictvlan = {}
          dictvlan['description'] = item['description']
          dictvlan['mode'] = item['mode']
          dictvlan['id'] = vlan_id
          vlan_vars.append(dictvlan)
    return vlan_vars
#
class nc_common:
#
  def add(self):
    print(self.vars)
    print(self.file)
    with open(self.file) as j:
      jinja_template = j.read()
      template = jinja2.Template(jinja_template)
      xml = template.render(vars=self.vars)
    j.close
    return xml
#
  def delete(self):
    with open(self.file) as j:
      jinja_template = j.read()
      template = jinja2.Template(jinja_template)
      xml = template.render(vars=self.vars)
    j.close
    return xml
#
  def loadymlfile(self):
    with open(self.ymlfile, 'r') as f:
      datas = yaml.load(f)
    f.close
    return datas
