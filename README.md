# Projeto de Sensores Inteligentes para IoT

Este repositório contém um projeto de detecção de objetos em imagens digitais, utilizando o modelo YOLO (You Only Look Once) em conjunto com a biblioteca ImageAI.

## Explicação sobre YOLO
YOLO é uma abreviação para "You Only Look Once", que representa uma rede neural de Deep Learning capaz de realizar a detecção e classificação de objetos em uma única etapa. Ele permite uma análise rápida e eficiente de imagens, tornando-o ideal para projetos que necessitam de detecção em tempo real.

## A biblioteca ImageAI
ImageAI é uma biblioteca de fácil uso que trabalha em conjunto com YOLO e oferece uma interface simplificada para a detecção de objetos em imagens e vídeos. Essa combinação poderosa nos permite criar aplicações inteligentes de detecção de objetos.

## Funcionalidades Principais
Neste projeto, o foco é utilizar o modelo YOLO pré-treinado em uma base de dados para detectar e classificar objetos específicos em imagens digitais. A aplicação é versátil, podendo ser utilizada para detectar pessoas em diferentes cenários, como nas ruas, em ambientes residenciais ou em estabelecimentos comerciais.

## Instruções de Uso
Certifique-se de ter o ambiente Python configurado com as dependências necessárias.
Instale a biblioteca ImageAI usando o comando pip: <code>pip install imageai</code>.
Faça o download do modelo YOLOv3 pré-treinado e defina o caminho do modelo no código.
Substitua "img_entrada.jpg" pelo caminho da imagem que deseja analisar.
Defina o caminho onde a imagem de saída, com as caixas delimitadoras dos objetos detectados, será salva.
Execute o código e veja os resultados da detecção de objetos em tempo real!