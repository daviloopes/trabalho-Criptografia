import os
import random

# Tipos permitidos de operação
TYPES = ["criptografar", "descriptografar"]

def main(args):
    # Precisamos de 3 parâmetros: arquivo, chave e tipo.
    if len(args) != 3:
        print("Parâmetros inválidos. Verifique e tente novamente.")
        return

    file_path, crypto_key, crypto_type = args

    if not validate_args(file_path, crypto_key, crypto_type):
        return

    if crypto_type == "criptografar":
        encrypt(file_path, crypto_key)
    elif crypto_type == "descriptografar":
        decrypt(file_path, crypto_key)


def validate_args(file_path, crypto_key, crypto_type):
    # O arquivo precisa existir
    if not os.path.exists(file_path):
        print("Arquivo inválido. Verifique o caminho e tente novamente.")
        return False

    # A chave precisa ser fornecida
    if not crypto_key:
        print("A chave é requisitada. Adicione e tente novamente.")
        return False

    # O tipo precisa ser criptografar ou descriptografar
    if crypto_type not in TYPES:
        print("Tipo de ação inválido. Deve ser 'criptografar' ou 'descriptografar'.")
        return False

    return True


def crypto_map(crypto_key):
    # Alfabeto base
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # baseado na frequencia dessas letras em portugues https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras
    frequencies = {
        "A": 14, "E": 12, "O": 10, "S": 7, "R": 6, "I": 6, "N": 5,
        "D": 5, "M": 4, "U": 4, "T": 4, "C": 3, "L": 2, "P": 2
    }

    utf8numbers = list(range(250))

    random.seed(crypto_key)
    random.shuffle(utf8numbers)

    mapped_alphabet = {}

    for i in range(len(alphabet)):
        mapped_alphabet[alphabet[i]] = []
        frequency = frequencies.get(alphabet[i].upper(), 1)
        for j in range(frequency):
            mapped_alphabet[alphabet[i]].append(utf8numbers.pop()) 

    # Criar o mapeamento
    return mapped_alphabet


def encrypt(file_path, crypto_key):
    # Gerar o mapa de criptografia com base na chave
    mapping = crypto_map(crypto_key)

    # Ler o conteúdo do arquivo
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    encrypted_content = []
    # Criptografar o conteúdo
    for char in content:
        entry = mapping.get(char, [ord(char)])
        encrypted_content.append(chr(random.choice(entry)))

    encrypted_text = "".join(encrypted_content)

    # Criar um novo arquivo com o conteúdo criptografado
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{file_name}_criptografado.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

    print(f"Arquivo criptografado gerado: {output_file}")


def decrypt(file_path, crypto_key):
    # Gerar o mapa de criptografia com base na chave
    mapping = crypto_map(crypto_key)

    # Ler o conteúdo criptografado do arquivo
    with open(file_path, 'r', encoding='utf-8') as f:
        encrypted_content = f.read()

    decrypted_content = []
    # Descriptografar o conteúdo
    for char in encrypted_content:
        # Procurar o código original para o caractere criptografado
        original_char = None
        for key, value in mapping.items():
            if ord(char) in value:
                original_char = key
                break
        if original_char:
            decrypted_content.append(original_char)
        else:
            # Caso o caractere não tenha sido criptografado, mantemos como está
            decrypted_content.append(char)

    decrypted_text = "".join(decrypted_content)

    # Criar um novo arquivo com o conteúdo descriptografado
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{file_name}_descriptografado.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

    print(f"Arquivo descriptografado gerado: {output_file}")


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
