#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

from fabric.api import *
from datetime import datetime
import os

filename = "web_static_" + datetime.now().replace(microsecond=0)\
            .strftime("%Y%m%d%H%M%S") + ".tgz"

env.hosts = ["ubuntu@34.237.53.89", "ubuntu@34.138.32.10"]


def do_pack():
    """Fabric function"""
    print("Packing web_static to versions/{}".format(filename))
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    tgz_path = "versions/" + filename
    local("tar -cvzf {} web_static".format(tgz_path))
    print("web_static packed: {} -> {}Bytes".format(
        tgz_path, os.path.getsize("versions/{}".format(filename))))
    return tgz_path


def do_deploy(archive_path):
    """Fabric deploy function, takes a file path as argument"""
    if not os.path.isfile(archive_path):
        return False
    # remove .tgz extension
    filename = archive_path.replace("versions/", "")
    # remove versions folder path
    folder_name = filename.replace(".tgz", "")
    put(archive_path, "/tmp", use_sudo=True)
    run("mkdir -p /data/web_static/releases/{}".format(folder_name))
    run("tar -xzf /tmp/{} --strip-components 1 -C \
        /data/web_static/releases/{}".format(filename, folder_name))
    run("rm /tmp/{}".format(filename))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current".
        format(folder_name))
    return True


def deploy():
    """Fabric function for full distribution of archices on servers"""
    path = do_pack()
    r = do_deploy(path)
    return r


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    archives = sorted(os.listdir('versions'), reverse=True)
    # print(type(number))
    if number <= 1:
        number = 1
    for tgz in archives[number:]:
        tgz_path = 'versions/' + tgz
        local("rm versions/{}".format(tgz))
    for tgz in archives[number:]:
        tgz_path = 'versions/' + tgz
        run("rm -rf /data/web_static/releases/{}"
            .format(tgz.replace(".tgz", "")))
