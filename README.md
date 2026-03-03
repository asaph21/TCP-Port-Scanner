# 🔎 TCP-Port-Scanner
Scanner de portas TCP multithread desenvolvido em Python, com classificação de IP e geração de relatório em JSON.

## 📌 Funcionalidades
Escaneamento de portas TCP com alta performance

Identificação automática de serviços (socket.getservbyport)

Banner grabbing para serviços que respondem a requisições HTTP simples

Classificação do tipo de IP: Público, Privado, Loopback, Multicast ou Reservado

Geração automática de relatório em JSON (report.json)

Interface via linha de comando

## 📦 Requisitos
Python 3.6 ou superior

Nenhuma dependência externa necessária (usa apenas bibliotecas padrão)

## 🧠 Como usar
python scanner.py <alvo> <porta_inicial> <porta_final>

Exemplo:
  python scanner.py 127.0.0.1 1 500
  
Exemplo com domínio:
  python scanner.py exemplo.com 10 200

## 🖥️ Exemplo de Saída no Terminal
<img width="468" height="151" alt="image" src="https://github.com/user-attachments/assets/f6f2b843-6ce1-450e-a7ad-7c31ffdc0909" />


## 📄 Exemplo do Arquivo JSON Gerado
<img width="465" height="274" alt="image" src="https://github.com/user-attachments/assets/f7ab98b6-650d-4863-b9b2-300e5121417e" />

## Autor
Asaph Bastos
