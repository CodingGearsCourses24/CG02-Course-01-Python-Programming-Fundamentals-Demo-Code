""" Where does the import look/search
Locations:
    1. Current working directory
    2. Paths defined in "PYTHONPATH" environmental variable (if declared)
    3. Installation-dependent default paths (controlled by site module)

    sys.path
"""

import mysimplemodule

print(mysimplemodule.my_message())




