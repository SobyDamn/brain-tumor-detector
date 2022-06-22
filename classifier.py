from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time




#types of tumors and their corresponding tags in the model as key and name and details as value
tumors = {
    "no_tumor": {
        "name": "No Tumor",
        "about": "No tumor is detected."
    },
    "meningioma_tumor":{
        "name": "Meningioma",
        "about": """
                A meningioma is a tumor that arises from the meninges — the membranes that surround the brain and spinal cord. Although not technically a brain tumor, it is included in this category because it may compress or squeeze the adjacent brain, nerves and vessels. Meningioma is the most common type of tumor that forms in the head.Meningiomas occur more commonly in women and are often discovered at older ages, but they may occur at any age.\n
                Because most meningiomas grow slowly, often without any significant signs and symptoms, they do not always require immediate treatment and may be monitored over time.
                """
    },
    "pituitary_tumor":{
        "name": "Pituitary",
        "about": """
                Pituitary tumors are abnormal growths that develop in your pituitary gland. Some pituitary tumors result in too much of the hormones that regulate important functions of your body. Some pituitary tumors can cause your pituitary gland to produce lower levels of hormones.
                Most pituitary tumors are noncancerous (benign) growths (adenomas). Adenomas remain in your pituitary gland or surrounding tissues and don't spread to other parts of your body.
                There are various options for treating pituitary tumors, including removing the tumor, controlling its growth and managing your hormone levels with medications
        """
    },
    "glioma_tumor":{
        "name": "Glioma",
        "about": """
                Glioma is a type of tumor that occurs in the brain and spinal cord. Gliomas begin in the gluey supportive cells (glial cells) that surround nerve cells and help them function.
                Three types of glial cells can produce tumors. Gliomas are classified according to the type of glial cell involved in the tumor, as well as the tumor's genetic features, which can help predict how the tumor will behave over time and the treatments most likely to work.A glioma can affect your brain function and be life-threatening depending on its location and rate of growth.
                Types of glioma include:
                \n
                \n

                1.Astrocytomas, including astrocytoma, anaplastic astrocytoma and glioblastoma\n
                2.Ependymomas, including anaplastic ependymoma, myxopapillary ependymoma and subependymoma\n
                3.Oligodendrogliomas, including oligodendroglioma, anaplastic oligodendroglioma and anaplastic oligoastrocytoma\n
                """
    }

}

ENDPOINT = "https://tumorpredictor.cognitiveservices.azure.com/"

#Keys
prediction_key = "5d7b521209884f01bfd402c49c343e48"
prediction_resource_id = "/subscriptions/d06e41e2-ee01-4888-a67b-3b8bdcff01a1/resourceGroups/FRT-Project"
url = "https://centralindia.api.cognitive.microsoft.com/customvision/v3.0/Prediction/220fce72-9221-425c-917f-6778d57e30a6/classify/iterations/Iteration2/image"

publish_iteration_name = "Iteration2"
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
    img_path = "test-image/meningioma_tumor/image.jpg"

    #Test implemented method
    with open(img_path, "rb") as image_contents:
        results = classify(image_contents.read())
        print(results)