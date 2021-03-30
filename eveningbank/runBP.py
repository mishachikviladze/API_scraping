from flask import  render_template, request, Blueprint
from pandas import DataFrame
from pycaret.regression import *

eveningbank=Blueprint('eveningbank', __name__, template_folder='templates/fortunetellerBP', static_folder='./static')   # static_url_path='eveningbank/static'


@eveningbank.route('/')
def home():
    return render_template('test.html') 

@eveningbank.route('/predict', methods=['post']) 
def predict():
    try:
        morningBank = request.form.get('morning',0)   # session['morningBank'] = request.form.get('morning')
        eveningbank = request.form.get('evening',0)   # session['eveningbank'] = request.form.get('evening')
        if  (float(eveningbank) > float(morningBank)):
            saved_final_model = load_model('eveningbank\static\Final huber Model 2021-03')
            values=pd.DataFrame(zip([float(morningBank)], [float(eveningbank)]), columns=['morning value', 'afternoon value'])
            new_prediction = predict_model(saved_final_model, data=values)
            result = round(new_prediction.iloc[0]['Label'])
            return  str(result) 
        else:
            return 'შეიტანეთ ლოგიკური ციფრები'
    except:
        return 'შეიტანეთ ლოგიკური ციფრები'


  


