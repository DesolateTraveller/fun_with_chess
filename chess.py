#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Template Graphics
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import chess
import chess.svg
from PIL import Image
import io

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="♟️ Chess | v0.1",
                   layout="wide",
                   #page_icon=               
                   initial_sidebar_state="collapsed")
#----------------------------------------
st.title("♟️ Chess")
st.markdown('Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>', 
            unsafe_allow_html=True)
#----------------------------------------
page_bg_img = '''
<style>
body {
    background-color: #f0f0f0;
    background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
    background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Sidebar for additional features
#---------------------------------------------------------------------------------------------------------------------------------

st.sidebar.title("Chess App Features")
st.sidebar.markdown("""
- Enter your moves in UCI format (e.g., e2e4).
- Click "Reset Board" to start a new game.
- Watch the board update in real-time as you make your moves.
""")
st.sidebar.info("Enjoy your game of chess! Feel free to contact the creator for more features or any issues.")

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------
def render_board(board):
    """Renders the chess board as an SVG image."""
    return chess.svg.board(board, size=400)

board = chess.Board()
board_ui = st.empty()

def update_board():
    svg_board = render_board(board)
    # Convert SVG to PNG for Streamlit display
    image = Image.open(io.BytesIO(svg_board.encode('utf-8')))
    board_ui.image(image, use_column_width=True)

update_board()
user_move = st.text_input("Enter your move (e.g., e2e4):")

if user_move:
    try:
        board.push_uci(user_move)
        update_board()
    except ValueError:
        st.error("Invalid move! Please enter a valid move in UCI format (e.g., e2e4).")

if st.button("Reset Board"):
    board.reset()
    update_board()




