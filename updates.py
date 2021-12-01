import os
from time import sleep
import time


#removendo os unzips pra atualizar
#relaxa q no ta apagando as py's.
os.system('rm -rf .source')

os.system('rm -rf cell.py')

os.system('rm -rf info.py')

os.system('rm -rf ss.py')

os.system("rm -rf install.sh'")

os.system('rm -rf ssh')

os.system('git pull');time.sleep(1)

os.system('clear');time.sleep(1)

message = ('VERIFICAÇÃO DE ATUALIZAÇÃO CONCLUÍDA :$')

##############################################

print(message);time.sleep(0.8)