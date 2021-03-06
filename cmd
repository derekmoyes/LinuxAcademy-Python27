#!/usr/local/bin/python
# Python 2.7 Scripting for System Administrators

import subprocess

try:
  output = subprocess.check_output(
    'ls fake.txt',
    stderr=subprocess.STDOUT
    )
except OSError as err:
  print("Caught OSError")
  output = err
except subprocess.CalledProcessError as err:
  print("Caught CalledProcessError")
  output = err

print(output)
