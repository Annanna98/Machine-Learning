import streamlit as st
import joblib
import pandas as pd

def main():
    st.title("Life expectation regression")
    newmodel = joblib.load('lifeexp_regression.pkl')
    newmodel

    x1 = st.slider('inserisci Adult Mortality:', 0., 484., 20.)
    x2 = st.slider('inserisci infant deaths',0, 910, 100)
    x3 = st.slider('inserisci Hepatitis B',0.,99., 0.2 )
    x4 = st.slider('inserisci Measles',0, 1000, 80)
    x5 = st.slider('inserisci BMI',0., 80., 12.)
    x6 = st.slider('inserisci under-five deaths',0, 1100, 200)
    x7 = st.slider('inserisci Polio',0., 100., 15.)
    x8 = st.slider('inserisci Diphtheria',0.,100., 12.)
    x9 = st.slider('inserisci HIV/AIDS',0., 10.,1.)
    x10 = st.slider('inserisci thinness 1-19 years',0., 30.,6.)
    x11 = st.slider('inserisci thinness 5-9 years',0.,30.,5.)
    x12 = st.slider('inserisci Income composition of resources',0.,1.,.2)
    x13 = st.slider('inserisci Schooling',0.,90.,9.)

    st.header('La life expectation è:')
    st.subheader(newmodel.predict([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]]))

    uploaded_file = st.file_uploader("Scegli un file",type={"csv"})
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.header('**Dataframe**')
        st.dataframe(df)

        


        
        
        st.download_button(label= 'Download file finale', data=df.to_csv().encode('utf-8'), file_name='risultato.csv', mime='text/csv')


        
       
        






if __name__ == "__main__":
    main()