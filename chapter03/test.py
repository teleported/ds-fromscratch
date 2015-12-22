#!/usr/bin/python

import matplotlib            
import matplotlib.pyplot as plt
# Print the default backend
print matplotlib.rcParams['backend']
# Another way to print the default backend
print plt.get_backend()
# List the backends
print matplotlib.rcsetup.interactive_bk
# List the backends
print matplotlib.rcsetup.non_interactive_bk
# List the backends
print matplotlib.rcsetup.all_backends
