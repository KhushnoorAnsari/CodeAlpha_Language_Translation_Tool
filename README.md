# CodeAlpha Language Translator Tool

CodeAlpha Language Translator Tool is a simple language translation application built using Python's Tkinter for the GUI and the Googletrans API for language translation. This tool allows users to input text in one language, choose a source and target language, and get a translation.

## Features

- **User-friendly GUI**: Built with Tkinter.
- **Language Translation**: Utilizes Googletrans API to translate between multiple languages.
- **Combobox Selection**: Allows users to select source and target languages from a dropdown.
- **Translation Display**: Shows the translated text in a text box.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/KhushnoorAnsari/CodeAlpha_Language_Translator_Tool.git
    ```

2. Install the required libraries:
    ```bash
    pip install googletrans==4.0.0-rc1
    pip install pillow
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Files Included

- `main.py`: The main script containing the GUI code and the translation logic.
- `README.md`: This file, with instructions on how to use the project.

## Usage

1. Run the script `main.py`.
2. Input your text in the source text box.
3. Choose the source language and the destination language from the dropdown combobox.
4. Click on **Translate** to view the translation in the destination text box.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Googletrans 4.0.0-rc1
- Pillow

## License

This project is licensed under the MIT License.

