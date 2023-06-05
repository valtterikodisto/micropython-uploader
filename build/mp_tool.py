import os
import subprocess

class MicroPythonTool():
    def __init__(self, port):
        self.port = port
        os.environ['AMPY_PORT'] = self.port
        
    def ls(self, path: str):
        result = subprocess.run(['ampy', 'ls', path], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8').splitlines()
    
    def rm(self, path: str):
        subprocess.run(
            ['ampy', 'rm', path],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            check=True
        )
    
    def rmdir(self, path: str):
        subprocess.run(
            ['ampy', 'rmdir', path],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            check=True
        )

    def put(self, src: str, dest: str):
        subprocess.run(
            ['ampy', 'put', src, dest],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            check=True
        )
    
    def run(self, path: str):
        subprocess.run(
            ['ampy', 'run', path],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            check=True
        )
            