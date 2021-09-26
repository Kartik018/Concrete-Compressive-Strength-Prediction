from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('random_forest_regression.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        cement=float(request.form['cement'])
        blast_furnace_slag=float(request.form['blast_furnace_slag'])
        fly_ash=float(request.form['fly_ash'])
        water=float(request.form['water'])
        superplasticizer=float(request.form['superplasticizer'])
        coarse_aggregate=float(request.form['coarse_aggregate'])
        fine_aggregate=float(request.form['fine_aggregate'])
        age=int(request.form['age'])
        
        prediction=model.predict([[cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]]) 
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Sorry can't predict")
        else:
            return render_template('index.html',prediction_text="Concrete compressive strength is {}Mpa".format(output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)