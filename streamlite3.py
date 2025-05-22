import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'root',
            'password': 'root',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
      st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")


if st.session_state["authentication_status"]:
  accueil()

# Création de 3 colonnes 
col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
with col2:
  st.header("A cat")
  st.image("https://imgs.search.brave.com/mGmdo8ibmzFiwa9AmRm5qk-gb6cJSHY9OGJgQu97UW0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQ0/MzU2Mjc0OC9mci9w/aG90by9taWdub24t/Y2hhdC1naW5nZW1i/cmUuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPXlnTlZWbnFM/azlWOEJXdTRWUTBE/MjF1Ny1kYUl5SFVv/eUtsQ2N4M0sxRTg9")

# Contenu de la troisième colonne : 
with col3:
  st.header("A cat")
  st.image("https://imgs.search.brave.com/1Ct9Tb0CtT0ZpfAjofmF86YkZdvXrdXCsJd9jqeSWZU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cGhvdG9zLWdyYXR1/aXRlL2NoYXQtbWln/bm9uLWZhaXNhbnQt/YWN0aXZpdGUtaHVt/YWluZV8yMy0yMTUx/ODc2NDA1LmpwZz9z/ZW10PWFpc19oeWJy/aWQmdz03NDA")


  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


