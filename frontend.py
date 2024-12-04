import streamlit as st
import time

def Sofia():
    st.subheader('VAI ALLA PAGINA 1')
def Malta():
    st.subheader('VAI ALLA PAGINA 2')

st.title('REGALO A VALERIA ( LA SKA MAX )')

st.subheader("COMPLIMENTI PER L'ESAME ORALE !! ORA TI MERITI UN REGALO")
st.write('Regalo da parte di Ester e Rosario 💕')

malta, sofia = False, False


if st.button('clicca per ricevere il regalo', 'RICEVI REGALO'):
    with st.spinner('Caricamento Regalo . . . 💑'):
        time.sleep(4)

    col1, col2 = st.columns(2) 

    with col1:

        st.write('Una vacanza in stile Bucarest, diciamo non troppo lontano ... 💋')
        st.write('Lontani abbastanza dal noioso turismo di massa per viverci la città insieme e in tranquillità ❤️')
        st.write('Culturale , intrigante ma economica ( avevamo in programma di visitarla )')
        st.write('La natura non manca e soprattutto , la possibilitò di provare molti cibi da cicius 👀')
        
        st.write('')
        Sofia()
            
    with col2:
        st.write('Una vacanza in un posto inaspettato . . .  ( isola )')
        st.write('Un clima sicuramente comodo per scegliere di viverla insieme in qualsiasi periodo ❤️')
        st.write('Segnata sui posti da visitare di IG ma non ne abbiamo mai parlato (ma comunque ho visto che era lì hihihi) 💋')
        st.write('Anche qui non spenderemo una fortuna ... speriamo 👀')
        
        st.write('')
        Malta()

