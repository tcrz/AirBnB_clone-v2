#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder of
# your AirBnB Clone repo, using the function do_pack.

from fabric.api import local
from datetime import datetime
import os

filename = "web_static" + datetime.now().replace(microsecond=0)\
.strftime("%Y%m%d%H%M%S") + '.tgz'


def do_pack():
    print("Packing web_static to versions/", filename)
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    local("tar -czvf versions/{} web_static".format(filename))
    print("web_static packed: versions/{} -> {}Bytes"\
          .format(filename, os.path.getsize("versions/{}".format(filename))))
