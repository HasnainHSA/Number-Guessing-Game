# Number Guessing Game

A modern, interactive number guessing game built with Streamlit and Python. Test your luck by guessing a random number within a custom range, with adjustable difficulty levels and a sleek, animated UI that adapts to both light and dark themes.

## Features

- **Random Number Generation**: Generates a number within a user-defined range using Python's `random` module.
- **Custom Range**: Set your own minimum and maximum values.
- **Difficulty Levels**: Choose from Easy (15 attempts), Medium (10 attempts), or Hard (5 attempts).
- **Feedback**: Get hints ("Too high" or "Too low") after each guess.
- **Progress Bar**: Visualizes remaining attempts with a smooth animation.
- **Responsive UI**: Adapts to both light and dark browser themes with a trendy, glassmorphism design.
- **Animations**: Includes neon glow, floating card, and bounce effects for a modern feel.
- **Reset Option**: Start a new game after winning or losing.

## Prerequisites

- Python 3.8 or higher
- A modern web browser (Chrome, Firefox, Edge, etc.)

## Installation

1. **Clone or Download the Project**
   - Clone this repository or download the files (`app.py`, `requirements.txt`) to a local folder.

2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Navigate to the Project Folder**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser**
   - The app will automatically open in your default browser at `http://localhost:8501`.
   - Alternatively, manually navigate to `http://localhost:8501`.

## How to Play

1. **Set the Range**: Adjust the "Min" and "Max" fields to define the number range (e.g., 1 to 100).
2. **Choose Difficulty**: Select Easy, Medium, or Hard from the dropdown to set the attempt limit.
3. **Guess the Number**: Enter your guess in the input field and click "Guess!".
4. **Follow Feedback**: Use the hints ("⬆️ Nope, go higher!" or "⬇️ Whoa, too high!") to refine your guess.
5. **Win or Lose**: Guess correctly to win, or run out of attempts for a game over.
6. **Play Again**: Click "Play Again" to reset and start a new game.

## Screenshots

*(Add screenshots here if desired, e.g., via GitHub or local images)*

## Theme Support

- **Dark Mode**: Cosmic gradient background with white text and vibrant accents.
- **Light Mode**: Light gradient background with dark text, auto-detected via `prefers-color-scheme`.

Switch your browser or OS theme to see the app adapt automatically.

## Troubleshooting

- **Text Not Visible**: Ensure your browser theme matches the app's detected mode, or refresh the page.
- **Unresponsiveness**: If the app freezes, check your Streamlit version (`streamlit --version`) and update if below 1.12.0.
- **Errors**: Verify Python and dependencies are installed correctly.

## Contributing

Feel free to fork this project, submit pull requests, or suggest improvements via issues!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/).
- Inspired by modern UI trends and glassmorphism design.
```

Save this as `README.md` in your project folder. Let me know if you need any changes!