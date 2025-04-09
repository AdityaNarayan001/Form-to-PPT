# 🧠 Auto-PPT Generator from User Input

This project generates a **professional PowerPoint presentation** based on user input collected from a simple web form. It's powered by AI to refine your content, correct grammar, improve English, and add **relevant images** that visually align with the text on each slide.

---

## 🚀 Tech Stack

- **🧠 Language Model:** [Ollama Mistral](https://ollama.com/)
- **🖼️ Image Generation:** [Janus Pro AI](https://huggingface.co/deepseek-ai/Janus-Pro-7B)
- **📊 Presentation Generator:** [`python-pptx`](https://python-pptx.readthedocs.io/)
- **🧩 Frontend UI:** [Streamlit](https://streamlit.io/)
- **🐍 Backend:** Python 3.12+

---

## 🔄 Flow

1. You open a web app built using Streamlit.
2. Fill out a simple form with your startup or idea details.
3. On submit, the app:
   - Cleans and improves your input using an LLM.
   - Generates a PowerPoint presentation with structured slides.
   - Adds visuals that match the content using Janus AI.
4. You get a clean **download button** to save your .pptx file.

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/your-username/form-to-ppt.git
cd form-to-ppt
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run main.py
```