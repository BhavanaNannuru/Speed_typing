# ⌨️ Typing Speed Test in Python

A simple yet effective **typing speed and accuracy tester** built using Python. This console-based project measures your **Words Per Minute (WPM)**, **accuracy**, and **response time** using a randomly chosen sentence.

---

## 🚀 Features

- Randomly displays one of several predefined sentences
- Captures the user's typing input and calculates:
  - ⏱️ Time taken
  - 🧠 Accuracy percentage
  - 🚀 Words Per Minute (WPM)
- Option to retry multiple times
- Reports total session time and memory usage
- Clean, beginner-friendly Python logic using:
  - `datetime` for time capture
  - `keyboard` for key detection
  - `math` for WPM calculation
  - `psutil` and `os` for performance metrics

---


## 🧠 How It Works

1. A sentence is randomly selected from a predefined list.
2. The user is prompted to press a key to start typing.
3. The system captures:
   - 🕒 Start and end time using `datetime`
   - 🎯 Accuracy by comparing each character
   - 🚀 Words Per Minute (WPM) using the formula:
     ```
     WPM = (((characters_typed / 5) - errors) / (time_in_seconds / 60))
     ```
4. If the input length doesn't match the expected sentence, the user is prompted to try again.
5. After typing:
   - Displays time taken, WPM, and accuracy
   - Asks if the user wants to retry
6. Once exited, it shows:
   - Total session duration
   - Memory used during execution

---

## ✅ Use Cases

- 🧪 **Typing Speed Practice**: Great for improving typing skills and tracking WPM.
- 🧑‍💻 **Beginner Python Project**: Ideal for students learning Python's standard libraries.
- ⌨️ **Keyboard Skill Benchmarking**: Check your current typing performance quickly.
- 🎓 **Interview Practice**: Useful for improving on-the-spot typing under time pressure.

---

## 🧪 Future Improvements (Ideas)

- 🖼️ **GUI Integration**: Build a desktop interface using Tkinter or PyQt.
- 📄 **External Sentence Loading**: Import sentences from a file or online source (API).
- 📊 **Session Analytics**: Show charts of performance over multiple runs.
- 🏆 **Leaderboard**: Add user scores and maintain a high-score leaderboard.
- 🌐 **Web App Version**: Convert this into a Flask or Django-based web app.
