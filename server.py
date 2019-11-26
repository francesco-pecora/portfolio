
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_route(page_name):
    return render_template(page_name)

# writing data to a txt file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n\nEMAIL: {email},\nSUBJECT:  {subject},\nMESSAGE: {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return "Something Went Wrong"

if __name__ == '__main__':
    app.run(debug = True)