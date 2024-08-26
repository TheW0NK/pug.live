from flask import Flask, Response
import time

app = Flask(__name__)

frames = [
    """
    o 
    """,
    """
    oo
    """,
    """
    ooo
    """
]

def generate_animation():
    while True:
        for frame in frames:
            yield frame + "\n"
            time.sleep(0.5)  # Adjust the delay as needed

@app.route('/')
def index():
    return Response(generate_animation(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)