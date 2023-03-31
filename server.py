from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    fruit_sum = strawberry + raspberry + apple
    print(
        f"Charging {request.form['first_name']} {request.form['last_name']} for {fruit_sum} fruits")
    return render_template("checkout.html")


@app.route('/fruits')
def fruits():
    return render_template("fruits.html", )


if __name__ == "__main__":
    app.run(debug=True)
