import streamlit as st
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io
import base64

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

    # --- GENERATE PROFILE ---
    if st.button("Generate Profile ✨"):
        if not pet_name:
            st.warning("Please enter your pet’s name.")
        else:
            with st.spinner("Sniffing personality..."):
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
        with st.spinner("Designing your masterpiece..."):
            uploaded_image.seek(0)
            base_img = Image.open(uploaded_image).convert("RGB")

            # Resize to a square crop for consistency
            size = min(base_img.size)
            base_img = base_img.crop((0, 0, size, size)).resize((800, 800))

            # Create semi-transparent overlay for text
            overlay = Image.new("RGBA", base_img.size, (255, 255, 255, 180))
            draw = ImageDraw.Draw(overlay)

            # Try to load a nicer font (Streamlit Cloud usually has DejaVuSans)
            try:
                font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
                font_body = ImageFont.truetype("DejaVuSans.ttf", 28)
            except:
                font_title = ImageFont.load_default()
                font_body = ImageFont.load_default()

            # Wrap text nicely
            max_width = 45
            wrapped_profile = textwrap.fill(profile_text[:700], width=max_width)

            # Draw text on overlay
            margin = 40
            y_text = margin
            draw.text((margin, y_text), f"{pet_name} the {pet_breed}", fill="black", font=font_title)
            y_text += 60
            draw.multiline_text((margin, y_text), wrapped_profile, fill="black", font=font_body, spacing=6)

            # Composite overlay and background
            combined = Image.alpha_composite(base_img.convert("RGBA"), overlay)

            # Convert to bytes for download
            buf = io.BytesIO()
            combined.convert("RGB").save(buf, format="JPEG", quality=90)
            byte_im = buf.getvalue()

            st.image(combined, caption="Your Pet's Dating Card 💘", use_column_width=True)
            st.download_button(
                label="Download Card 🐾",
                data=byte_im,
                file_name=f"{pet_name.lower()}_pawsonals_card.jpg",
                mime="image/jpeg"
            )

    # --- REMIX PROMPTS ---
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
