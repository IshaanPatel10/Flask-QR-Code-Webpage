from flask import Flask, render_template, request, send_file
import qrcode 
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img = None
    if request.method == 'POST':
        data = request.form['data']
        if data:
            img = qrcode.make(data)
            buf = BytesIO()
            img.save(buf)
            buf.seek(0)
            return send_file(buf, mimetype='image/png', as_attachment=False, download_name='qr.png')
    return render_template('flask_index.html')

if __name__ == '__main__':
    app.run(debug=True)