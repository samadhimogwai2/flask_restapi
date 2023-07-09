import base64
from io import BytesIO
from PIL import Image
import torchvision

def image_recognition(image):
    # Step 1: Initialize model with the best available weights
    print("Load Model")
    weights = torchvision.models.ResNet50_Weights.DEFAULT
    model = torchvision.models.resnet50(weights=weights)
    model.eval()

    # Step 2: Initialize the inference transforms
    print("Preprocess")
    preprocess = weights.transforms()
    batch = preprocess(image).unsqueeze(0)

    # Step 3: Use the model and print the predicted category
    print("prediction")
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    return score, category_name    

def main():
    image_path = "./images/sample.jpg"

    # Step 0: Load Image
    print("Load Image")
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    image_byte = base64.b64decode(image_b64.encode("utf-8"))
    image_file = BytesIO(image_byte)
    image_pil = Image.open(image_file)

    score, category_name = image_recognition(image_pil)
    print(f"{category_name}: {100 * score:.1f}%")

if __name__ == '__main__':
    main()