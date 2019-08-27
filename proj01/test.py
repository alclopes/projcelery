path = 'C:\MyProjects\projCelery\proj01'
import sys
sys.path.append(path)
from proj.tasks import add

r = add.delay(4, 4)
print(r.status)
print(r.result)