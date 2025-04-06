import streamlit as st
import random

def add_custom_css():
    st.markdown("""
    <style>
    :root {
        --primary-bg: #0f0c29;  /* Dark mode default */
        --secondary-bg: #302b63;
        --accent-color: #ff6f61;
        --text-color: #ffffff;
        --card-bg: rgba(255, 255, 255, 0.05);
        --shadow-color: rgba(255, 111, 97, 0.2);
        --input-bg: rgba(255, 255, 255, 0.1);
    }
    
    /* Light theme adjustments */
    @media (prefers-color-scheme: light) {
        :root {
            --primary-bg: #f0f0f0;
            --secondary-bg: #d9d9d9;
            --accent-color: #ff6f61;
            --text-color: #333333;
            --card-bg: rgba(0, 0, 0, 0.05);
            --shadow-color: rgba(0, 0, 0, 0.2);
            --input-bg: rgba(0, 0, 0, 0.1);
        }
    }
    
    .main {
        background: linear-gradient(45deg, var(--primary-bg) 0%, var(--secondary-bg) 50%, var(--primary-bg) 100%);
        padding: 2rem;
        min-height: 100vh;
        overflow: hidden;
    }
    
    .title {
        color: var(--accent-color);
        font-size: 3.5rem;
        text-align: center;
        font-family: 'Arial', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        animation: neonGlow 1.5s ease-in-out infinite alternate;
    }
    
    .game-card {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 600px;
        box-shadow: 0 0 20px var(--shadow-color);
        border: 2px solid var(--accent-color);
        animation: float 3s ease-in-out infinite;
    }
    
    .guess-button {
        background: var(--accent-color);
        color: var(--text-color);
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px var(--shadow-color);
    }
    
    .guess-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px var(--shadow-color);
        background: #ff867a;
    }
    
    .reset-button {
        background: #4ecdc4;
        color: var(--text-color);
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .reset-button:hover {
        transform: translateY(-3px);
        background: #63e6de;
    }
    
    .feedback {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        background: var(--input-bg);
        animation: bounceIn 0.5s ease;
        text-align: center;
        color: var(--text-color);
    }
    
    .attempts {
        color: var(--text-color);
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .progress-bar {
        width: 100%;
        background: var(--input-bg);
        border-radius: 10px;
        height: 20px;
        margin: 1rem 0;
        overflow: hidden;  /* Prevent overflow */
    }
    
    .progress-fill {
        background: var(--accent-color);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        max-width: 100%;  /* Cap the width */
    }
    
    @keyframes neonGlow {
        from { text-shadow: 0 0 5px var(--text-color), 0 0 10px var(--text-color), 0 0 15px var(--accent-color); }
        to { text-shadow: 0 0 10px var(--text-color), 0 0 20px var(--text-color), 0 0 30px var(--accent-color); }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    
    @keyframes bounceIn {
        0% { transform: scale(0.8); opacity: 0; }
        60% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); }
    }
    
    /* Style number input */
    .stNumberInput input {
        background: var(--input-bg);
        border: 2px solid var(--accent-color);
        color: var(--text-color);
        border-radius: 10px;
        padding: 0.5rem;
        text-align: center;
    }
    
    /* Style selectbox container */
    .stSelectbox [data-baseweb="select"] {
        background: var(--input-bg);
        border: 2px solid var(--accent-color);
        border-radius: 10px;
    }
    
    /* Style selectbox text and options */
    .stSelectbox [data-baseweb="select"] span,
    .stSelectbox [data-baseweb="select"] div,
    .stSelectbox [data-baseweb="select"] ul {
        color: var(--text-color) !important;
        background: var(--input-bg);
    }
    
    /* Ensure dropdown options are visible */
    .stSelectbox [data-baseweb="select"] ul {
        background: var(--card-bg);
        border: 1px solid var(--accent-color);
    }
    </style>
    """, unsafe_allow_html=True)


def init_session_state():
    if 'number' not in st.session_state:
        st.session_state.number = None
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = 10

# Game logic
def guess_number(guess, min_range, max_range):
    if st.session_state.number is None:
        st.session_state.number = random.randint(min_range, max_range)
    
    if not st.session_state.game_over:  
        st.session_state.attempts += 1
    
    if guess == st.session_state.number:
        st.session_state.game_over = True
        return f"🎉 Boom! You nailed it! The number was {st.session_state.number} in {st.session_state.attempts} attempts!"
    elif st.session_state.attempts >= st.session_state.max_attempts:
        st.session_state.game_over = True
        return f"💥 Game Over! The number was {st.session_state.number}. You're out of attempts!"
    elif guess < st.session_state.number:
        return "⬆️ Nope, go higher!"
    else:
        return "⬇️ Whoa, too high!"


def reset_game():
    st.session_state.number = None
    st.session_state.attempts = 0
    st.session_state.game_over = False

def main():
    add_custom_css()
    init_session_state()
    

    st.markdown('<h1 class="title">Guess the Number!</h1>', unsafe_allow_html=True)
    
    # Game container
    with st.container():
        
        # Settings
        col1, col2, col3 = st.columns(3)
        with col1:
            min_range = st.number_input("Min", value=1, step=1)
        with col2:
            max_range = st.number_input("Max", value=100, step=1)
        with col3:
            difficulty = st.selectbox(
                "Difficulty",
                [("Easy (15)", 15), ("Medium (10)", 10), ("Hard (5)", 5)],
                format_func=lambda x: x[0]
            )
            st.session_state.max_attempts = difficulty[1]
        

        progress = min((st.session_state.attempts / st.session_state.max_attempts) * 100, 100)
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress}%"></div>
        </div>
        """, unsafe_allow_html=True)
        

        st.markdown(f'<p class="attempts">Attempts: {st.session_state.attempts}/{st.session_state.max_attempts}</p>', unsafe_allow_html=True)
        

        guess = st.number_input("", min_value=min_range, max_value=max_range, step=1, label_visibility="collapsed")
        if st.button("Guess!", key="guess_btn", help="Take your shot!", type="primary", disabled=st.session_state.game_over):
            feedback = guess_number(guess, min_range, max_range)
            st.markdown(f'<div class="feedback">{feedback}</div>', unsafe_allow_html=True)
        

        if st.session_state.game_over:
            if st.button("Play Again", key="reset_btn", help="Start fresh!"):
                reset_game()
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()