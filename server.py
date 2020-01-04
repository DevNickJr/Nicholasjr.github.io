from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:path>')
def home(path):
    return render_template(path)

def write_to_text(data):
	with open('database.txt', mode='a') as database:
		database.write(f'\n{data}')
	return 'done'  

def write_to_csv(data):
	with open('database2.csv', mode='a', newline='') as database2:
	    csv_writer = csv.writer(database2, delimiter=' ',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL, )
	    fieldnames = ['email', 'subject', 'message']
	    writer = csv.DictWriter(database2, fieldnames=fieldnames)
	    writer.writerow(data)
	return 'done'  

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'something went wrong'