from flask import Flask, render_template,request
import classifier

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
        predictions = classifier.classify(img)
        #First key is the result
        result = list(predictions.keys())[0]
        return render_template("result.html",result = result)
    return "Error"



app.config["TEMPLATES_AUTO_RELOAD"] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
