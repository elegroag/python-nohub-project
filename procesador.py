#procesador
import os
from time import sleep
from subprocess import run, TimeoutExpired

def execCmd(cmd, _id, _db, logging):
    try:
        _db.updateQuery(_id, 'P')
        print(cmd)
        p = run(cmd.split(' '), 
            capture_output=True, 
            encoding="utf-8", 
            timeout=28800
        )
        _db.updateQuery(_id, 'F')
        logging.info(f'Comando {_id} P-OK | {p}') 
        sleep(10)
        return p
    except TimeoutExpired as ter:
        _db.updateQuery(_id, 'X')
        logging.error(f'Comando {_id} P-Fail | {ter}') 
        sleep(10)
        return 'Error ps: {0}'.format(err)
    except Exception as err:
        _db.updateQuery(_id, 'X')
        logging.error(f'Comando {_id} P-Fail | {err}') 
        sleep(10)
        return 'Error ps: {0}'.format(err)
    except OSError as os_err:
        _db.updateQuery(_id, 'X')
        logging.error(f'Comando {_id} P-Fail | {os_err}') 
        sleep(10)
        return 'Error ps: {0}'.format(err)
    else:
        logging.error(f'Comando {_id} P-Fail') 
        _db.updateQuery(_id, 'X')
        sleep(10)
        return "Other Error";
