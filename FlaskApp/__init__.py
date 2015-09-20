from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():

	try:
		title = "Welcome to my homepage!"
		paragraph = ["I am a biomedical researcher with object-oriented programming, database and machine learning experiences pursuing continued higher education in computer science."]
		return render_template("home.html", title = title, paragraph = paragraph )
	except Exception, e:
		return str(e)
		
@app.route('/skills')
def skillpage():
	title = "Technical Skills"
	paragraph = ["- Languages: fluent in Python, Java, C#; experience with C, R and SQL", 
	"- Tools: Pandas, NumPy, scikit-learn, matplotlib, PyBrain, Git, BWA, bowtie, samtools ", 
	"- Modelling: supervised learning, clustering, randomized optimization", 
	"- Web application: MVC pattern, Entity Framework, HTML/CSS/Javascript, Python Flask"]

	return render_template("index.html", title = title, paragraph = paragraph)

@app.route('/publications')
def coursepage():
	title = ""
	paragraph = [""]
	return render_template("publications.html", title = title, paragraph = paragraph)
	
@app.route('/research')
def researchpage():
	title = "My Research"
	paragraph = [""]
	return render_template("research.html", title = title, paragraph = paragraph)
	
@app.route('/projects')
def projectpage():
	title = "Selected Projects"
	paragraph = [""]
	return render_template("project.html", title = title, paragraph = paragraph)

@app.route('/course')
def experiencepage():
	title = "Related Courses"
	paragraph = [""]
	return render_template("course.html", title = title, paragraph = paragraph)
	
@app.route('/slides')
def slides():
	title = "Healthy Beats"
	paragraph = [""]
	#pageType = 'about'
	
	return render_template("slides.html", title = title, paragraph = paragraph)

@app.route('/healthybeats')
def healthybeats():
	#title = ""
	#paragraph = [""]
	return render_template("healthybeats.html")

@app.route('/xpx')
def xpx():
	return render_template("xpx.html")
		


        
if __name__ == "__main__":
    app.run()

