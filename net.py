from flask import Flask,request
import debug as h
import pandas
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/job_search',methods=['GET','POST'])
def job_search():
    outStr ='''
    <html>
    <form action='/job_search' method='POST'>
        <label>What job's keyword do you want to search?</label>
        <br>
        <input type='textbox' name='keyword'>
        <button type='submit'>Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    '''



    if request.method == 'GET':
        return outStr%('')

    elif request.method =='POST':
        keyword = request.form.get('keyword')
        t = h.input_key(str(keyword))
        return outStr%('%s'%(t)) 

if __name__ == '__main__':
    #app.run(port = 5100, debug=True)

    # flask_ngrok
    app.run()



