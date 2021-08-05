#!/usr/bin/env python
"""
kill the running process listening on a given port

Python's standard library comes with an HTTP server that you can use to start a 
server listening on a port (5500 in this case) with this line:

$ python -m SimpleHTTPServer 5500

Use a separate terminal window/tab to test out your script to kill that 
process.
"""
import argparse
import textwrap
import subprocess
import os
from sys import exit

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter, 
    description=__doc__)
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port

try:
    output = subprocess.check_output(['lsof', '-n', "-i4TCP:%s" % port])
except subprocess.CalledProcessError:
    print("No process listening on port %s" % port)
    exit(1)
else:
    listening = None

    for line in output.splitlines():
        if "LISTEN" in line:
            listening = line
            break

    if listening:
        # PID is the second column in the output
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print("Killed process %s" % pid)
    else:
        print("No process listening on port %s" % port)
        exit(1)
