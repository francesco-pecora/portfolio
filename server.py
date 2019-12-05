from database_library import define_database, insert_query
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_route(page_name):
    return render_template(page_name)

def write_to_database(data):
    db = define_database()
    insert_query(db, str(data['email']), str(data['subject']), str(data['message']))

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # making sure we receive data
            if(data['email'] and data['subject'] and data['message']):
                #write_to_database(data)
                return redirect('thankyou.html')
            else:
                return render_template("contact.html")
        except:
            return "No data sent to the server..."
    else:
        return "Something Went Wrong"

if __name__ == '__main__':
    app.run(debug = True)