import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="MCQ Generator",
    page_icon="📝"
)

st.title("📝 MCQ Generator App")
st.write("Generate multiple-choice questions using an LLM.")

@st.cache_resource
def load_model():
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

if "questions" not in st.session_state:
    st.session_state.questions = []

text = st.text_area(
    "📚 Enter your topic or study text:",
    placeholder="Enter your study text here..."
)

num_questions = st.number_input(
    "🔢 Number of questions:",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("Generate MCQs 🤖"):

    if not text.strip():
        st.warning("Please enter some study text.")

    else:

        with st.spinner("Generating MCQs..."):

            prompt = f"""
Create {num_questions} simple questions from this text.
Return only the questions, one per line.

Text:
{text}
"""

            inputs = tokenizer(
                prompt,
                return_tensors="pt",
                truncation=True,
                max_length=512
            )

            outputs = model.generate(
                **inputs,
                max_new_tokens=300
            )

            result = tokenizer.decode(
                outputs[0],
                skip_special_tokens=True
            )

        questions = [
            q.strip()
            for q in result.split("\n")
            if q.strip()
        ]

        st.session_state.questions = questions[:num_questions]

if st.session_state.questions:

    st.subheader("📋 Generated MCQs")

    for i, question in enumerate(st.session_state.questions, 1):

        st.write(f"### Q{i}. {question}")

        st.write("A) Artificial Intelligence")
        st.write("B) Machine Learning")
        st.write("C) Computer Science")
        st.write("D) Data Science")

        answer = st.radio(
            "Choose your answer:",
            ["A", "B", "C", "D"],
            key=f"answer_{i}"
        )

        if st.button(
            f"Show Answer for Q{i}",
            key=f"show_{i}"
        ):
            st.success("✅ Correct Answer: A")
            st.info(
                "Artificial Intelligence is the correct answer "
                "because it is the broader field that enables "
                "machines to perform tasks requiring human-like intelligence."
            )
            