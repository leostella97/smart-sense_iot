from imageai.Detection import ObjectDetection

def detectar_objetos_na_imagem(input_image, output_image, model_path):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()  # Usar o modelo YOLOv3
    detector.setModelPath(model_path)  # Caminho para o modelo pré-treinado YOLOv3
    detector.loadModel()

    # Detecção de objetos na imagem de entrada
    detections = detector.detectObjectsFromImage(input_image, output_image_path=output_image, minimum_percentage_probability=30)

    # Exibindo os resultados
    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    
    return detections

if __name__ == "__main__":
    input_image = "img_entrada.jpg"
    output_image = "img_saida.jpg"
    model_path = "caminho_modelo_YOLO.h5"  # Baixe o modelo YOLOv3 pré-treinado

    detectar_objetos_na_imagem(input_image, output_image, model_path)