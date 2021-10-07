# TCC2

**As aplicações stylegan-encoder e interfacegan foram utilizadas apenas para finalidades de estudo.**

## Baseado nos trabalhos realizados por:
- SHEN, Y.; GU, J.; TANG, X.; ZHOU, B. Interpreting the latent space of gans for semantic face editing. In:2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2020, Seattle, WA, USA, June 13-19,2020. IEEE, 2020. p. 9240–9249. Disponível em: <https://doi.org/10.1109/CVPR42600.2020.00926>. Repositório Github: https://github.com/genforce/interfacegan
- KARRAS,  T.;  LAINE,  S.;  AILA,  T.  A  style-based  generator  architecture  for generative adversarial networks. In:IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2019, Long Beach, CA, USA, June 16-20,2019. Computer Vision Foundation / IEEE, 2019. p. 4401–4410. Disponível em: <http://openaccess.thecvf.com/content\_CVPR\_2019/html/Karras\_A\_Style-Based\_Generator\_Architecture\_for\_Generative\_Adversarial\_Networks\_CVPR\_2019\_paper.html>. Repositório Github: https://github.com/NVlabs/stylegan

## Base de dados utilizada:

A base de dados utilizda foi a FFHQ, apresentada em:
KARRAS,  T.;  LAINE,  S.;  AILA,  T.  A  style-based  generator  architecture  for generative adversarial networks. In:IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2019, Long Beach, CA, USA, June 16-20,2019. Computer Vision Foundation / IEEE, 2019. p. 4401–4410. Disponível em: <http://openaccess.thecvf.com/content\_CVPR\_2019/html/Karras\_A\_Style-Based\_Generator\_Architecture\_for\_Generative\_Adversarial\_Networks\_CVPR\_2019\_paper.html>.

E disponibilizada em:
https://github.com/NVlabs/stylegan

## Aplicação baseada nos repositórios:
Repositório Oficial InterfaceGAN:
- InterfaceGAN:https://github.com/Vishal-V/GSoC-TensorFlow-2019/tree/master/face_app
Repositórios de contribuição ao trabalho realizado por Karras, et. Al (2019):
- StyleGAN-Encoder com otimizadores: https://github.com/pbaylies/stylegan-encoder, contribuição ao repositório stylegan-encoder: https://github.com/Puzer/stylegan-encoder. Ambas stylegan-encoder, foram contribuições diretas ao repositório da StyleGAN oficial: https://github.com/NVlabs/stylegan.
Neste trabalho foi utilizada a StyleGAN-Encoder com otimizadores.


### Ambiente de execução, Versionamento e Frameworks:
**Algoritmo executado usando a plataforma Google Colab**

**Configurações e Dependências:**

**Python**
- Versão 3.7.3

**Tensorflow**
- Versão 2.X executado em modo compatibilidade com a versão 1.x

**Keras**
- Versão 2.3.1

**Numpy**
- Versão 1.19.5

**h5py**
- Versão 2.10.0

### Execução do modelo
- O primeiro passo é clonar o repositório git:

```
!git clone https://github.com/jpparreirap/TCC2
```

- Em seguida, realizar o modo compatibilidade do tensorflow para a versão 1.x:

```
%tensorflow_version 1.x
```

- Agora devemos entrar no diretório da aplicação stylegan-encoder e preparar o diretório que recebe as imagens sem processamento e o diretório que receberá as imagens pré-processadas:

```
cd stylegan-encoder
```

```
!mkdir raw_images aligned_images
```

- Coloque as imagens desejadas no diretório raw_images, e execute o script para realizar o pré-processamento dessas imagens:

```
!python align_images.py raw_images/ aligned_images/ --output_size=1024
```

- Agora faça o download do modelo resnet, crie um diretório chamado data e coloque o modelo resnet dentro dela:

```
!gdown https://drive.google.com/uc?id=1aT59NFy9-bNyXjDuZOTMl0qX0jmZc6Zb
```

```
!mkdir data
```

```
!mv finetuned_resnet.h5 data
```

- Prepare o framework h5py:

```
!pip install 'h5py<3.0.0'
```

- Agora para obter os vetores latentes, execute o script `encode_images.py`, passando como argumento o otimizador desejado, os parâmetros pré-definidos, a o diretório das imagens pré-processadas (aligned_images), o diretório que recebera a reconstruição inicial (generated_images), e o diretório que receberá a representação latente/vetores latentes de cada imagem (latente_representations).

```
!python encode_images.py --optimizer=adam --lr=0.002 --decay_rate=0.95 --decay_steps=6 --use_l1_penalty=0.3 --face_mask=True --iterations=500 --early_stopping=False --early_stopping_threshold=0.05 --average_best_loss=0.5 --use_lpips_loss=0 --use_discriminator_loss=0 --output_video=True aligned_images/ generated_images/ latent_representations/
```

- Em seguida execute o script `save_latent.py`, para gerar um únivo vetor de saída contendo todas as representações latentes em blocos:

```
!python save_latent.py
```

O script `save_latent.py` é uma contribuição de , disponível em: 

- Tendo obtido a representação latente, agora vamos entrar na parte da aplicação InterfaceGAN:

```
cd ../interfacegan/
```

- Então iremos realizar o download do modelo pré-treinado e coloca-lo dentro do diretório `models/pretrain/`:

```
!gdown colocar link dps
```

- Por fim, basta executar o script `edit.py`, passando como argumento o nomde do modelo pré-treinado (`-m stylegan_ffhq`), o boundarie que será utilizado (`-b boundaries/stylegan_ffhq_age_w_boundary.npy`), o espaço latente (`-s Wp`), o caminho para o vetor único de saída (`-i '/content/drive/MyDrive/stylegan-encoder/latent_representations/output_vectors.npy'`), o diretório de saída para o resultado da pravisão (`-o results/predict/`), o intervalo de variação (`--start_distance` e `--end_distance`) e o número de passos para que essas modificaçõe sejam feitas (`--steps`). Desta forma:

```
!python edit.py -m stylegan_ffhq -b boundaries/stylegan_ffhq_age_w_boundary.npy -i '/content/drive/MyDrive/stylegan-encoder/latent_representations/output_vectors.npy' -o results/predict/ -3.0 3.0 10
```

Os resultados obtidos podem ser visualizados no diretório de saída que foi passado como parêmetro para este algoritmo, neste caso seria o diretório `results/predict/`.
