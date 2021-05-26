from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius_input>')
def display_celsius_to_fahrenheit_conversion(celsius_input=""):
    fahrenheit_input = celsius_to_fahrenheit(celsius_input)
    return "<p>Celsius input value: {}</p>" \
           "<p>Fahrenheit output value: {:.2f}</p>".format(celsius_input, fahrenheit_input)


def celsius_to_fahrenheit(celsius_input):
    celsius = float(celsius_input)
    fahrenheit = float(celsius * 9.0 / 5 + 32)
    return fahrenheit


if __name__ == '__main__':
    app.run()
