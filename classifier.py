from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time


ENDPOINT = "https://tumorpredictor.cognitiveservices.azure.com/"

#Keys
prediction_key = "5d7b521209884f01bfd402c49c343e48"
prediction_resource_id = "/subscriptions/d06e41e2-ee01-4888-a67b-3b8bdcff01a1/resourceGroups/FRT-Project"
url = "https://centralindia.api.cognitive.microsoft.com/customvision/v3.0/Prediction/220fce72-9221-425c-917f-6778d57e30a6/classify/iterations/Iteration1/image"

publish_iteration_name = "Iteration1"
project_id = "220fce72-9221-425c-917f-6778d57e30a6"


#Making prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
def classify(image):
    """
    Classify the given image in binary format.
    """
    test_data = image
    results = predictor.classify_image(project_id, publish_iteration_name, test_data)
    result_data = {}
    for prediction in results.predictions:
        result_data[prediction.tag_name] = prediction.probability * 100
    
    return result_data
    #return results


#Test
if __name__ == "__main__":
    img_path = "test-image/no_tumor/image.jpg"

    #Test implemented method
    with open(img_path, "rb") as image_contents:
        results = classify(image_contents.read())
        print(results)