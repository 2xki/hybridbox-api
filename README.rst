==================================================
hybridbox-api by `2xki <https://github.com/2xki>`_
==================================================
|

Description
===========
A small python package that can be usefull to interact with a A1 (Telekom Austria) Hybridbox Router. Tested with Software version: V100R001C22B026SP03

Bindings for hybridbox-api
==========================

::

    import hybridbox

    myRouter = hybridbox.Session(username='admin', password='P4ssword').login()
    myRouter.turn5gon()
    myRouter.turn5goff()
    myRouter.turn2gon()
    myRouter.turn2goff()
    myRouter.logout()

::

    myRouter.reboot() # note that reboot logs you out


Installation
============
**Dependencies:**

- requests

**pre installed:**

- base64
- hashlib
- re
- json

::

    sudo python setup.py install

License
=======

``hybridbox-api`` is released under the 3-clause BSD license, see ``LICENSE``
for details.
