#!/usr/bin/env python
import os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Add apps and lib directories to PYTHONPATH
sys.path = [
    os.path.join(ROOT, 'apps'),
    os.path.join(ROOT, 'lib'),
    # add /lib/* paths here for submodules
] + sys.path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suwakiorg.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



#from django.core.management import execute_manager
#import imp
#try:
#    imp.find_module('settings') # Assumed to be in the same directory.
#except ImportError:
#    import sys
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
#    sys.exit(1)

#import settings

#if __name__ == "__main__":
#    execute_manager(settings)
