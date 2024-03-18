from flask import Flask, render_template, request
import fancytexts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    mylist = ["af", "scf", "cf", "dsf", "bf", "ff", "bff", "ffd", "mfd", 
          "bfd", "rfd", "bbfd", "bsfd", "hwfd", "sfd", "bfds", "ifds",
            "bifd", "mofd", "sofd", "hiafd", "spfd", "sqfd", "blfd",
              "ticfd", "blsfd", "fs1f", "fs2f", "fs3f", "syfd"]
    #result1="<table><tr>"
    result1=""
    for listq in mylist:
        StyleCode = listq
        text = request.form['text']
        result1 +=fancytexts.fancytext(StyleCode, text) + '\n'
       # result1 += result1.replace('\n', '<br>')
    #result1 +="</tr></table>"
    return render_template('result.html', result=result1)

if __name__ == '__main__':
    app.run(debug=True)
