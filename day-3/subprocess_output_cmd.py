import subprocess

p1 = subprocess.run('ls -ltr', capture_output=True, text=True, shell=True)

print(p1.stdout)