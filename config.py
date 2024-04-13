# server

# `server_code` también puede definirse con el contenido del
# archivo BB_SERVER_CODE. Sinó tomará el valor de la siguiente variable
server_code = '01'

# host
host = '0.0.0.0'
port = 9009

# acciones
u1 = 'a'
u1_cmd = 'echo $(date) " - A " >> /tmp/scc_control.log'
u1_msg = 'A ... done!'

u2 = 'b'
u2_cmd = 'echo $(date) " - B" >> /tmp/scc_control.log'
u2_msg = 'B ... done!'
