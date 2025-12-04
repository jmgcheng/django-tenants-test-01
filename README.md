# django-tenants-test-01
```
Python 3.13.7
Django==5.2.8
```

# clone
```
git clone git@github.com:jmgcheng/django-tenants-test-01.git
```

# conda
```
conda create -n venv_conda_3.13 python=3.13 -y
conda env list
conda activate venv_conda_3.13
```

# first setup
```
pip install -r requirements.txt
setup postgresdb below because settings.py already use postgres with specific db, user, pass
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# db

```
psql -U postgres
CREATE DATABASE django_tenant_test_db;
CREATE USER django_tenant_test_user WITH PASSWORD 'thepass';
GRANT ALL PRIVILEGES ON DATABASE django_tenant_test_db TO django_tenant_test_user;
ALTER DATABASE django_tenant_test_db owner to django_tenant_test_user;
```

# django shell

```
python manage.py shell
from customers.models import Client, Domain
from datetime import date

# Create the "public" tenant
public = Client(schema_name='public', name='Public Tenant', paid_until=date(2030,1,1), on_trial=False)
public.save()

Domain(domain='localhost', tenant=public, is_primary=True).save()

# Create a customer tenant
client1 = Client(schema_name='client1', name='Client 1', paid_until=date(2030,1,1), on_trial=True)
client1.save()

Domain(domain='client1.localhost', tenant=client1, is_primary=True).save()
```

# hosts file

```
127.0.0.1   client1.localhost
```

# db check

```
\dt

# schema = namespace
\dn

\dt client1.*
SELECT * FROM client1.dashboard_product;
SELECT * FROM client1.mainapp_product;
```

# notes

- client/tenant can have multiple domain
- you need to manually crud tenant and domain
- visit http://localhost:8000 for your company
- visit http://client1.localhost:8000 for specific tenant
