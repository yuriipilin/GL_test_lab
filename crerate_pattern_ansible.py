from jinja2 import Environment, FileSystemLoader
import csv
import re
import os

#delete ansible configs if exists for propper work of 'a' write mod
#try:
#    os.remove('/home/yuriypilin/ansible/fixVulnerabilities.yml')
#    os.remove('/home/yuriypilin/ansible/hosts')
#except OSError:
#    pass


list_values =   []
list_of_hosts = []
list_of_names = []
list_of_lists = []
fixed_list_of_packages = []
raw_list_of_packages = []



rdr= csv.reader( open("/home/yuriypilin/scanned.csv", "r" ) )

#do a list obj from cvs file
for line in rdr:
   list_of_lists.append(line)

#delete first empty string
list_of_lists = list_of_lists[1:]

#do a list consisted of packages need to be updated with other data
for lists in list_of_lists:
   raw_list_of_packages.append(lists[2])

#delete new lines characters
raw_list_of_packages = map(lambda s: s.strip(), raw_list_of_packages)

#split list of ackages with other data for easier manipulation
templist = []
for word in raw_list_of_packages:
    word = word.split(":")
    templist.extend(word) 

# dummy regex and slice to find packets need to be updated
for string in templist:
    if re.search(r'\d$', string):
        fixed_list_of_packages.append(string[:string.index('_')])

#delete whitespaces before text
fixed_list_of_packages = list(map(lambda s: s.strip(), fixed_list_of_packages))

#creating list of names(CVE) used for 'name' field in ansible playbook
for lists in list_of_lists:
   list_of_names.append(lists[0])

#to enumerate hosts names in ansible config
host_number = 1

#create list of host to be updated
for lists in list_of_lists:
   list_of_hosts.append(lists[1])

#create file containins list of host needs to be updated
with open('/home/yuriypilin/ansible/hosts', 'w') as hosts_file:
   for host in list_of_hosts:
      pattern = 'webserver_' + str(host_number) + ' ansible_host=' + str(host) + '\n' 
      host_number = host_number + 1
      hosts_file.write(pattern)

env = Environment(loader=FileSystemLoader('/home/yuriypilin/jinjaTemplates'))
template = env.get_template('template')

# create ansible playbook template
#playbook = jinja2.Template("- name: Fix {{name}} \n  apt: \n     name: {{pack}}     \n     state: present \n \n ") 

 
config = template.render(name=list_of_names[0], package=fixed_list_of_packages[0]) 
with open('/home/yuriypilin/ansible/fixVulnerabilities.yml', 'w') as file:
   file.write(config)

#TONS of prints func for debug has been here
