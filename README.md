Django/Celery Scl Demo
======================

This is the demo site I've created for playing with software collections.

How-To:  Install CentOS/RHEL 7

Enable epel

install rabbitmq-server

systemctl start rabbitmq-server

Enable my scl stack:

https://copr.fedorainfracloud.org/coprs/pcreech17/pulp-scl-demo/

Download the .repo file from the Epel7 button

Heres the fun part:

Install
=======

yum install pcreech17-pulp-scl-demo-python35-python-django pcreech17-pulp-scl-demo-python35-python-celery tmux

Enable scl for bash (IMPORTANT!)
=======

scl enable pcreech17-pulp-scl-demo-python35 bash

If you want to make life easy:
======
Start a tmux session and split screens (AFTER enabling the scl and running bash)
    otherwise you'll need multiple terminals, or daemonizing the celery worker... but then you don't get realtime output!


start the celery worker
====
From the code root dir:

celery -A addtask.tasks worker --loglevel=info

Start the django devel webserver:
======
From the code root dir:

./manage.py runserver 0.0.0.0:8000 

Now, make some sample requests!
======

http://192.168.x.x:8000/addtask/add/2/2/

