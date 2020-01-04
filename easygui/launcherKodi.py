from easygui import *
from subprocess import call
import sys
import fcntl
pid_file = 'launcher_kodi.pid'

fp = open(pid_file, 'w')
try:
	fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
	while 1:
	    choices = [
		"Enfants", "Parents"
	    ]

	    image = "kodi.png"
	    msg = "Lancement de Kodi"
	    title = "Lanceur"

	    reply = buttonbox(image=image, msg=msg, title=title, choices=choices, cancel_choice='OK')
	    if reply == "Enfants":
		    call(["/home/guillaume/Applications/switch_kodi/kodi_enfants.sh",""])
            if reply == "Parents":
                    call(["/home/guillaume/Applications/switch_kodi/kodi_parents.sh",""])

	    sys.exit(0)
except IOError:
    # another instance is running
    sys.exit(1)
