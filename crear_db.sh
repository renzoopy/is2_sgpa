sudo service postgresql start
sudo su - postgres -c "createuser -s sgpa"
sudo -u postgres psql -c "ALTER USER sgpa WITH SUPERUSER;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sgpa;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO sgpa;"
sudo -u postgres psql -c "CREATE DATABASE sgpa;"
sudo -u postgres -i psql --command "DROP ROLE IF EXISTS admin_proyecto; CREATE ROLE admin_proyecto superuser;";
#sudo -u postgres -i dropdb --if-exists sgpa1; createdb sgpa1;
#pipenv shell && \
#python3 manage.py migrate --run-syncdb

#esto pongo en build desarrollo  