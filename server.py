import pybreaker
from flask import Flask, abort


class DBListener(pybreaker.CircuitBreakerListener):
    def state_change(self, cb, old_state, new_state):
        print(new_state)


breaker = pybreaker.CircuitBreaker(fail_max=4, reset_timeout=10, listeners=[DBListener()])
app = Flask(__name__)





@app.route("/greetings")
def hello():
    return "hello world"


@breaker
def error_method():
    raise Exception


@app.route("/error")
def error():
    error_method()


@app.errorhandler(404)
def error_404(error):
    return 'error 404'


@app.errorhandler(500)
def error_500(error):
    return 'error 500'
