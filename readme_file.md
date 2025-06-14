# 🕉️ Mandala Generator

A beautiful web application that generates black and white mandalas inspired by single words using AI.

## Features

- **AI-Powered Generation**: Uses OpenAI's DALL-E 3 to create unique mandalas
- **Single Word Inspiration**: Enter any word to inspire your mandala design
- **Black & White Art**: Creates intricate geometric patterns perfect for meditation
- **Download Ready**: High-quality PNG downloads (1024x1024)
- **Secure**: API key input is handled securely without storage

## How to Use

1. **Get an OpenAI API Key**: Visit [OpenAI Platform](https://platform.openai.com/api-keys) to get your API key
2. **Enter Your API Key**: Paste it in the sidebar (it's not stored anywhere)
3. **Choose an Inspiration Word**: Words like "peace", "nature", "wisdom" work great
4. **Generate**: Click the generate button and wait for your unique mandala
5. **Download**: Save your mandala as a PNG file

## Local Development

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/mandala-generator.git
cd mandala-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run mandala_app.py
```

4. Open your browser to `http://localhost:8501`

## Deployment

This app is deployed on Streamlit Cloud. You can access it at: [Your App URL]

## Technologies Used

- **Frontend**: Streamlit
- **AI Model**: OpenAI DALL-E 3
- **Image Processing**: Pillow (PIL)
- **HTTP Requests**: Requests library

## Tips for Best Results

- Use meaningful, abstract words for inspiration
- Words related to emotions, nature, or concepts work well
- Each generation creates a completely unique design
- Perfect for meditation, coloring, or wall art

## Privacy & Security

- API keys are never stored or logged
- All processing happens in real-time
- No user data is retained between sessions

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ using Streamlit and OpenAI DALL-E