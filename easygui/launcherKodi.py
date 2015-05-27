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
		"OK"
	    ]

	    image = "kodi.png"
	    msg = "Lancement de Kodi"
	    title = "Lanceur"

	    reply = buttonbox(image=image, msg=msg, title=title, choices=choices, cancel_choice='OK')
	    if reply == "OK":
		    call(["kodi",""])
	    sys.exit(0)
except IOError:
    # another instance is running
    sys.exit(1)
