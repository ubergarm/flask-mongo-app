flask-mongo-app
===============

A Python Flask Web App Development Skeleton using mongoDB featuring javascript.

I wanted to learn some neat tools so I created this project to tie a few interesting things together.  After you start up the virtual machine, you will be able to query the database which dynamically generates a templated javascript map to view GPS coordinates and information based on zipcodes.

Screenshot
----------
![Screen Shot](./flask-mongo-app-screenshot.png?raw=true)


Try it out!
-----------
*Bring up the virtualmachine and provision the server*

    $ vagrant up

_Point your browser at_

    http://localhost:5000/

_Cleaning up_

    $ vagrant destroy

_If you accidently delete the dir before doing destroy_

    $ VBoxManage list vms
    $ VBoxManage unregistervm flask-app-server –delete

####Requires:
* [Vagrant](http://www.vagrantup.com/) -- `sudo apt-get install vagrant` 1.2.2
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads/) -- `sudo apt-get install virtualbox-4.2`

####Built On:
* [ansible](https://github.com/ansible/ansible/) -- provisioner loaded up first
* [Flask](http://flask.pocoo.org) -- Python microframework web app engine
* [mongoDB](http://mongodb.org) -- noSQL database
* [Flask-PyMongo](http://flask-pymongo.readthedocs.org/en/latest/) -- bridges Flask and PyMongo
* [leafletjs] (http://leafletjs.com/) -- javascript mapping
* [bootstrap] (http://twitter.github.io/bootstrap/) -- pretty css

####TODO:
* Try out some Javascript Charts & Graphs:
    * https://github.com/mbostock/d3/wiki/Gallery
    * http://square.github.io/crossfilter/ 
    * http://bl.ocks.org/tjdecke/5558084
    * http://www.chartjs.org/
    * http://www.flotcharts.org/flot/examples/
* Various Mapping Styles:
    * http://maps.stamen.com/#toner/12/37.7706/-122.3782
* Play with adding an [Nginx](http://wiki.nginx.org/Main) layer on top of Flask


####Issues:
* sometimes have to vagrant ssh && sudo supervisorctl start flask-mongo-app

####Notes:
* bootstrap.sh does a one-time install of ansible to get the ball rolling
* mongodb stores its data files in /var/lib/mongodb/
* mongodb stores its log files in /var/log/mongodb/

####My workflow:
* git config --global user.name 'Your Name'
* git config --global user.email your@email
* git pull
* edit some code
* git add <new files>
* git commit -am 'fixed some bugs'
* git push -u origin master

####Thanks to:
* http://www.pixelmonkey.org/2013/03/13/rapid-web-prototyping-with-lightweight-tools
* http://ryaneshea.com/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku

Contributing
------------

1. Fork it.
2. Create a branch (`git checkout -b my_new_feature`)
3. Commit your changes (`git commit -am "Added Cool Thing"`)
4. Push to the branch (`git push origin my_new_feature`)
5. Open a [Pull Request][1]
6. Enjoy a few plumphelmets while you wait cuz I've never done this before.

[1]: http://github.com/ubergarm/flask-mongo-app/pulls

