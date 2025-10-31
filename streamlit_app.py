import streamlit as st
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont
import io

# --- SETUP ---
st.set_page_config(page_title="Pawsonals 🐾", page_icon="🐶")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- UI HEADER ---
st.title("🐾 Pawsonals")
st.caption("Generate a witty dating profile for your pet. Because even your cat deserves a soulmate.")

# --- IMAGE UPLOAD ---
uploaded_image = st.file_uploader("Upload your pet’s photo", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, use_column_width=True)

    # --- PET INFO ---
    pet_name = st.text_input("What's your pet's name?")
    pet_breed = st.text_input("What breed (or best guess)?")
    vibe = st.selectbox("Pick their vibe:", ["Chill", "Chaotic", "Cuddly", "Diva", "Adventurous"])

import base64

if st.button("Generate Profile ✨"):
    if not pet_name:
        st.warning("Please enter your pet’s name.")
    else:
        with st.spinner("Sniffing personality..."):
            # Read and encode the image
            image_bytes = uploaded_image.read()
            image_b64 = base64.b64encode(image_bytes).decode("utf-8")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=1.0,
                messages=[
                    {
                        "role": "system",
                        "content": "You're a witty and warm pet dating profile writer. Keep it playful and concise."
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    f"This is {pet_name}, a {vibe.lower()} {pet_breed or 'pet'}.\n"
                                    "Write a short dating profile including:\n"
                                    "1. A one-sentence summary of personality.\n"
                                    "2. Three randomized playful Hinge-style prompts, each under 20 words.\n"
                                    "3. A fun fact about the breed or personality type.\n"
                                    "Keep it humorous and charming."
                                )
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_b64}"
                                }
                            }
                        ]
                    }
                ]
            )

            profile_text = response.choices[0].message.content
            st.subheader("💘 Pet Dating Profile")
            st.markdown(profile_text)

            # --- CARD GENERATION ---
            if st.button("📸 Create Shareable Card"):
                with st.spinner("Drawing up your masterpiece..."):
                    uploaded_image.seek(0)
                    img = Image.open(uploaded_image).convert("RGBA")

                    # Create overlay
                    overlay = Image.new("RGBA", img.size, (255, 255, 255, 220))
                    draw = ImageDraw.Draw(overlay)

                    # Text styling
                    font = ImageFont.load_default()
                    margin = 40
                    text_y = margin
                    wrapped_text = profile_text[:800]  # truncate for space

                    draw.text((margin, text_y), f"{pet_name} the {pet_breed}", fill="black", font=font)
                    draw.text((margin, text_y + 40), wrapped_text, fill="black", font=font)

                    combined = Image.alpha_composite(img, overlay)
                    rgb_image = combined.convert("RGB")

                    buf = io.BytesIO()
                    rgb_image.save(buf, format="JPEG")
                    byte_im = buf.getvalue()

                    st.download_button(
                        label="Download Card 🐾",
                        data=byte_im,
                        file_name=f"{pet_name.lower()}_profile.jpg",
                        mime="image/jpeg"
                    )

    if st.button("Remix Prompts 🌀"):
        with st.spinner("Reinventing personality..."):
            remix_response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=1.2,
                messages=[
                    {
                        "role": "system",
                        "content": "Generate three brand-new funny prompts for a pet dating profile, less than 20 words each."
                    },
                    {
                        "role": "user",
                        "content": f"The pet is {pet_name}, a {vibe.lower()} {pet_breed or 'pet'}."
                    }
                ]
            )
            st.markdown(remix_response.choices[0].message.content)
