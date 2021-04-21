from flask import Flask, render_template, request
import pickle
app=Flask('__name__')

@app.route('/',methods=['Post','GET'])
@app.route('/home')
def home():
    if request.method == 'POST':
        fs = request.form['FS']
        fu = request.form['FU']
        with open('my_model','rb') as f:
            model=pickle.load(f)
            result = model.predict([[fs,fu]])
            if result[0] =='YES':
               return render_template('home.html',data=['You have a Diabetes','red'])
            else:
                return render_template('home.html',data=["Congratulation you don't have Diabetes",'green'])
    else:
        return render_template('home.html')

@app.route('/about')
def abbout():
    return render_template('about.html')


if __name__ =="__main__":
    app.run(debug=True)