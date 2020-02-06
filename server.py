from flask import Flask, render_template
app = Flask(__name__)

from linear_regression import LineaerRegression
from make_sumple import MakeSumple

@app.route('/')
def return_hello():
    return render_template('result.html')



m = MakeSumple()
m.makesumple()
l = LineaerRegression()
l.work()


app.run(host="0.0.0.0", port=8080, debug=True)

