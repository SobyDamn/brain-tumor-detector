from flask import Flask, render_template,request
import classifier
from base64 import b64encode, encode
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        #get image from form data
        img = request.files['scan_file']
        #Classify the image
        predictions = classifier.classify(img) #Result in dict

        #get the image data to display it on result page
        img_data = Image.open(img)
        #resize the image
        #img_data = img_data.resize((300,300))
        buffered = BytesIO()
        img_data.save(buffered, format="JPEG")
        #encoded data in base64
        encoded = b64encode(buffered.getvalue())
        uri = f"data:image/jpeg;base64,{encoded.decode('UTF-8')}" #URI to be displayed on result page

        #First key is the result
        result = list(predictions.keys())[0]
        data = {}
        data["uploaded_image"] = uri
        data['result'] = classifier.tumors[result]['name']
        data['about'] = classifier.tumors[result]['about']
        data["predictions"] = []
        for key,value in predictions.items():
            data["predictions"].append({'name':key,'probability':round(value,2)})

        return render_template("result.html",data = data)
    return "Forbidden Request"



app.config["TEMPLATES_AUTO_RELOAD"] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
