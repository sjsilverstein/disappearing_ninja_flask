from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjaTeam():
	return render_template('ninja.html', ninja='tmnt.png')

@app.route('/ninja/<color>')
def ninjaByColor(color):
	ninja = 'notapril.jpg'
	if color == 'blue':
		ninja = 'leonardo.jpg'
		print "Ninja Turtle Leonardo"
	elif color == 'orange':
		print "Ninja Turtle Michelangelo"
		ninja = 'michelangelo.jpg'
	elif color == 'red':
		print "Ninja Turtle Raphael"
		ninja = 'raphael.jpg'
	elif color == 'purple':
		print "Ninja Turtle Donatello"
		ninja = 'donatello.jpg'
	else:
		print "Not a ninja"
	return render_template('ninja.html', ninja=ninja)

app.run(debug=True)