a. Pesquisar sobre os métodos do OPENCV, descritos abaixo:
opencv_annotation,
opencv_createsamples, 
opencv_traincascade.


Usando a ferramenta de anotação integrada do OpenCV

Desde o OpenCV 3.x, a comunidade fornece e mantém uma ferramenta de anotação de código aberto, usada para gerar o -infoarquivo. A ferramenta pode ser acessada pelo comando opencv_annotation.

O uso da ferramenta é bastante direto. A ferramenta aceita vários parâmetros obrigatórios e alguns opcionais:

--annotations (obrigatório) : caminho para o arquivo txt de anotações, no qual você deseja armazenar suas anotações, que são passadas para o -infoparâmetro [exemplo - /data/annotations.txt]
--images (obrigatório) : caminho para a pasta que contém as imagens com seus objetos [exemplo - / data / testimages /]
--maxWindowHeight (opcional) : se a imagem de entrada for maior em altura, em seguida, a resolução fornecida aqui, redimensione a imagem para facilitar a anotação usando --resizeFactor.
--resizeFactor (opcional) : fator usado para redimensionar a imagem de entrada ao usar o --maxWindowHeightparâmetro.
Observe que os parâmetros opcionais podem ser usados ​​apenas juntos. Um exemplo de comando que pode ser usado pode ser visto abaixo

opencv_annotation --annotations = / caminho / para / anotações / arquivo.txt --images = / caminho / para / imagem / pasta /

Este comando abrirá uma janela contendo a primeira imagem e o cursor do mouse, que serão usados ​​para anotação. Basicamente, existem várias teclas que acionam uma ação. 
O botão esquerdo do mouse é usado para selecionar o primeiro canto do seu objeto, depois continua desenhando até estiver ok e para um segundo clique no botão esquerdo do mouse é registrado. 

Após cada seleção, você tem as seguintes opções:

Pressionando c: confirme a anotação, deixando a anotação verde e confirmando que está armazenada
Pressionando d: exclua a última anotação da lista de anotações (fácil para remover anotações erradas)
Pressionando n: continue para a próxima imagem
Pressionando ESC: isso sairá do software de anotação

Finalmente, você terminará com um arquivo de anotação utilizável que pode ser passado ao -infoargumento de opencv_createsamples.


Ao executar opencv_createsamples, o procedimento a seguir é usado para criar uma instância de objeto de amostra: 
A imagem de origem fornecida é girada aleatoriamente em torno dos três eixos. O ângulo escolhido é limitado por -maxxangle, -maxyanglee -maxzangle. 
Em seguida, pixels com a intensidade do [bg_color-bg_color_threshold; bg_color + bg_color_threshold] são interpretados como transparentes. O ruído branco é adicionado às intensidades do primeiro plano. Se a -invchave for especificada, as intensidades de pixel em primeiro plano serão invertidas. Se a -randinvchave for especificada, o algoritmo seleciona aleatoriamente se a inversão deve ser aplicada a esta amostra. Por fim, a imagem obtida é colocada em um plano de fundo arbitrário a partir do arquivo de descrição de plano de fundo, redimensionada para o tamanho desejado especificado por -we-he armazenado no arquivo vec, especificado pela -vecopção da linha de comandos.

Amostras positivas também podem ser obtidas de uma coleção de imagens previamente marcadas, que é a maneira desejada ao criar modelos de objetos robustos. Essa coleção é descrita por um arquivo de texto semelhante ao arquivo de descrição de plano de fundo. Cada linha deste arquivo corresponde a uma imagem. O primeiro elemento da linha é o nome do arquivo, seguido pelo número de anotações de objetos, seguido pelos números que descrevem as coordenadas dos objetos que delimitam os retângulos (x, y, largura, altura).

O utilitário opencv_createsamples pode ser usado para examinar amostras armazenadas em qualquer arquivo de amostras positivas. 
Para fazer isso apenas -vec, -we os -hparâmetros devem ser especificados.
Exemplo de arquivo vec está disponível aqui opencv/data/vec_files/trainingfaces_24-24.vec. 
Ele pode ser usado para treinar um detector de cara com o seguinte tamanho da janela: -w 24 -h 24.

Treinamento em cascata

O próximo passo é o treinamento real da cascata impulsionada de classificadores fracos, com base no conjunto de dados positivo e negativo que foi preparado.

Argumentos de linha de comando do aplicativo opencv_traincascade agrupados por finalidades:

Argumentos comuns:
-data <cascade_dir_name>: Onde o classificador treinado deve ser armazenado. Esta pasta deve ser criada manualmente com antecedência.
-vec <vec_file_name> : arquivo vec com amostras positivas (criadas pelo utilitário opencv_createsamples).
-bg <background_file_name>: Arquivo de descrição de plano de fundo. Este é o arquivo que contém as imagens de amostra negativas.
-numPos <number_of_positive_samples> : Número de amostras positivas usadas no treinamento para cada estágio do classificador.
-numNeg <number_of_negative_samples> : Número de amostras negativas usadas no treinamento para cada estágio do classificador.
-numStages <number_of_stages> : Número de estágios em cascata a serem treinados.
-precalcValBufSize <precalculated_vals_buffer_size_in_Mb>: Tamanho do buffer para valores de recursos pré-calculados (em Mb). Quanto mais memória você atribuir mais rápido o processo de formação, no entanto ter em mente que -precalcValBufSizee -precalcIdxBufSizecombinado não deve exceder você memória disponível no sistema.
-precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb>: Tamanho do buffer para índices de recursos pré-calculados (em Mb). Quanto mais memória você atribuir mais rápido o processo de formação, no entanto ter em mente que -precalcValBufSizee -precalcIdxBufSizecombinado não deve exceder você memória disponível no sistema.
-baseFormatSave: Esse argumento é real no caso de recursos do tipo Haar. Se for especificado, a cascata será salva no formato antigo. Isso está disponível apenas por razões de compatibilidade com versões anteriores e para permitir que os usuários presos à interface obsoleta antiga treinem pelo menos modelos usando a interface mais recente.
-numThreads <max_number_of_threads>: Número máximo de threads a serem usados ​​durante o treinamento. Observe que o número real de threads usados ​​pode ser menor, dependendo da sua máquina e das opções de compilação. Por padrão, o máximo de threads disponíveis é selecionado se você criou o OpenCV com suporte a TBB, o que é necessário para essa otimização.
-acceptanceRatioBreakValue <break_value>: Esse argumento é usado para determinar quão preciso seu modelo deve continuar aprendendo e quando parar. Uma boa orientação é treinar não mais do que 10e-5, para garantir que o modelo não exagere nos dados de treinamento. Por padrão, esse valor é definido como -1 para desativar esse recurso.
Parâmetros em cascata:
-stageType <BOOST(default)>: Tipo de etapas. No momento, apenas classificadores aprimorados são suportados como um tipo de estágio.
-featureType<{HAAR(default), LBP}> : Tipo de recursos: HAAR - recursos semelhantes ao Haar, LBP - padrões binários locais.
-w <sampleWidth>: Largura das amostras de treinamento (em pixels). Deve ter exatamente o mesmo valor usado durante a criação de amostras de treinamento (utilitário opencv_createsamples).
-h <sampleHeight>: Altura das amostras de treinamento (em pixels). Deve ter exatamente o mesmo valor usado durante a criação de amostras de treinamento (utilitário opencv_createsamples).
Parâmetros de classificador aprimorados:
-bt <{DAB, RAB, LB, GAB(default)}> : Tipo de classificadores impulsionados: DAB - AdaBoost discreto, RAB - AdaBoost real, LB - LogitBoost, GAB - AdaBoost suave.
-minHitRate <min_hit_rate>: Taxa de acerto mínima desejada para cada estágio do classificador. A taxa geral de acertos pode ser estimada em (min_hit_rate ^ number_of_stages), [213] §4.1.
-maxFalseAlarmRate <max_false_alarm_rate>: Taxa máxima de alarmes falsos desejada para cada estágio do classificador. A taxa geral de alarmes falsos pode ser estimada em (max_false_alarm_rate ^ number_of_stages), [213] §4.1.
-weightTrimRate <weight_trim_rate>: Especifica se o corte deve ser usado e seu peso. Uma escolha decente é 0,95.
-maxDepth <max_depth_of_weak_tree>: Profundidade máxima de uma árvore fraca. Uma escolha decente é 1, que é o caso de tocos.
-maxWeakCount <max_weak_tree_count>: Contagem máxima de árvores fracas para cada estágio em cascata. O classificador impulsionado (estágio) terá tantas árvores fracas (<= maxWeakCount), conforme necessário para alcançar o dado -maxFalseAlarmRate.
Parâmetros de recurso do tipo Haar:
-mode <BASIC (default) | CORE | ALL>: Seleciona o tipo de conjunto de recursos Haar usado no treinamento. O BASIC usa apenas recursos na vertical, enquanto o ALL usa o conjunto completo de recursos na vertical e girados a 45 graus. Veja [123] para mais detalhes.
Parâmetros de padrões binários locais: os padrões binários locais não têm parâmetros.
Depois que o aplicativo opencv_traincascade terminar seu trabalho, a cascata treinada será salva em um cascade.xmlarquivo na -datapasta Outros arquivos nesta pasta são criados para o caso de treinamento interrompido, portanto, você pode excluí-los após a conclusão do treinamento.

O treinamento está concluído e você pode testar seu classificador em cascata!



b. Elaborar um tutorial de como pode-se treinar uma rede para ser usada no python com o cv2.


Step 1: Preparo Do Ambiente

Serão utilizados neste tutorial os seguintes programas:

- Python 3.6 (Esta versão já vem como pip Instalado);

- Numpy (Numerical Python);

- OpenCV último release estável disponível.

Como já há o pip instalado nesta versão do Python será possível baixar os pacotes Python necessários.

Para começarmos devemos criar o diretório do projeto como o nome que desejar. 
Dentro do Diretório devem ser criadas os seguintes diretórios. Esta estrutura será utilizada para quando for feito o treinamento com apenas uma imagem do objeto que se deseja detectar:

- data (onde será salvo o resultado do treinamento do algoritmo, arquivo XML que será utilizado para detecção de objetos);

- positivas (imagens do objeto que se deseja detectar, na resolução 50 x 50 pixesl e em escala de cinza);

- negativas (imagens negativas, imagens que não contém o objeto que se deseja detectar);

- feias (imagens com erro de que não existem mais nos links onde seriam baixadas); - info (amostras criadas com base nas imagens negativas e positivas).

Esta estrutura será utilizada para quando for feito o treinamento com mais de uma imagem do objeto que se deseja detectar:

- Será feita uma pasta info para cada imagem que se deseja detectar.


Step 2: Baixando O Dataset De Imagens Negativas

Este passo consiste em baixar o dataset de imagens negativas, são necessárias algumas centenas de imagens negativas para que o treinamento do algoritmo fique preciso e que a detecção funcione com a precisão desejada. 
Baixar esta quantidade de imagens manualmente é completamente inviável, para esta finalidade já existe um site que transforma imagens da Web em suas respectivas URLs para que você apenas utilize no seu script e as baixe.
Você pode acessar o site:

http://image-net.org

Step 3: Removendo Imagens Falhas

À partir disso será utilizado um script para que sejam removidas as imagens do seu dataset que são iguais às imagens falhas.

import numpy as np

import cv2

import os

igual = False

for file_type in ['negativas']:

for img in os.listdir(file_type):

for feia in os.listdir('feias'):

try:

caminho_imagem = str(file_type)+'/'+str(img)

feia = cv2.imread('feias/'+str(feia))

pergunta = cv2.imread(caminho_imagem)

if feia.shape == pergunta.shape and not(np.bitwise_xor(feia,pergunta).any()):

print('Apagando imagem feia!')

print(caminho_imagem)

os.remove(caminho_imagem)

except Exception as e:

print(str(e))

Este script removerá uma série de imagens que corresponderão às imagens que não desejamos utilizar no treinamento do algoritmo.


Step 4: Renomeando Arquivos Da Pasta De Images

Este não é um passo necessário mas deixa a prática mais elegante.

Com a remoção das imagens feias os nomes dos arquivos não seguirão uma sequencia então vamos renomeá-los numa sequência numérica novamente para isto utilizaremos um script que vamos colocar dentro do diretório onde as imagens se encontram, no caso, "negativas".

Podemos selecionar todas as imagens dentro da pasta e renomeá-las via Windows mesmo ou Linux, selecionando e apertando a tecla F2 irá renomear todas as imagens para o mesmo nome com um incremento numérico. O script abaixo não está tratando quando tenta-se renomear uma imagem para o mesmo nome que ela já possui.

import os

for i, f in enumerate(os.listdir(".")):

f_new = '{}.jpg'.format(i)

os.rename(f, f_new)

print '{}.'.format(i), f, '->', f_new

Após este passo as imagens que estão no diretório "negativas" estarão renomeadas com números em ordem crescente.

Step 5: Gerando Lista De Imagens Negativas
Deve ser gerada uma lista da localização das imagens presentes no diretório de imagens negativas para que esta lista seja utilizada para criar amostras e treinar o algoritmo para gerar o arquivo com as características que devem ser detectadas.

import urllib

import numpy as np

import cv2

import os

for file_type in ['negativas']:

for img in os.listdir(file_type):

if file_type == 'negativas':

line = file_type+'/'+img+'\n'

with open('bg.txt','a') as f:

f.write(line)

elif file_type == 'positivas':

line = file_type+'/'+img+' 1 0 0 150 150\n'

with open('info.dat','a') as f:

f.write(line)


Step 6: Criando Amostras

De posse dos arquivos de imagens negativas, da imagem positiva e da lista de imagens negativas que foi gerado no passo anterior podemos criar amostras de imagens positivas para serem utilizadas no treinamento da imagem.

Abaixo a sintaxe do comando que deve ser utilizado para que sejam geradas as amostras de imagens positivas:

opencv_createsamples -img NOME_DO_ARQUIVO.jpg -bg ARQUIVO_LISTA_DE_IMAGENS_NEGATIVAS.txt -info DIRETÓRIO_SAÍDA/ARQUIVO_LISTA.lst -pngoutput DIRETÓRIO_SAÍDA -maxxangle ÂNGULO_MÁXIMO_EIXO_X -maxyangle ÂNGULO_MÁXIMO_EIXO_Y -maxzangle ÂNGULO_MÁXIMO_EIXO_Z -num NÚMERO_DE_IMAGENS_NEGATIVAS

No exemplo da sintaxe do comando de criar amostra temos a imagem positiva como POS.jpg e 5500 imagens negativas.

opencv_createsamples -img POS.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 5500


OBSERVAÇÃO: Para treinar para mais de uma imagem positiva devem ser geradas amostras para cada. E deve ser gerado um diretório info para cada imagem positiva. (info1, info2 e etc).

Após criada a lista acima devemos gerar um vetor com as imagens e a posição da imagem positiva em cada uma das imagens negativas. Será criado um arquivo de vetores.

opencv_createsamples -info DIRETÓRIO/ARQUIVO_LISTA.lst -num NÚMERO_DE_IMAGENS_NEGATIVAS -w LARGURA_DA_AMOSTRA -h ALTURA_DA_AMOSTRA -vec ARQUIVO_VETORES

No exemplo da sintaxe do comando de criar amostra temos 5500 imagens negativas, altura e largura máxima 20 pixels e arquivo de saída positives.vec.

opencv_createsamples -info info/info.lst -num 5500 -w 20 -h 20 -vec positives.vec


OBSERVAÇÃO: Para treinar para mais de uma imagem positiva devem ser gerados vários vetores, um para cada imagem positiva e depois devemos fundir os vetores gerados.

Para fundir os vetores há um script do GitHub: https://github.com/wulfebw/mergevec

A sintaxe de uso é:

python mergevec.py -v DIRETÓRIO_VETORES -o ARQUIVO_VETOR_SAÍDA


Step 7: Treinando O Algoritmo

Feitos os passos anteriores que são rápidos (exceto o download das imagens mas que também é relativamente rápido perto deste) está na hora do passo mais demorado de todos que é a parte do treinamento do algoritmo. Este passo dependendo do número de imagens negativas/amostras utilizadas pode demorar dias. Como referência tenha que para 1900 imagens e apenas uma positiva é um processo que leva em torno de 2 horas quando desejamos uma taxa de falsos alarmes de 0.5%. Os parâmetros podem fazer com que o tempo demore bastante.

Para realizar o treinamento da imagem deve ser utilizado o seguinte comando:

opencv_traincascade -data PASTA_DESTINO -vec VETOR.vec -bg bg.txt -numPos (NÚMERO_DE_IMAGENS - 200) -numNeg METADE_DO_NUMPOS -numStages NÚMERO_DE_ESTAGIOS_DO_TREINO -w LARGURA_DA_AMOSTRA -h ALTURA_DA_AMOSTRA

Seguindo o Exemplo:

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 5000 -numNeg 2500 -numStages 10 -w 20 -h 20

Lembrando que quanto maior o número de estágios mais precisa será a detecção mas também mais demorado será o processo de treino.

Durante o treino serão gerados diversos arquivos .XML na pasta data um arquivo referente à cada estágio e um aos parâmetros.

Após o treino será gerado um arquivo chamado cascade.xml que será utilizado para a detecção.


OBSERVAÇÃO 1: Caso haja problema em algum estágio, basta utilizar novamente o comando de treinamento que os estágios que já foram feitos permanecerão.

OBSERVAÇÃO 2: Caso esteja fazendo para mais de uma imagem positiva, utilize o vetor resultante da união mencionada no passo anterior e no campo de -numPos utilize o número de imagens negativas vezes número de positivas e subtraia entre 200 e 500 para cada imagem positiva.


Step 8: Detectando Objetos

Deve ser criado um script para detectar objetos, uma vez que foi feito o treinamento do algoritmo e se tem um arquivo .XML referente à detecção do objeto que se deseja. Segue script:

import cv2

import sys

# Define o número da Webcam

NUM_WEBCAM = 0

# Responsável por ler arquivo XML

if len(sys.argv) > 1:

XML_PATH = sys.argv[1]

else:

print "Erro: Caminho para XML não definido"

sys.exit(1)

# Inicializa o Classificador Cascade

faceCascade = cv2.CascadeClassifier(XML_PATH)

# Inicializa a Webcam

vc = cv2.VideoCapture(NUM_WEBCAM)

# Verifica se a Webcam está funcionando

if vc.isOpened():

# Tentar pegar o primeiro frame

retval, frame = vc.read()

else:

# Fechar o programa

sys.exit(1)


i = 0

objetos =[]

# Se a Webcam estiver lendo, repetir indefinidamente

while retval:

# Define o frame que será mostrado

frame_show = frame

if i % 1 == 0:

# Converte o frame para escalas de cinza e descarta os dados de cores

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detecta objetos e retorna o array de objetos

objetos = faceCascade.detectMultiScale(

frame,

scaleFactor=1.2,

minNeighbors=20,

minSize=(50, 50),

flags=cv2.CASCADE_SCALE_IMAGE

)

# Desenha um retângulo em torno do objeto

for (x, y, w, h) in objetos:

cv2.rectangle(frame_show, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Mostra o Frame ao usuário

cv2.imshow("Foto", frame_show)

# Lê o próximo frame

retval, frame =vc.read()

# Fecha o programa se o usuário apertar o botão ESC

if cv2.waitKey(1) == 27:

break

i += 1

Após criar o script salvá-lo como detecta.py, por exemplo, para utilizá-lo basta seguir a sintaxe abaixo:

python detecta.pyARQUIVO_XML


Step 9: Usando O Código - Detectar Ford New Fiesta

Foi treinado um algoritmo para reconhecer um Ford New Fiesta. 
Foi utilizada apenas uma imagem para treinar então irá detectar apenas o Ford New Fiesta idêntico. 
O treinamento utilizando apenas uma imagem é ideal para alguma empresa que quer detectar quando vezes a sua logomarca aparece, pois não há muitas variações exceto ângulos.

