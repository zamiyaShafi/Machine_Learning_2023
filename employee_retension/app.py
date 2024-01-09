from flask import Flask,request,render_template
import pickle
import numpy as np


app=Flask(__name__)

with open("employee_retension.pkl","rb")as f:
    model=pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        l=[]
        hours=int(request.form.get('hours'))
        time=int(request.form.get('time'))
        promotion=int(request.form.get('promotion'))
        salary=int(request.form.get('salary'))
        l=l+[hours,time,promotion,salary]
        department=request.form.get('department')
        if department=="Department_IT":
            l=l+[1,0,0,0,0,0,0,0,0,0]
        elif department=="Department_RandD":
            l=l+[0,1,0,0,0,0,0,0,0,0]
        elif department=="Department_accounting":
            l=l+[0,0,1,0,0,0,0,0,0,0]
        elif department=="Department_hr":
            l=l+[0,0,0,1,0,0,0,0,0,0]
        elif department=="Department_management":
            l=l+[0,0,0,0,1,0,0,0,0,0]
        elif department=="Department_marketing":
            l=l+[0,0,0,0,0,1,0,0,0,0]
        elif department=="Department_product_mng":
            l=l+[0,0,0,0,0,0,1,0,0,0]
        elif department=="Department_sales":
            l=l+[0,0,0,0,0,0,0,1,0,0]
        elif department=="Department_support":
            l=l+[0,0,0,0,0,0,0,0,1,0]
        elif department=="Department_technical":
            l=l+[0,0,0,0,0,0,0,0,0,1,0]
        
        l=np.array([l])
        print(l)
        predict=model.predict(l)
        print(predict)
        if predict==[0]:
            pred="employee may not retain"
        else:
            pred="employee may retain"
        
       
            
            
        
        
        
    return render_template("predict.html",p=pred)



if __name__=="__main__":
    app.run(debug=True)