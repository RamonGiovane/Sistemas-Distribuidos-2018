# Sistemas Distribuídos 2018
Protocolo de Comandos Remotos Simples - SRCP
=============================================
Este é um simples programa para controlar um host remoto (servidor) por meio de outra máquina cliente.
Este programa é, até que se prove o contrário, multiplataforma. Podendo funcionar independente do SO.
Contate o desenvolvedor em caso de problemas.


*Começando*
********************************************
- O arquivo **servidor.py** contém o programa que será controlado remotamente. Ele deve ser executado
e aguardar até que o cliente esteja pronto.
- Na máquina cliente, a controladora, tem-se dois arquivos próprios. **cliente.py** e **config.txt**
- Para começar, deve-se entrar com o endereço e porta do servidor no arquivo de configuração config.txt
Para que não haja problemas, favor não desrespeitar a formatação ou ordem dos prâmetros do arquivos, apenas os valores.


*Utilizando comandos*
******************************************
Depois que os preparativos foram realizados, você poderá utlizar remotamente comandos para controlar o host servidor,
porém, algumas funcionalidades próprias de linha de comando não funcionam remotamente, por motivos dos próprios sistemas 
operacionais e seus processos, como é o caso do comando *cd* (Windows/Linux).
No entanto, sinta-se livre para criar/ler arquivos, visualizar configurações e etc.




