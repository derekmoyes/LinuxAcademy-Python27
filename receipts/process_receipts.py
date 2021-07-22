import glob
import os
import shutil
import json
#import re

try:
  os.mkdir("./processed")
except OSError:
  print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.glob('./new/receipt-[0-9]*.json')
  # only process even numbered receipts 
#receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') 
#  if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0 

# Iterate over the receipts 
for path in receipts:
  with open(path) as f:
  # read content and tally a subtotal 
    content = json.load(f)
    subtotal += float(content['value'])

  # mv the file to the processed directory 
  # one way using split
  #   name = path.split('/')[-1]
  #   destination = "./processed/%s" % name
  # another way using object methods
  destination = path.replace('new', 'processed')
  shutil.move(path, destination)

  # print that we processed the file 
  print("moved '%s' to '%s'" % (path, destination))

# Print the subtotal of all processed receipts 
print("Receipt subtotal: $%.2f" % subtotal)
