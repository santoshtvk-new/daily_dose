# Python Daily Dose - IsMyPasswordStrong
*[As part of [pynfinity.com upcoming complete python help-guide](https://pynfinity.com/welcome/about) ]*

## 🏆 Projects Overview

Each project is developed with a goal of being:
- **Single-File**: The entire logic is implemented in a single Python file, easy to understand and deploy.
- **Self-Contained**: Minimal dependencies to ensure easy setup and execution.
- **Modular**: Focused on various Python libraries, providing opportunities for learning new modules.
- **Educational**: Helpful for both beginners and advanced developers understand core Python concepts.
- **Reusable**: Open to suggestions, cloning, or adaptable for personal use.

### Featured Projects

Here are some of the featured projects you'll find in this repository:

1. **"IsMyPasswordStrong" Both UI and CLI**  
   Take User Password and Validate its strength, score, check if it's compromised with online pwn-list, complete with a user-friendly command-line and GUI interface.
   - Libraries used: `requests`, `tkinter` *(optional with flag)*

## 🚀 Getting Started

To start using this code:

1. Clone this repository:
    ```bash
    git clone https://github.com/santoshtvk-new/daily_dose.git
    ```
   
2. Run the Python file directly:
    ```bash
    python daily_dose/IsMyPasswordStrong/IsMyPasswordStrong.py
    ```

## 🚀 Understand Code
Code can be triggered with and without GUI

1. Core function which evaluates, if we meet all required password conditions:
```python
def validations(password):
   """
     
   """
```
   
2. Run the Python file directly:
```python
def output_message(status):
  """
      Composes understandable and useful insights from shared param
      Function is responsible for only output text/message consolidation
  :param status: dictionary with following keys ['lower_case', 'upper_case', 'special_character', 'digits', 'length', 'un_pwned', 'full_un_pwned', 'no_consecutive']
  :return: message and evaluation-result to be prompted to user regarding validated password
  """
```


## 🛠️ Technologies Used

Here are some of the libraries and technologies commonly used across projects:
- **Python 3.11+**
- **tkinter**
- **requests**
- ...and more depending on the project!

## 📝 License

This repository is licensed under the MIT License. Feel free to use, modify, and distribute any part of this project.

---

Thank you for visiting! I hope you find these projects useful and educational. Feel free to reach out for feedback, collaboration, or questions.
Happy coding! 🎉
