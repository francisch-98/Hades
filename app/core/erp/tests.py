from config.wsgi import *
from core.erp.models import Type, Employee

# SELECT

# query = Type.objects.all()
# print(query)

# INSERT
# t = Type()
# t.id = 3
# t.name = 'Gerente'
# t.save()

# UPDATE

# t = Type.objects.get(id=1)
# t.name = 'Propietario'
# t.save()

# DELETE
# t = Type.objects.get(pk=3)
# t.delete()

obj = Employee.objects.filter(type_id=1)

for i in Type.objects.filter(name__icontains='pr'):
    print(i.name)6