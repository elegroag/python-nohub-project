# Python Nohub Project

Realizando el Proyect NoHub Crontab  
Servicio de ejecución de procesos en segundo plano, mediante la base de datos, python y crontab linux.

```bash
mkdir /home/python
cd /home/python

git clone https://github.com/elegroag/python-nohub-project.git
mv python-nohub-project nohub
cd nohub

#version de python
python3 -V

#install venv
sudo apt-get install python3.10-venv

#the env create
python3 -m venv env

#the environment initialize project
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

Config mysql database.py

Create .env file local

```sh
MYSQL_USER= ...
MYSQL_PASSWORD= ...
MYSQL_HOST= ...
MYSQL_PORT= ...
MYSQL_DATABASE= ...
```

Add command crontab

```sh
* 2 0 * 4 /home/python/env/bin/python3 /home/python/main.py
```

Check crontab run

```bash
crontab –l
```

Create SQL - DML

```sql
-- CREATE TABLES
CREATE TABLE comando_estructuras (
  id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  procesador CHAR(10) DEFAULT NULL,
  estructura VARCHAR(255) DEFAULT NULL,
  variables VARCHAR(200) DEFAULT NULL,
  tipo VARCHAR(45) DEFAULT NULL,
  sistema VARCHAR(45) DEFAULT NULL,
  env CHAR(1) DEFAULT '2',
  descripcion VARCHAR(255) DEFAULT NULL,
  asyncro TINYINT(1) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE comandos (
  id INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  fecha_runner DATE DEFAULT NULL,
  hora_runner TIME DEFAULT NULL,
  usuario CHAR(6) NOT NULL,
  progreso INT(3) NOT NULL DEFAULT 0,
  estado ENUM('P','F','X','E') NOT NULL DEFAULT 'P',
  proceso CHAR(6) DEFAULT NULL,
  linea_comando TEXT NOT NULL,
  estructura INT(2) NOT NULL,
  parametros VARCHAR(500) NOT NULL,
  resultado VARCHAR(255) DEFAULT '{}',
  KEY comandos_fk (estructura),
  CONSTRAINT comandos_fk
  FOREIGN KEY (estructura)
  REFERENCES comando_estructuras (id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
) ENGINE=InnoDB;


-- ESTADOS =
--    P = Pendiente
--    F = Finalizado
--    X = Cancelado
--    E = Ejecución
```

```sql
-- INSERT ESTRUCTURES
INSERT INTO comando_estructuras (id,procesador,estructura,variables,tipo,sistema,env,descripcion,asyncro) VALUES
(
    1,
    'p7',
    '$PATH/artisan server:send {{servicio}} {{metodo}} {{params}} {{user}} {{sistema}} {{env}} {{comando}}',
    'servicio|metodo|params|user|sistema|env|comando',
    'PHP',
    'SYS',
    '1',
    'Proceso php7 syncrono',
    0
),
(
    3,
    'p7',
    '$PATH/artisan server:send {{servicio}} {{metodo}} {{params}} {{user}} {{sistema}} {{env}} {{comando}}',
    'servicio|metodo|params|user|sistema|env|comando',
    'PHP',
    'SYS',
    '2',
    'Proceso php7 asyncrono',
    1
),
(
    4,
    'python3',
    '$PATH/{{servicio}} {{metodo}} {{params}} {{user}} {{sistema}} {{env}} {{comando}}',
    'servicio|metodo|params|user|sistema|env|comando',
    'PYTHON',
    'SYS',
    '2',
    'Proceso python asyncrono',
    1
),
(
    5,
    'node',
    '$PATH/{{servicio}} {{metodo}} {{params}} {{user}} {{sistema}} {{env}} {{comando}}',
    'servicio|metodo|params|user|sistema|env|comando',
    'NODE',
    'SYS',
    '2',
    'Proceso nodejs asyncrono',
    1
);
```
