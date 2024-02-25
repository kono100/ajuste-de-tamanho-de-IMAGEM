from PIL import Image
import os

def redimensionar_imagem(input_path, output_path, novo_tamanho):
    # Abrir a imagem
    imagem = Image.open(input_path)

    # Redimensionar a imagem para as novas dimensões
    nova_imagem = imagem.resize(novo_tamanho)

    # Salvar a nova imagem na pasta Ajustada
    nova_imagem.save(output_path)

# Diretórios de entrada e saída
caminho_entrada = 'img/Imagem.jpg'

tamanho_desejado = "1000x641"
tamanho_desejado = tamanho_desejado.replace("x", ",")
tamanho_desejado = tuple(map(int, tamanho_desejado.split(",")))


tamanho_str = f"{tamanho_desejado[0]}x{tamanho_desejado[1]}"


# Caminho de saída na pasta Ajustada
nome_arquivo = os.path.splitext(os.path.basename(caminho_entrada))[0]  # Obtém o nome do arquivo sem extensão
caminho_saida = os.path.join('Ajustada', f'{nome_arquivo}  {tamanho_str}.png')

# Redimensionar a imagem
redimensionar_imagem(caminho_entrada, caminho_saida, tamanho_desejado)

# Exibir informações
print(f"\nSalvo como: {caminho_saida}\n")

# Verificar se já existe um arquivo com o mesmo nome e adicionar um sufixo numerado
counter = 1
while os.path.exists(caminho_saida):
    output_filename = f'{nome_arquivo}  {tamanho_str}  ({counter}).png'
    caminho_saida = os.path.join('Ajustada', output_filename)
    counter += 1

# Redimensionar novamente e salvar com o novo nome
redimensionar_imagem(caminho_entrada, caminho_saida, tamanho_desejado)

# Exibir novo nome do arquivo
print(f"\nSalvo como: {caminho_saida}\n")
