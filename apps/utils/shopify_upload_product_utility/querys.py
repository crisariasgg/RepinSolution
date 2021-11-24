from django.db.models import F
import datetime
from apps.import_excel.models import *
# TODOS LOS REGISTROS DONDE LA FECHA ES UN DIA DESPUES
today = PartsAuthority.objects.filter(date=datetime.date.today()) 
future = PartsAuthority.objects.filter(date=datetime.date.today()+datetime.timedelta(days=1)) 


# SOLUCION 1
# ENCUENTRA DIFERENCIA ENTRE ARCHIVO FUTURO CON ARCHIVO PASADO
# MUESTRA LOS RESULTADOS DE LAS NUEVAS PARTES
today = PartsAuthority.objects.filter(date=datetime.date.today()) 
all_parts=[]

for x in today:
    all_parts.append(x.part)
difference = future.exclude(part__in=all_parts)

# SOLUCION 2
# MODIFICACION DEL PRECIO DE COSTO
today = PartsAuthority.objects.filter(date=datetime.date.today()) 
all_cost=[]

for x in today:
    all_cost.append(x.cost)
difference = future.exclude(cost__in=all_cost)


# MODIFICACION DEL PRECIO DE QTY TODO
today = PartsAuthority.objects.filter(date=datetime.date.today()) 
all_cost=[]

for x in today:
    all_cost.append(x.cost)
difference = future.exclude(cost__in=all_cost)





# ===================ELEMENTOS ELIMINADOS=====================
# SOLUCION 1
# MODIFICACION DE LA PARTE
future = PartsAuthority.objects.filter(date=datetime.date.today()+datetime.timedelta(days=1)) 
all_parts=[]

for x in future:
    all_parts.append(x.part)
difference = today.exclude(part__in=all_parts)




# campos adicionales en nueva tabla
#campo de fecha, status(agrego,actualizo,elimino)