from PIL import Image
import os

def redimensionar_imagem(input_path, output_path, novo_tamanho):
    # Verificar se o arquivo existe
    if not os.path.exists(input_path):
        raise FileNotFoundError(f'A imagem {input_path} não foi encontrada.')

    # Verificar se já existe um arquivo com o mesmo nome e adicionar um sufixo numerado
    counter = 1
    while os.path.exists(output_path):
        output_filename = f'{nome_arquivo}  {tamanho_str}  ({counter}).png'
        output_path = os.path.join('Ajustada', output_filename)
        counter += 1

    # Abrir a imagem
    imagem = Image.open(input_path)

    # Redimensionar a imagem para as novas dimensões
    nova_imagem = imagem.resize(novo_tamanho)

    # Salvar a nova imagem na pasta Ajustada
    nova_imagem.save(output_path)

    # Exibir novo nome do arquivo
    print(f"\nSalvo como: {output_path}\n")

# Diretórios de entrada e saída
caminho_entrada = 'img/Imagem.jpg'

tamanho_desejado = "800x800"
tamanho_desejado = tamanho_desejado.replace("x", ",")
tamanho_desejado = tuple(map(int, tamanho_desejado.split(",")))

tamanho_str = f"{tamanho_desejado[0]}x{tamanho_desejado[1]}"

# Caminho de saída na pasta Ajustada
nome_arquivo = os.path.splitext(os.path.basename(caminho_entrada))[0]  # Obtém o nome do arquivo sem extensão
caminho_saida = os.path.join('Ajustada', f'{nome_arquivo}  {tamanho_str}.png')

# Redimensionar a imagem
try:
    redimensionar_imagem(caminho_entrada, caminho_saida, tamanho_desejado)
except FileNotFoundError as e:
    # Imprimir mensagem de erro
    print(f"Erro: {e}")
