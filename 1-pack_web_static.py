#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated.
        None: If the archive hasn't been generated.
    """
    # Create the versions folder if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the archive name
    now = datetime.now()
    archive_name = f"versions/web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"

    # Create the archive
    command = "tar -czvf {} web_static".format(archive_name)
    result = local(command)

    # Check if the archive was created successfully
    if result.failed:
        return None
    return archive_name
