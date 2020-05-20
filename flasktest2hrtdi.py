import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('lr.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('indexhd.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

#    output = round(prediction[0], 2)

    return render_template('indexhd.html', prediction_text=f'Person has heart disease or not: {prediction}')

if __name__ == "__main__":
    app.run()
    

