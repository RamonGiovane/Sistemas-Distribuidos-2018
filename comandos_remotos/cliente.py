import socket

def cliente():
  arquivo = open('config.txt', 'r')
  texto = arquivo.readlines()

  #Obtendo os valores de cada parametro do arquivo de config.
  HOST = texto[0].split(':')[1].strip()
  PORTA = int(texto[1].split(':')[1].strip())
  
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

try:
  cliente()

except Exception as e:
  print("Algo sinistro aconteceu.\nDetalhes do erro: ", e)


