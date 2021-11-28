import time
from multiprocessing import Process

from flask import Flask, render_template

from plot_service import generate_new_plot

PLOT_NAME = "plot"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(PLOT_NAME + ".html")


@app.route('/night')
def night():
    return render_template(PLOT_NAME + "_night.html")


def plot_generation():
    while True:
        print('Starting plot generation')
        generate_new_plot("templates/" + PLOT_NAME)
        generate_new_plot("templates/" + PLOT_NAME + "_night", dark_mode=True)
        print('Plot generation sleeping...')
        time.sleep(30)


if __name__ == '__main__':
    plot_process = Process(target=plot_generation)
    plot_process.start()
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=80)
    plot_process.join()
