import socket

HOST = '127.0.0.1' # IP do servidor
PORTA = 15000      # Porta do servidor

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
enderecoServidor  = (HOST, PORTA)

tcpSocket.connect(enderecoServidor);
print("\tBem-vindo\nComados de mudança de diretório podem não funcionar corretamente.\nUtilize caminhos absolutos")
print ("Conexão estabelecida com servidor");
while True:
  comando = input("\n:");
  if(comando == 'exit'):
    break
  tcpSocket.send(comando.encode('utf-8'));
  print(tcpSocket.recv(1024).decode('utf-8'));

