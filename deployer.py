import subprocess
cmd1= "git clone https://github.com/akhilvaka2/webapp.git"
data1 = subprocess.run([cmd1], stdout=subprocess.PIPE, shell=True)
cmd2 = "cd webapp && python3 manage.py makemigrations && python3 manage.py migrate && gunicorn main.wsgi --bind 0.0.0.0:8000"
data2 = subprocess.run([cmd2], stdout=subprocess.PIPE, shell=True)
print("data1", data1.stdout)
print("data2", data2.stdout)
