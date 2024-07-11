#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

from fabric.api import env, put, run
import os

env.hosts = ['xx-web-01', 'xx-web-02']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.isfile(archive_path):
        return False

    # Extract the filename without the directory path
    archive_filename = os.path.basename(archive_path)

    # Extract the filename without the extension
    archive_filename_no_ext = archive_filename.split(".")[0]

    # Upload the archive to the /tmp/ directory of the web server
    if put(archive_path, "/tmp/{}".format(archive_filename)).failed:
        return False

    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    if run("mkdir -p /data/web_static/releases/{}/".format(archive_filename_no_ext)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, archive_filename_no_ext)).failed:
        return False

    # Delete the archive from the web server
    if run("rm /tmp/{}".format(archive_filename)).failed:
        return False

    # Move contents of the unzipped folder to the right location
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_filename_no_ext, archive_filename_no_ext)).failed:
        return False

    # Remove the now empty web_static directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(archive_filename_no_ext)).failed:
        return False

    # Delete the symbolic link /data/web_static/current from the web server
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Create a new symbolic link /data/web_static/current on the web server, linked to the new version of your code
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_filename_no_ext)).failed:
        return False

    return True
