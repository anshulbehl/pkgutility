==========
pkgutility
==========

**pkgutility** is a set of scripts to perform following tasks:

  - Generate package requirements in a single file from all the public repos of a github user.

How to Use
==========
::
    $ sudo yum install python-pip python-devel libxml2-devel libxslt-devel libffi-devel
    $ sudo pip install --pre github3.py
    $ git clone https://github.com/chkumar246/pkgutility.git
    $ cd pkgutility
    $ # python pkgutility.py <your github username> <target github user> <filename: For example: test_requirements.txt>
    $ python pkgutility.py chkumar246 openstack test-requirements.txt


How to Contribute
=================
On Fedora

::
    $ sudo yum install python-pip python-virtualenv
    $ virtualenv project
    $ source project/bin/activate
    $ git clone https://github.com/chkumar246/pkgutility.git
    $ cd pkgutility

Check TODO,
Add the script, test it and send a pull request.

