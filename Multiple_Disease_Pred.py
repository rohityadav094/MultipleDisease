import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# Loading the saved models

parkinsons_model= pickle.load(open('C:/Users/Dell/Desktop/Multiple Disease Prediction Web App/saved_models/parkinson_trained_model.sav', 'rb'))

liver_disease_model= pickle.load(open('C:/Users/Dell/Desktop/Multiple Disease Prediction Web App/saved_models/liver.pkl', 'rb'))

Kidney_disease_model= pickle.load(open('C:/Users/Dell/Desktop/Multiple Disease Prediction Web App/saved_models/kidney.pkl', 'rb'))

# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Liver Disease Prediction',
                           'Parkinson Disease Prediction',
                           'Kidney Disease Prediction'],
                           icons= ['activity','heart','person'],
                           default_index = 0)
    
# Parkinson Disease Prediction
if (selected == 'Parkinson Disease Prediction'):
        
    # Page Title
    st.title('Parkinson Disease Prediction')
    
    MDVPFoHz= st.text_input('MDVPFoHz: Pls Enter Average vocal fundamental frequency')
    MDVPFhiHz= st.text_input('MDVPFhiHz: Pls Enter Maximum vocal fundamental frequency')
    MDVPFloHz= st.text_input('MDVPFloHz: Pls Enter Minimum vocal fundamental frequency')
    MDVPJitter= st.text_input('MDVPJitter: Pls Enter measures of variation in fundamental frequency')
    MDVPJitterAbs= st.text_input('MDVPJitterAbs: Pls Enter measures of variation in fundamental frequency')
    MDVPRAP= st.text_input('MDVPRAP: Pls Enter measures of variation in fundamental frequency')
    MDVPPPQ= st.text_input('MDVPPPQ: Pls Enter measures of variation in fundamental frequency')
    JitterDDP= st.text_input('JitterDDP: Pls Enter measures of variation in fundamental frequency')
    MDVPShimmer= st.text_input('MDVPShimmer: Pls Enter measures of variation in amplitude')
    MDVPShimmerdB= st.text_input('MDVPShimmerdB: Pls Enter measures of variation in amplitude')
    ShimmerAPQ3= st.text_input('ShimmerAPQ3: Pls Enter measures of variation in amplitude')
    ShimmerAPQ5= st.text_input('ShimmerAPQ5: Pls Enter measures of variation in amplitude')
    MDVPAPQ= st.text_input('MDVPAPQ: Pls Enter measures of variation in amplitude')
    ShimmerDDA= st.text_input('ShimmerDDA: Pls Enter measures of variation in amplitude')
    NHR= st.text_input('NHR: Pls Enter ratio of noise to tonal components in the voice')
    HNR= st.text_input('HNR: Pls Enter ratio of noise to tonal components in the voice')
    RPDE= st.text_input('RPDE: Pls Enter dynamical complexity measures')
    DFA= st.text_input('DFA: Pls Enter Signal fractal scaling exponent')
    spread1= st.text_input('spread1: Pls Enter nonlinear measures of fundamental frequency variation')
    spread2= st.text_input('spread2: Pls Enter nonlinear measures of fundamental frequency variation')
    D2= st.text_input('D2: Pls Enter dynamical complexity measures')
    PPE= st.text_input('PPE: Pls Enter nonlinear measures of fundamental frequency variation')
    
    # code for prediction
    parkin_dignosis=''
    
    # creating a button for prediction
    if st.button('Parkinson Test Result'):
        parkin_prediction=parkinsons_model.predict([[MDVPFoHz,MDVPFhiHz,MDVPFloHz,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (parkin_prediction[0]==1):
            parkin_dignosis='The Person is suffering from Parkinson Disease'
            
        else:
            parkin_dignosis='The Person is not suffering from Parkinson Disease'
            
    st.success(parkin_dignosis)
            
    
    
    
# Liver Disease Prediction      
if (selected == 'Liver Disease Prediction'):
           
   # Page Title
   st.title('Liver Disease Prediction')
   
   Age= st.text_input('Age: Pls Enter Age')
   Gender = st.text_input('Gender: Pls Enter Gender')
   Total_Bilirubin= st.text_input('Total Bilirubin: Pls Enter Total Bilirubin')
   Direct_Bilirubin= st.text_input('Direct Bilirubin: Pls Enter Direct Bilirubin')
   Alkaline_Phosphotase= st.text_input('Alkaline Phosphotase: Pls Enter Alkaline Phosphotase')
   Alamine_Aminotransferase= st.text_input('Alamine Aminotransferase: Pls Enter Alamine Aminotransferase')
   Aspartate_Aminotransferase= st.text_input('Aspartate Aminotransferase: Pls Enter Aspartate Aminotransferase')
   Total_Protiens= st.text_input('Total Protiens: Pls Enter Total Protiens')
   Albumin= st.text_input('Albumin: Pls Enter Albumin')
   Albumin_Globulin_Ratio= st.text_input('Albumin and Globulin Ratio: Pls Enter Albumin and Globulin Ratio')
   
    # code for prediction
   liver_dignosis=''
    
    # creating a button for prediction
   if st.button('Liver Test Result'):
       
        input_data=([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_Globulin_Ratio]])
        # Changing input data to a numpy array
        input_data_as_numpy_array=np.asarray(input_data)
        
        # Reshape the numpy array
        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
        
        liver_prediction=liver_disease_model.predict(input_data_reshaped)
        
        
        if (liver_prediction[0]==1):
            liver_dignosis='The Person is suffering from Liver Disease'
            
        else:
            liver_dignosis='The Person is not suffering from Liver Disease'
            
   st.success(liver_dignosis)

   
           
# Kidney Disease Prediction          
if (selected == 'Kidney Disease Prediction'):
               
   # Page Title
   st.title('Kidney Disease Prediction')
   
   Age= st.text_input('Age: Pls Enter Age')
   BP = st.text_input('BP: Pls Enter Blood Pressure')
   #SG= st.text_input('SG: Pls Enter Specific Gravity')
   AL= st.text_input('AL: Pls Enter Albumin')
   SU= st.text_input('SU: Pls Enter Sugar')
   RBC= st.text_input('RBC: Pls Enter Red Blood Cells')
   PC= st.text_input('PC: Pls Enter Pus Cell')
   PCC= st.text_input('PCC: Pls Enter Pus Cell Clumps')
   BA= st.text_input('BA: Pls Enter Bacteria')
   BGR= st.text_input('BGR: Pls Enter Blood Glucose Random')
   BU= st.text_input('BU: Pls Enter Blood Urea')
   SC = st.text_input('SC: Pls Enter Serum Creatinine')
   #SOD= st.text_input('SOD: Pls Enter Sodium')
   POT= st.text_input('POT: Pls Enter Potassium')
  # HEMO= st.text_input('HEMO: Pls Enter Hemoglobin')
  # PCV= st.text_input('PCV: Pls Enter Packed Cell Volume')
   WC= st.text_input('WC: Pls Enter White Blood Cell Count')
 #  RC= st.text_input('RC: Pls Enter Red Blood Cell Count')
   HTN= st.text_input('HTN: Pls Enter Hypertension')
   DM= st.text_input('DM: Pls Enter Diabetes Mellitus')
   CAD= st.text_input('CAD: Pls Enter Coronary Artery Disease')
 #  APPET= st.text_input('APPET: Pls Enter Appetite')
   PE= st.text_input('PE: Pls Enter Pedal Edema')
   ANE= st.text_input('ANE: Pls Enter Anemia')

   
    # code for prediction
   kidney_dignosis=''
    
    # creating a button for prediction
   if st.button('Kidney Test Result'):
       input_data=([[Age,BP,AL,SU,RBC,PC,PCC,BA,BGR,BU,SC,POT,WC,HTN,DM,CAD,PE,ANE]])
       
       # Changing input data to a numpy array
       input_data_as_numpy_array=np.asarray(input_data)
        # Reshape the numpy array
       input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
        
       kidney_prediction=Kidney_disease_model.predict(input_data_reshaped)
        
        
       if (kidney_prediction[0]==1):
            kidney_dignosis='The Person is suffering from Kidney Disease'
            
       else:
            kidney_dignosis='The Person is not suffering from Kidney Disease'
            
   st.success(kidney_dignosis)
     
    
