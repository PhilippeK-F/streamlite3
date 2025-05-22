import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(page_title="Mon Application Chat", page_icon="🐱")

# Gestion de l'état de connexion
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# URLs des photos de 3 chats différents
cat_photos = [
    {
        "url": "https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_1280.jpg",
        "name": "Misty",
        "description": "Misty adore se prélasser au soleil"
    },
    {
        "url": "https://cdn.pixabay.com/photo/2015/11/16/22/14/cat-1046544_1280.jpg",
        "name": "Simba",
        "description": "Simba est un aventurier curieux"
    },
    {
        "url": "https://cdn.pixabay.com/photo/2018/01/28/12/37/cat-3113513_1280.jpg",
        "name": "Luna",
        "description": "Luna a des yeux magnifiques"
    }
]

# Page de connexion
def login_page():
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username", value="root")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if username and password:
                if username == "root" and password == "root":
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Identifiants incorrects")
            else:
                st.warning("Les champs username et mot de passe doivent être remplis")

# Page d'accueil
def home_page():
    st.title("Bienvenue sur ma page")
    st.header("Accueil")
    st.write("- Les photos de mon chat")

# Page des photos du chat
def cat_photos_page():
    st.title("Bienvenue dans l'album de mon chat")
    st.write("---")
    
    if st.button("Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    
    st.write(f"Bienvenue {st.session_state.username}")
    
    # Affichage des 3 chats avec style
    st.header("Mes trois magnifiques chats")
    
    for cat in cat_photos:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(cat["url"], width=300)
            with col2:
                st.subheader(cat["name"])
                st.write(cat["description"])
            st.markdown("---")

# Menu de navigation
def show_navigation():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Accueil", "Les photos de mon chat"],
            icons=["house", "images"],
            default_index=1 if st.session_state.get('current_page') == 'photos' else 0
        )
        
        if selected == "Accueil":
            st.session_state.current_page = 'home'
        elif selected == "Les photos de mon chat":
            st.session_state.current_page = 'photos'
        
        st.session_state.selected_page = selected

# Application principale
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        show_navigation()
        
        if st.session_state.selected_page == "Accueil":
            home_page()
        elif st.session_state.selected_page == "Les photos de mon chat":
            cat_photos_page()

if __name__ == "__main__":
    # Initialisation de la page sélectionnée
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Accueil"
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    main()
