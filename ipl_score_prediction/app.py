from flask import Flask,render_template,request
import pickle
import numpy as np

with open('ipl_model.pkl','rb')as f:
    model=pickle.load(f)




app=Flask(__name__)

def predict_score(batting_team='Chennai Super Kings', bowling_team='Mumbai Indians', overs=5.1, runs=50, wickets=0, runs_in_prev_5=50, wickets_in_prev_5=0):
  temp_array = list()

  # Batting Team
  if batting_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Bowling Team
  if bowling_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
  temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

  # Converting into numpy array
  temp_array = np.array([temp_array])
  print(temp_array[0])

  # Prediction
  return int(model.predict(temp_array)[0])


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        bat_team=request.form.get('bat_team')
        bowl_team=request.form.get('bowl_team')
        overs=float(request.form.get('overs'))
        runs=int(request.form.get('runs'))
        wickets=int(request.form.get('wickets'))
        runs_in_5=int(request.form.get('runs_in_5'))
        wickets_in_5=int(request.form.get('wickets_in_5'))
        
        predict=predict_score(batting_team=bat_team,bowling_team=bowl_team,overs=overs,runs=runs,wickets=wickets,runs_in_prev_5=runs_in_5,wickets_in_prev_5=wickets_in_5)
        print(predict)




        
    return render_template('predict.html',pred=predict)
    



if __name__=='__main__':
    app.run(debug=True)