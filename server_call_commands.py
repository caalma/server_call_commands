#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# requerimientos
from os.path import exists
from flask import Flask, request
from subprocess import Popen, PIPE
from waitress import serve
import config as cfg

def exec_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    p.stdout.read()

# renderización y accionar de urls
def u0():
    return ''

def u1():
    exec_cmd(cfg.u1_cmd)
    return cfg.u1_msg

def u2():
    exec_cmd(cfg.u2_cmd)
    return cfg.u2_msg


# personalización de variable
f_ksc = 'BB_SERVER_CODE'
if exists(f_ksc):
    with open(f_ksc) as f:
        cfg.server_code = f.read().strip()

# log urls
f_urls = 'ACTUAL_URL'

# inicio de aplicación
app = Flask(cfg.server_code)

# ruteos de página
app.add_url_rule('/', view_func=u0)

urls = [
    [f'/{cfg.u1}/{cfg.server_code}', u1],
    [f'/{cfg.u2}/{cfg.server_code}', u2]
    ]

exec_cmd('''dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | sed 's/"//g' > /tmp/IP_EXTERNA''')
exec_cmd(f'echo "" > {f_urls}')
for v in urls:
    app.add_url_rule(v[0], view_func=v[1])
    exec_cmd(f'echo "http://"$(cat /tmp/IP_EXTERNA)":{cfg.port}{v[0]}" >> {f_urls}')

# inicializar server
if __name__ == '__main__':
    print(f'http://{cfg.host}:{cfg.port}')
    serve(app, host=cfg.host, port=cfg.port)
