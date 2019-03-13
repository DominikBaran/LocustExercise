# Documentation:
https://docs.locust.io/en/latest/index.html

# Usage 
1. To intall:
  a) use docker to install container from the docker.hub: https://cloud.docker.com/u/dominikbaran08/repository/docker/dominikbaran08/locust
  b) use documentation page and python/pip to instal locust manually
  
2. To run:
  a) to run Locust with GUI locally on your machine use command: locust -f locust_files/my_locust_file.py --host=http://example.com 
  b) to run Locust without GUI locally on your machine use command: locust -f locust_files/my_locust_file.py --no-web -c 1000 -r 100
  c) alternatywely you could run Locust in the master/slave mode. Please use command: 
    *) to run master: locust -f my_locustfile.py --master
    **) to run agent/slave: locust -f my_locustfile.py --slave --master-host=host_ip_address

