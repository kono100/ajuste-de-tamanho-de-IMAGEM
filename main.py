from PIL import Image
import os

def redimensionar_imagem(input_path, output_path, novo_tamanho):
    # Abrir a imagem
    imagem = Image.open(input_path)

    # Redimensionar a imagem para as novas dimensões
    nova_imagem = imagem.resize(novo_tamanho)

    # Salvar a nova imagem
    nova_imagem.save(output_path)

# Diretórios de entrada e saída
caminho_entrada = 'img/t.jpg'
caminho_saida = 'Ajustada/exemplo_redimensionada.jpg'
tamanho_desejado = (333, 100)

# Certifique-se de que o diretório de saída existe, se não, crie
if not os.path.exists('Ajustada'):
    os.makedirs('Ajustada')

# Redimensionar a imagem
redimensionar_imagem(caminho_entrada, caminho_saida, tamanho_desejado)
