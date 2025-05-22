import streamlit as st
from streamlit_authenticator import Authenticate

# Titre de l'application
st.title("Application Streamlit avec Barre latérale")

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'root',
            'password': 'root',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Configuration de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",         # Le nom du cookie, un str quelconque
    "cookie_key",          # La clé du cookie, un str quelconque
    30                     # Le nombre de jours avant que le cookie expire
)

# Authentification dans la barre latérale
name, authentication_status, username = authenticator.login('Login', 'sidebar')

# Gestion des états d'authentification
if authentication_status:
    # Utilisateur connecté
    st.sidebar.success(f"Bienvenue, {name} !")
    
    # Barre latérale avec des boutons
    page = st.sidebar.selectbox("Choisissez une page", ["Bienvenue", "Photos"])

    # Page de bienvenue
    if page == "Bienvenue":
        st.header("Page de Bienvenue")
        st.write("Bienvenue dans l'application Streamlit !")
        st.write("Cliquez sur 'Photos' dans la barre latérale pour voir les images.")

    # Page avec des photos
    elif page == "Photos":
        st.header("Page des Photos")
        st.write("Voici quelques images :")

        # Création de 3 colonnes
        col1, col2, col3 = st.columns(3)

        # Contenu de la première colonne
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        # Contenu de la deuxième colonne
        with col2:
            st.header("A cat")
            st.image("https://imgs.search.brave.com/mGmdo8ibmzFiwa9AmRm5qk-gb6cJSHY9OGJgQu97UW0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQ0/MzU2Mjc0OC9mci9w/aG90by9taWdub24t/Y2hhdC1naW5nZW1i/cmUuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPXlnTlZWbnFM/azlWOEJXdTRWUTBE/MjF1Ny1kYUl5SFVv/eUtsQ2N4M0sxRTg9")

        # Contenu de la troisième colonne
        with col3:
            st.header("A cat")
            st.image("https://imgs.search.brave.com/1Ct9Tb0CtT0ZpfAjofmF86YkZdvXrdXCsJd9jqeSWZU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cGhvdG9zLWdyYXR1/aXRlL2NoYXQtbWln/bm9uLWZhaXNhbnQt/YWN0aXZpdGUtaHVt/YWluZV8yMy0yMTUx/ODc2NDA1LmpwZz9z/ZW1")