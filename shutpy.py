import subprocess
import os
import sys
#Comprobar si es usuario root
if os.geteuid() != 0:
    print('Debes tener privilegios root para este script.')
    sys.exit(1)#Sale del programa
else:
    print('puedes ejecutar el gestor de bateria')
    print("Script in python3 created by asier adell")
op =  input("apagar/reiniciar/suspender/hibernar/ahorro-de-bateria/terminal/salir/cerrar-sesion: ") #Crea la pregunta al usuario
if op == "apagar":
    os.system("init 0")
elif op == "reiniciar":
    os.system("init 6")
elif op == "suspender":
   os.system("pm-suspend")
elif op == "hibernar":
    os.system("sudo pm-hibernate")
elif op == "ahorro-de-bateria":
   os.system("sudo pm-powersave")
elif op == "terminal":
    os.system("sudo /bin/bash")
elif op == "salir":
    sys.exit(1)
elif op == "cerrar-sesion":
    os.system("sudo pkill -KILL -u $USER")
else:
    print("Comando desconocido")



