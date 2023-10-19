# Python Nohub Project

Realizando el Proyect NoHub Crontab  
Servicio de ejecución de procesos en segundo plano, mediante la base de datos, python y crontab linux.

```bash
mkdir /home/python
cd /home/python

git clone https://github.com/elegroag/python-nohub-project.git
mv python-nohub-project nohub
cd nohub

#initializa el environment project
source env/bin/activate

#install dependences
pip3 install -r requirements.txt

#show dependences
pip3 freeze

#optional close environment project
deactivate
```

## RUN PROJECT

```bash
#test script python main process
python3 main.py

crontab –e
crontab –u username –e
```

- Config mysql database.py

```python
cnx = mysql.connector.connect(
    user='root',
    host='$host',
    database='$database',
    password='$password',
    port='3306'
)
return cnx
```

Add command crontab

```sh
* 2 0 * 4 /home/python/env/bin/python3 /home/python/main.py
```

Check crontab run

```bash
crontab –l
```
