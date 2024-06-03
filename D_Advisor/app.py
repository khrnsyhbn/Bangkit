from flask import Flask, render_template
from models import algorithm_ml
from datetime import date

application = Flask(__name__)

content = '''D-Advisor (Diagnosis Advisor) is a <em>self-diagnosis program</em> using <em>machine learning algorithms</em> that aims to address the problem of lack of accessibility of medical information that can be understood easily and quickly. 
As interest in self-care and disease prevention increases, there is a greater demand for information on <em>disease symptoms, early diagnosis, and preventive measures</em>. D-Advisor can serve as a tool that helps individuals understand their symptoms, 
identify potential diseases, and take appropriate preventive measures. D-Advisor focuses on addressing the medical information gap that often confuses the general public.'''

@application.route('/')
def index():
    #Membuat objek dari kelas algorithm_ml
    model = algorithm_ml()
    
    #Memuat nilai kedalam model
    model.setTitle('D-Advisor (Diagnosis Advisor)')
    model.setContent(content)
    model.setDate(date.today())


    #Mengirim value ke view
    return render_template('index.php', 
        judul = model.getTitle(),
        tanggal = model.getDate(),
        isi = model.getContent())

@application.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    application.run(debug=True)