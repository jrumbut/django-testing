import sys
import os
sys.path = sys.path[1:]
import django
path = os.path.dirname(django.__file__)
print(path)
