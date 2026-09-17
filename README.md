# 📝 AI-Powered MCQ Generator

## 📌 About

The **AI-Powered MCQ Generator** is an LLM-based application that generates multiple-choice questions from user-provided study text.

The application uses a **Large Language Model (LLM)** with a simple Streamlit interface to help students create practice questions quickly.

## ✨ Features

* 📚 Enter a topic or study text
* 🔢 Select the number of questions
* 🤖 Generate questions using an LLM
* 🔘 Multiple-choice options
* ✅ Select an answer
* 💡 View the correct answer and explanation
* 🖥️ Simple and interactive Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* FLAN-T5
* PyTorch

## 🤖 LLM Model

This project uses the **Google FLAN-T5 Small** model through the Hugging Face Transformers library.

## ⚙️ How It Works

1. The user enters study text or a topic.
2. The user selects the number of questions.
3. The application sends the text to the LLM.
4. The LLM generates questions.
5. The questions are displayed with multiple-choice options.
6. The user selects an answer.
7. The application displays the correct answer and explanation.

## 📸 Application

The application provides a simple interface for generating and answering MCQs.

![MCQ Generator Output]
<img width="806" height="489" alt="image" src="https://github.com/user-attachments/assets/3eb1c381-42ce-426f-a7d4-0e8289622ff1" />
<img width="793" height="460" alt="image" src="https://github.com/user-attachments/assets/e5d9d207-c798-48db-aa85-2c4ada136ef3" />




## 📂 Project Structure

```text
MCQ-Generator-App/
│
├── app.py
├── requirements.txt
├── README.md
└── mcq-output.png
```

## ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🎯 Purpose

This project demonstrates how **Large Language Models can be used in education** to automatically generate practice questions from study material.

## 👩‍💻 Author

**Sibiral Ruban**

B.Sc Computer Science with Artificial Intelligence
