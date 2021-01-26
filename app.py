from flask import Flask,render_template,redirect,request
# import keras
import Flask_Caption

# __name__ == __main__
app = Flask(__name__)

@app.route("/")
def cap():
	return render_template("index.html")

@app.route("/",methods = ['POST'])
def image():
	if request.method == 'POST':
		# userfile is the name you have assigned in index.html file
		f = request.files['userfile']
		path = "./static/{}".format(f.filename) 
		f.save(path)
		caption = Flask_Caption.caption_this_image(path)
		result_dic = {
		'image':path,
		'caption':caption
		}
		# print(caption)
	return render_template("index.html",your_result=result_dic)

if __name__ == "__main__":
	app.run(threaded=False)
	# debug=Falses