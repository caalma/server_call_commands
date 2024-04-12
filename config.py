# server

# este codigo también puede modificarse definiendo la variable BB_SERVER_CODE
# mediante el siguiente comando:
# export BB_SERVER_CODE=codigo_personalizado
# en caso de que exista la variable de entorno el siguiente valor es sobreescrito.
server_code = '01'

# host
host = '0.0.0.0'
port = 9009

# acciones
stop_cmd = 'echo "stop" >> control.log'
stop_msg = 'stop'

restart_cmd = 'echo "restart" >> control.log'
restart_msg = 'restart'
