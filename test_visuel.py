import streamlit as st

# Fonction principale pour l'application
def app():
    ########################################################### TITRE ###################################
    # Titre de la page principale
    st.title("Ce qu'on met dans nos assietes, quel impact sur la planète ?")
    #####################################################################################################
    # Créer une mise en page avec un conteneur de deux colonnes
    col1, col2 = st.columns([1, 4])  # col1 pour le bandeau, col2 pour le contenu principal

    # Contenu du bandeau latéral
    with col1:
        ################################################## CONTENU BANDEAU ###########################
        st.sidebar.title("Contenu")
        st.sidebar.radio("Navigation", ["Accueil", "Contexte", "Méthodologie","Analyse globale"])
        st.sidebar.write("A propos :")
        st.sidebar.write("nous étudiants et bla bla bla...")
        ########################################### CONTENU PAGE ######################################
    # Contenu principal de la page
    with col1:
        st.write("Voici le contenu de la page principale qui peut être défilé.")
    with col2:
        st.write("Ajoutez du contenu ici, des graphiques, des tableaux, etc.")
        for i in range(30):
            st.write(f"Exemple de contenu {i+1}")

# Lancer l'application
if __name__ == "__main__":
    app()
