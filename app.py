from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    color = None

    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        height_m = height / 100  # convert cm → meters
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#00bfff"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            color = "#00ff7f"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "#ffa500"
        else:
            category = "Obese"
            color = "#ff4500"

    return render_template('index.html', bmi=bmi, category=category, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
