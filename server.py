# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:22:24 2017

@author: Administrator
"""
#
#import socket,time
#import threading
#
# def tcplink(sock,addr):
#    print('Accept new connection from {}:{}...'.format(addr,addr))
#    sock.send(b'Welcome!')
#    while True:
#        data = sock.recv(1024)
#        time.sleep(1)
#        if not data or data.decode('utf-8') == 'exit':
#            break
#        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#    sock.close()
#    print('Connection from %s:%s closed.' % addr)
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1',8899))
# s.listen(5)
#print('Waiting for connecting...')
#
#
# while True:
#    sock,addr = s.accept()
#    t=threading.Thread(target=tcplink,args=(sock,addr))
#    t.start()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# echo_server.py
import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    print(addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 8899))
s.listen(5)
print('Waiting for connection..')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
