# 🐾 Pawsonals — Pet Dating Profile Generator

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991?logo=openai&logoColor=white)](https://openai.com/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

> Every pet deserves a soulmate. Every owner deserves a laugh.  
> Generate funny, AI-written dating profiles for your pets — powered by GPT-4o.

---

## 🌟 Demo

👉 **[Try Pawsonals on Streamlit Cloud](https://pawsonals-gavin.streamlit.app/)**

![Demo Screenshot](assets/demo_screenshot.png)
*(Add screenshot to `/assets/demo_screenshot.png`)*

---

## ✨ Features

- 🐕 **Upload** photos of your cat or dog  
- 💬 **Generate** a witty dating profile and 3 playful prompts  
- 🌀 **Remix** prompts for endless variety  
- 📸 **Create & Download** a shareable “Pawsonals Card” image  
- 🚀 Deploy instantly via **Streamlit Cloud**

---

## 🧠 How It Works

1. Upload a photo and describe your pet’s **vibe**  
2. The app encodes the image and sends it to **GPT-4o-mini** via the OpenAI API  
3. GPT writes a short bio and prompts based on your pet’s appearance and vibe  
4. Optionally, generate a shareable card you can post anywhere

---

## 🧩 Roadmap

- [ ] Pet breed recognition using CLIP / ViT  
- [ ] Voice memo “interpretation” (barks & meows → text)  
- [ ] Public gallery of shared pet profiles  
- [ ] Polished card templates for social media  
- [ ] Custom fine-tuned tone per breed or mood  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend / Backend | [Streamlit](https://streamlit.io/) |
| AI Model | [OpenAI GPT-4o-mini](https://platform.openai.com/docs/guides/gpt) |
| Image Handling | [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) |
| Hosting | [Streamlit Cloud](https://share.streamlit.io/) |

---

## 🚀 Getting Started

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<yourusername>/pawsonals.git
cd pawsonals
```

### 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies + add OpenAI API Key
```bash
pip install -r requirements.txt
```
### 5️⃣ Run locally
```bash
streamlit run streamlit_app.py
```

## 📸 Example Output

Meet Luna the Tabby
“I’m a cuddle enthusiast with trust issues and impeccable taste in naps.”

💬 My ideal first date is… chasing laser dots together.
💬 Most controversial opinion: Dogs are just furry extroverts.
💬 You should leave a treat if… you appreciate dramatic yawns.

## 💖 Credits

Built by Gavin Qu
 — Data scientist & builder exploring the creative side of multimodal AI.
Powered by Streamlit, OpenAI GPT-4o, and Pillow.
