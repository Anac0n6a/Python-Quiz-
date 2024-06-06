# Quiz App

This is a simple quiz application built with Python and Tkinter. It reads questions from a text file, displays them to the user, and allows the user to select answers. At the end of the quiz, it shows the user's score.

## Features

- Reads questions from a file with a specific structure
- Displays questions one at a time
- Allows multiple choice answers
- Calculates and displays the final score

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Setup and Installation

1. **Clone the repository** (if using a version control system like Git):
    ```bash
    git clone https://github.com/Anac0n6a/Python-Quiz-
    cd Python-Quiz-
    ```

2. **Download the files**:
    If you are not using a version control system, download the files manually and place them in a directory.

3. **`questions_and_answers.txt` file** Should contain the following structure:
    ```
    Question #1
    Question text here...
    A. Option A
    B. Option B
    C. Option C
    D. Option D
    Correct Answer: B
    Community vote distribution
    C (55%)

    Question #2
    Another question text...
    A. Option A
    B. Option B
    C. Option C
    D. Option D
    Correct Answer: A
    Community vote distribution
    A (100%)

    ... (add more questions as needed)
    ```

4. **Run the quiz application**:
    Navigate to the directory where the script is located and run:
    ```bash
    python test_app.py
    ```

## Usage

- The quiz application will start and display the first question.
- Select one or more answers for each question.
- Click "Next" to move to the next question.
- After answering all the questions, the application will display your score as a percentage.


## Notes

- Ensure that each question in the `questions_and_answers.txt` file follows the specified structure.
- The script currently selects 90 random questions from the file for the quiz.

## Troubleshooting

- **Tkinter not installed**: If you encounter an error about Tkinter not being installed, you can install it using your package manager. For example, on Ubuntu/Debian, you can run:
    ```bash
    sudo apt-get install python3-tk
    ```
    this is installing locally via pip
    ```bash
    pip install tk
    ```
- **Encoding issues**: Ensure that the `questions_and_answers.txt` file is saved with UTF-8 encoding to avoid any character display issues.
