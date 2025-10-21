#!/usr/bin/env python3
import time         # Importa o modulo time para funcao que usam o tempo
import zenoh        # Importa a biblioteca ZEnoh 

def main():                                                      # Define a função main
    z = zenoh.open(zenoh.Config())                               # Cria uma sessão Zenoh  e o zenoh.config faz as configs padrão
    pub = z.declare_publisher("demo/example/hello")              # Declara um Publisher para o topico demo/example/ hello, quem tiver inscrito ali, recebe as pubs
    for i in range(10):                                          # Loop
        msg = f"hello {i}"                                       # Insere um valor i dentro da sting
        print("[Publisher teste] Publishing:" , msg)                   # Mostra no console a mensagem que esta sendo publicada
        pub.put(msg)                                             # Publica a mensagem no topico
        time.sleep(1)                                            # Faz o programa esperar 1 segundo
    z.close()       # Close session                              # Fecha a sessao zenoh ao final do loop
    
if __name__ == "__main__":                                        # Verifica se o script esta sendo executado diretamente e nao por outro modulo
    main()                                                        # inicia a funcao main com todos os processos
