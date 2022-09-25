import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'basico')
print(mymodule_dir)
sys.path.append( mymodule_dir )

import Ejercicios_18_juntos_Menu_y_Clases

Ejercicios_18_juntos_Menu_y_Clases.suma([2, 3])
