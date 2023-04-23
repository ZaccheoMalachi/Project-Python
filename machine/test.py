import joblib
jim=joblib.load("student_weight_predictor.pkl")
height=int(input('HEIGHT(cm):'))
print(jim.predict([[height]]))