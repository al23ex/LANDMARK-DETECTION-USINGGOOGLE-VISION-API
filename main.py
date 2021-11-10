from flask import *
import os
from landmark import *

app=Flask(__name__)
app.config['SECRET_KEY']='landmark'
app.config['UPLOAD_FOLDER']='H:/SEM 3/cloud lab/LANDMARK PROJECT/img'

@app.route('/',methods=['GET','POST'])
def homepage():

    if request.method=='POST':
        file=request.files['file']
        file_loc=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_loc)
        out=detect_landmarks(file_loc)
        return render_template('result.html',data=out)
    return render_template('TRY_IT_YOURSELF.html')
        
        
    
