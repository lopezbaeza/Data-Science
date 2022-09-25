import os

# C://Users/nombre usuario/...
# /home/nombre usuario/...

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'media')

MEDIA_ROOT = os.path.expanduser(mymodule_dir)
#MEDIA_ROOT = os.path.expanduser("~\\git_test\\Data-Science\\media\\")