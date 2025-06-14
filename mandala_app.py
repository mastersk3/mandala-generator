import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
import base64

# Set page config
st.set_page_config(
    page_title="Mandala Generator",
    page_icon="🕉️",
    layout="centered"
)

def generate_mandala(api_key, inspiration_word):
    """
    Generate a mandala using DALL-E based on inspiration word
    """
    try:
        # Set up OpenAI client
        client = openai.OpenAI(api_key=api_key)
        
        # Create detailed prompt for mandala generation
        prompt = f"""
        Create a detailed black and white mandala inspired by the word '{inspiration_word}'.
        The mandala should be:
        - Intricate and symmetrical
        - Black ink on white background
        - Circular geometric pattern
        - Hand-drawn artistic style
        - Incorporating elements that relate to '{inspiration_word}'
        - Suitable for meditation and coloring
        - High contrast black and white only
        """
        
        # Generate image using DALL-E
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Get the image URL
        image_url = response.data[0].url
        
        # Download the image
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        
        return image, None
        
    except Exception as e:
        return None, str(e)

def download_image(image, filename):
    """
    Convert PIL image to downloadable format
    """
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer.getvalue()

# Main app
def main():
    st.title("🕉️ Mandala Generator")
    st.markdown("Generate beautiful black and white mandalas inspired by a single word using AI")
    
    # Sidebar for API key input
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input(
            "OpenAI API Key", 
            type="password",
            help="Enter your OpenAI API key. Get one at https://platform.openai.com/api-keys"
        )
        
        st.markdown("---")
        st.markdown("### How to use:")
        st.markdown("1. Enter your OpenAI API key")
        st.markdown("2. Type an inspiration word")
        st.markdown("3. Click 'Generate Mandala'")
        st.markdown("4. Download your mandala")
        
        st.markdown("---")
        st.markdown("### Tips:")
        st.markdown("- Use meaningful words like 'peace', 'love', 'nature'")
        st.markdown("- Abstract concepts work well")
        st.markdown("- Each generation creates a unique design")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Create Your Mandala")
        
        # Input for inspiration word
        inspiration_word = st.text_input(
            "Inspiration Word",
            placeholder="Enter a word (e.g., peace, love, nature, wisdom)",
            help="This word will inspire the mandala's design and symbolism"
        )
        
        # Generate button
        generate_button = st.button(
            "🎨 Generate Mandala",
            type="primary",
            use_container_width=True
        )
    
    with col2:
        st.header("Preview")
        preview_placeholder = st.empty()
        
        if not api_key:
            with preview_placeholder.container():
                st.info("👈 Enter your API key to start")
        elif not inspiration_word:
            with preview_placeholder.container():
                st.info("👈 Enter an inspiration word")
    
    # Generation logic
    if generate_button:
        if not api_key:
            st.error("Please enter your OpenAI API key in the sidebar")
            return
        
        if not inspiration_word.strip():
            st.error("Please enter an inspiration word")
            return
        
        # Show loading state
        with st.spinner(f"Creating mandala inspired by '{inspiration_word}'..."):
            image, error = generate_mandala(api_key, inspiration_word.strip())
        
        if error:
            st.error(f"Error generating mandala: {error}")
            if "API key" in error:
                st.info("Please check that your API key is valid and has sufficient credits")
        elif image:
            # Display the generated mandala
            st.success(f"Mandala inspired by '{inspiration_word}' generated successfully!")
            
            # Create two columns for display and download
            img_col1, img_col2 = st.columns([3, 1])
            
            with img_col1:
                st.image(
                    image, 
                    caption=f"Mandala inspired by '{inspiration_word}'",
                    use_column_width=True
                )
            
            with img_col2:
                # Download button
                img_bytes = download_image(image, f"mandala_{inspiration_word.lower()}.png")
                st.download_button(
                    label="📥 Download",
                    data=img_bytes,
                    file_name=f"mandala_{inspiration_word.lower().replace(' ', '_')}.png",
                    mime="image/png",
                    type="secondary",
                    use_container_width=True
                )
                
                # Generate another button
                if st.button("🔄 Generate Another", use_container_width=True):
                    st.rerun()
            
            # Show some details
            with st.expander("ℹ️ About this Mandala"):
                st.write(f"**Inspiration:** {inspiration_word}")
                st.write(f"**Style:** Black and white geometric mandala")
                st.write(f"**Size:** 1024x1024 pixels")
                st.write(f"**Format:** PNG")
                st.write("**Usage:** Perfect for meditation, coloring, or decoration")

# Footer
def show_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; font-size: 0.8em;'>
            Made with ❤️ using Streamlit and DALL-E | 
            <a href='https://platform.openai.com/api-keys' target='_blank'>Get OpenAI API Key</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
    show_footer()