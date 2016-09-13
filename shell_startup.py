#!/.pyenv/shims/python
# -*- coding: utf-8 -*-
import os, stat, sys
import time
import subprocess

shellfile = sys.path[0] + '/legendary.sh'
st = os.stat(shellfile)
os.chmod(shellfile, st.st_mode | stat.S_IRWXU)
subprocess.call([shellfile])
while True: 
    time.sleep(1)
