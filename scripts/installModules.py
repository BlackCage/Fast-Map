import os
import time
import subprocess
try:
    from alive_progress import alive_bar
except:
    FNULL = open(os.devnull, 'w')
    subprocess.run(['pip', 'install', 'alive-progress'], stdout=FNULL, stderr=subprocess.STDOUT)
from alive_progress import alive_bar

modules = ['json', 'signal', 'socket', 'colorama', 'requests', 'argparse', 'python-nmap']

with alive_bar(8, force_tty=True, dual_line=True, title='Downloading') as bar:
    for i in modules:
        FNULL = open(os.devnull, 'w')
        bar.text = f'Installing module {i}, this may take a while.'
        subprocess.run(['pip', 'install', f'{i}'], stdout=FNULL, stderr=subprocess.STDOUT)
        time.sleep(0.1)
        bar()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')