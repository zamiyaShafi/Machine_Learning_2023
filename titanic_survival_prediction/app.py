# flask framework->to connect both front and backend
                #   creating api ->mediater
                # request and response
                
from flask import Flask,render_template,request
import pickle
import numpy as np

# object creation
app=Flask(__name__)  


with open("titanic_prediction.pkl","rb") as f:
    model=pickle.load(f) 


# create the routing
@app.route('/') 
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict",methods=['POST'])
def predict():
   
    if request.method=='POST':
        pclass=int(request.form.get('pclass'))
        age=float(request.form.get('age'))
        fare=float(request.form.get('fare'))
        gender=[int(i) for i in request.form.get('gender')]
        print(gender)
        print(type(gender))
        print(type(pclass))
        lst=[pclass,age,fare]
        lst.extend(gender)
        print(lst)
        lst_pr=np.array([lst])
        pr=model.predict(lst_pr)
       
        if pr==[0]:
            output="Survival Possibility is less"
        else:
            output="Survival Possibility is high"
        print(output)
        
        
       
   
        
    return render_template('predict.html',op=output)
    


if __name__=='__main__':
    app.run(debug=True)

  

            
                
                