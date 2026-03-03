##🔎 TCP-Port-Scanner
Scanner de portas TCP multithread desenvolvido em Python, com classificação de IP e geração de relatório em JSON.

##📌 Funcionalidades
Escaneamento de portas TCP com alta performance

Identificação automática de serviços (socket.getservbyport)

Banner grabbing para serviços que respondem a requisições HTTP simples

Classificação do tipo de IP: Público, Privado, Loopback, Multicast ou Reservado

Geração automática de relatório em JSON (report.json)

Interface via linha de comando

##📦 Requisitos
Python 3.6 ou superior

Nenhuma dependência externa necessária (usa apenas bibliotecas padrão)

##🧠 Como usar
python scanner.py <alvo> <porta_inicial> <porta_final>

Exemplo:
  python scanner.py 127.0.0.1 1 500
  
Exemplo com domínio:
  python scanner.py exemplo.com 10 200

##🖥️ Exemplo de Saída no Terminal
[*] Scanning 93.184.216.34 | Type: Public

[+] Port 80 Open | http | HTTP/1.1 200 OK
[+] Port 443 Open | https | HTTPS - TLS handshake required

[*] Scan finished in 2.45 seconds.

##📄 Exemplo do Arquivo JSON Gerado
[
    {
        "port": 80,
        "service": "http",
        "banner": "HTTP/1.1 200 OK"
    },
    {
        "port": 443,
        "service": "https",
        "banner": "HTTPS - TLS handshake required"
    }
]

##Autor
Asaph Bastos
