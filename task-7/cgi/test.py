#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

a = cgi.FieldStorage()
cmd = a.getvalue("s")

if "kubectl" in cmd:
	output = subprocess.getoutput("sudo "+cmd+" --kubeconfig admin.conf")
else:
	output = subprocess.getoutput("sudo "+cmd)
print(output)
