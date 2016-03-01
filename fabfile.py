#!/usr/bin/env python

from fabric.api import run, sudo, task, get, put


@task
def cmdrun(arg):
    """ Usage: fab -H server1,server2 cmdrun:"uptime" """
    run(arg)


@task
def sudorun(arg):
    """ Usage: fab -H server1,server2 sudorun:"fdisk -l" """
    sudo(arg)


@task
def download(arg):
    """ Usage: fab -H server1 download:"/path/to/file" """
    get(remote_path=arg, local_path="/tmp/", use_sudo=True)


@task
def upload(arg1, arg2):
    """Usage: fab -H server1,server2 upload:"/localfile","/remote/path/" """
    put(local_path=arg1, remote_path=arg2, use_sudo=True)
