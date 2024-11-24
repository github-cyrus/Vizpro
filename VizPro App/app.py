from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart', methods=['POST'])
def chart():
    try:
        # Retrieve user input
        values = request.form.get('values')
        # Convert the comma-separated string into a list of integers
        values = list(map(int, values.split(',')))
        
        # Generate the chart
        img = io.BytesIO()
        plt.figure(figsize=(10,6))
        plt.plot(values, marker='o')
        plt.title('User Input Chart')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.grid(True)
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        return render_template('chart.html', plot_url=plot_url)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
