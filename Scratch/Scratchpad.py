#!/
#Scratchpad
import sys
import pathlib
if str(pathlib.Path.cwd()).endswith('queue'):
    sys.path.insert(0, pathlib.Path.cwd().parent)
from singly_linked_list import LinkedList

