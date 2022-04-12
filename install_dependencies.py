import os
import sys
import subprocess


subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'])
os.system(f'python3 start_integration.py')
