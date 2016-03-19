#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'


'''
origin blog from Mark McLoughlin

https://blogs.gnome.org/markmc/2013/06/04/async-io-and-python/

测试通过一台ubutun 14.04 服务器运行ncat命令监听端口12345.
root@localhost:~# ncat -l 12345 | dd of=/dev/null

默认ubuntu 14.04没有ncat命令,需要通过apt安装nmap包,其中包含ncat命令

root@localhost:~# apt-get install nmap

'''

import socket

sock = socket.socket()
sock.connect(('192.168.38.2', 12345))
sock.send('foo\n' * 10 * 1024 * 41024)


