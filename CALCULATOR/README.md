# AI-Powered Calculator with Memory and Voice/Keyboard Input

Welcome to the **AI-Powered Calculator** project! This project aims to create a versatile, interactive calculator that leverages OpenAI's API to perform mathematical operations using natural language queries. Users can interact with the calculator using voice commands or keyboard input, and the calculator can also store previous calculations for future reference.

---

## 🚀 Features

- **Natural Language Math Query Interpretation**: Input mathematical expressions as plain text or spoken words, and the AI-powered system will handle the rest.
  
- **Voice Control and Keyboard Input**: Choose to interact with the calculator via voice commands or keyboard input, making it accessible in different use cases.
  
- **Memory Functionality**: The calculator stores previous calculations in memory, allowing users to recall, edit, or reuse past computations.
  
- **AI-Powered Expression Processing**: Using OpenAI's `gpt-3.5-turbo` model, the calculator can understand natural language queries and convert them into accurate mathematical expressions.
  
- **Error Handling**: Detects and handles invalid queries or requests gracefully.
  
- **Customizable for Future Expansion**: This project can be extended to include additional features such as graph plotting, advanced algebraic computations, and even more intuitive user interactions.

---

## 📚 How It Works

1. **Input**: Users can choose between voice or keyboard input. 
2. **Processing**: The input is processed using the OpenAI API, which converts natural language queries into a mathematical expression.
3. **Calculation**: The mathematical expression is evaluated and the result is displayed.
4. **Memory**: Calculations can be stored and retrieved for future use.

---

## 🛠 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BEIGELAKE/VOICE-CALCULATOR.git
    cd AI-Powered-Calculator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:

    - Go to [OpenAI API](https://platform.openai.com/account/api-keys) to create an API key.
    - Create a `.env` file in the project directory and add your API key:
    
    ```env
    OPENAI_API_KEY=your-openai-api-key-here
    ```

4. Run the project:

    ```bash
    python main.py
    ```

---

## 🧪 Usage

When you run the program, you will be prompted to choose your input method:
- Type `voice` to use voice commands, or `keyboard` to use text input.

For example, if you type `keyboard` and then enter a query like `6 + 9`, the AI will interpret it and return the correct result. Previous queries are also stored and can be recalled at any time.

---

## 🌟 Contributing

Contributions are welcome! Here's how you can contribute to the project:

1. Fork the repository.
2. Create a feature branch:

    ```bash
    git checkout -b feature-name
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add some feature"
    ```

4. Push the changes to your branch:

    ```bash
    git push origin feature-name
    ```

5. Open a pull request on GitHub.

### Areas for Contribution:
- **New Features**: Add new capabilities like handling more complex math operations or adding support for other input methods.
- **Bug Fixes**: Help us identify and fix bugs.
- **Code Optimization**: Refactor the existing code for better performance or readability.
- **UI Improvements**: Improve user interaction and make the calculator even more user-friendly.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com/) for providing the API that powers this project.
- All contributors who help in building and improving this calculator.

---

Thank you for checking out this project! If you find it useful, feel free to give it a star ⭐ and share it with others!
