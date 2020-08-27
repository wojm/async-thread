import time
from flask import Flask

app = Flask(__name__)

@app.route('/sleep/<time_to_sleep>')
def hello_world(time_to_sleep):
	time.sleep(int(time_to_sleep))
	return f'slept {time_to_sleep} seconds'

if __name__ == "__main__":
	app.run(debug=True)
