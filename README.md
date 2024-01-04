>Please use branch ```apache-config``` for this task that already exist in your forked repository after you has been started task
# apache-conf

Create Jinja2 template for Apache configuration.

Create _vhosts.j2_ template, that will return similar Apache config:
```bash
<VirtualHost *:80>
  ServerName www.domain.tld
  DocumentRoot /www/domain
  ServerAdmin www-admin@foo.example.com
  <Directory "/usr/local/httpd/htdocs">
     AllowOverride All
     Options Indexes FollowSymLinks
     Order allow,deny
     Allow from all
  </Directory>
</VirtualHost>
```
Script _conf.py_ should return _vhosts.conf_, that contain multiple VirtualHosts and takes data from  _data.yml_.


Your solution should contain  the following files:
- _vhosts.j2_
- _data.yml_
- _conf.py_
- generated _vhosts.conf_ 
