# Criptografia e Descriptografia com Substituição Homofônica

Este projeto implementa uma cifra de substituição homofônica, onde caracteres são substituídos por um conjunto de valores baseados em um mapeamento gerado por uma chave de criptografia.

## Requisitos

- Python 3.x
- Acesso a arquivos para criptografar e descriptografar

## Como Usar

### 1. Preparação

Certifique-se de que o arquivo que você deseja criptografar ou descriptografar está acessível no seu sistema.

### 2. Estrutura de Comando

O programa aceita 3 parâmetros:
- file_path: Caminho para o arquivo a ser criptografado ou descriptografado.
- crypto_key: Chave que será utilizada para gerar o mapeamento de criptografia.
- crypto_type: Tipo de operação a ser realizada, que pode ser "criptografar" ou "descriptografar".

#### Exemplo de uso:

python3 script.py caminho/do/arquivo.txt chave criptografar