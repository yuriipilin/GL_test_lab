 
# A solution to technical task for position "junior DevOps engineer"
## List of tasks:
- [x] Create terraform config and make some Google Cloud VMs instances with it
- [x] Create mysql replication between two hosts
- [ ] Run nessus scanner without GUI (***see notes below***)
- [x] process the report from nessus with python to create ansible playbook (***see notes below***)
- [x] Run python script for creation ansible playbook template and than ansible with Jenkins to update Vulnerabilities

# List of hosts involved in:
1. jobserv (35.228.75.189) - Jenkins
2. vpnserv (35.228.5.226)  - Nessus scanner
3. webserver-centos (35.228.32.105) - mysql master 
4. webserver-debi (35.228.71.249) - mysql replicant 


# Files explained:
## All files are placed in the jobserv (35.228.75.189) host
* ansible directory - contains necessary config and generated playbook
* crerate_pattern_ansible.py - a script to generate playbook file using jinja2
* google-cloud-sdk - a tool needed to Terraform integration with Google Cloud
* jinjaTemplates a folder for template patterns nedded to jinja framework
* scanned.csv - report provided by Nessus scanner
* terraform a folder contains Terraform config file to create some VM's
* runNessus folder contains an attempt to run nessus scan with python sekenium webdriver

# Notes:
The firts difficulty was that i haven't managed to run Nessus scanner with CLI(unable),API(unable) and selenium also(unable?)<br>
I just couldn't upload an ssh key for the new scan
create_pattern_ansible script is pretty dummy. It's just hardcoding the package name with vulnerability to create jinja2 pattern.<br>
I havent figured out ho to make it uniq in ONE ansible playbook pattern. Due to luck of time I belive) <br>
To login to Google Cloud host please find the login info inside the answer to technical task email