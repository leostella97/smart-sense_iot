from imageai.Detection import ObjectDetection

def detectar_objetos_na_imagem(input_image, output_image, model_path):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()  # Usar o modelo YOLOv3
    detector.setModelPath(model_path)  # Caminho para o modelo pré-treinado YOLOv3
    detector.loadModel()