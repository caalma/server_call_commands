#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# requerimientos
from os import environ
from flask import Flask, request
from subprocess import Popen, PIPE
from waitress import serve
import config as cfg

def exec_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    p.stdout.read()

# reemplazo de variable por versión de environment
ksc = 'BB_SERVER_CODE'
if ksc in environ:
    cfg.server_code = environ[ksc]

# inicio de aplicación
app = Flask(cfg.server_code)

# ruteos de página
@app.route(f'/stop/{cfg.server_code}')
def stop():
    exec_cmd(cfg.stop_cmd)
    return cfg.stop_msg

@app.route(f'/restart/{cfg.server_code}')
def restart():
    exec_cmd(cfg.restart_cmd)
    return cfg.restart_msg

# inicializar server
if __name__ == '__main__':
    print(f'http://{cfg.host}:{cfg.port}')
    serve(app, host=cfg.host, port=cfg.port)
