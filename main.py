#main

import sys
import json
from database import Db
from procesador import execCmd;
import logging
import threading

def main():
    try:
        _db = Db()
        rows = _db.readQuery() 
        threads = list()
        for row in rows:
            filename = './logs/{0}.txt'.format(row['usuario'])
            logging.basicConfig(
                datefmt='%d/%m/%Y %I:%M:%S %p',
                filename=filename, 
                level=logging.INFO, 
                format='%(levelname)s | %(asctime)s | %(message)s'
            )
            comando = ' '.join([row['ps'], row['linea_comando']]) 
            x = threading.Thread(target=execCmd, args=(comando, row['id'],  _db, logging))
            print('Hilo run')
            threads.append(x)
            x.start()
            
        for index, thread in enumerate(threads):
            print(f"Result : before joining thread {index}.", )
            thread.join()
            print(f"Result : thread {index} done")
            
    except Exception as e: 
        print('Error main: %s' % e, file=sys.stderr)

if __name__ == '__main__':
    main()
    