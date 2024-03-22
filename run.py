import subprocess
import os
import sys

def setup_venv():
    python_executable = 'python3'
    subprocess.check_call([python_executable,'-m' ,'pip', 'install', '-r', 'requirements.txt'])
    return python_executable

def run_script_in_venv(python_executable, script_path):
    print(f"Running script {script_path} in the virtual environment...")
    subprocess.check_call([python_executable, script_path])

if __name__ == "__main__":
    python_executable = setup_venv()
    working_scripts = [
        'example.py',
        'mosley.py',
        'pklein.py',
    ]
    for script_path in working_scripts:
        run_script_in_venv(python_executable, script_path)
