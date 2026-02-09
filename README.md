# Video Dubbing Master

A comprehensive Streamlit-based application for dubbing and translating videos into multiple languages. This tool extracts subtitles from YouTube videos, translates them to your target language, and generates dubbed audio using advanced AI.

## Features

- **YouTube Integration**: Extract subtitles directly from YouTube videos
- **Multi-Language Support**: Dub videos into 8 different languages:
  - Hindi
  - Chinese (Simplified)
  - Japanese
  - Spanish
  - French
  - German
  - Korean
  - Russian
- **AI-Powered Translation**: Uses Google Cloud Translation API for accurate subtitle translation
- **Audio Dubbing**: Generates natural-sounding dubbed audio synchronized with original video timing
- **Web Interface**: User-friendly Streamlit interface for easy access

## Project Structure

```
ai_summit/   
├── frontend/
│   └── streamlit.py                  
├── backend/                                
│   └── backend.ipynb
└── README.md
```

## Components

### 1. streamlit.py

The frontend of web application that:
- Provides a user interface for audio dubbing
- Manages language selection
- Displays original and dubbed content
- Configures page settings and language mappings

## Prerequisites

- Python 3.7+
- Streamlit
- Deep Translator library
- SciPy (for audio processing)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai_summit
```

2. Install dependencies:
```bash
pip install streamlit google-cloud-translate youtube-transcript-api deep-translator scipy numpy requests
```

3. Set up Google Cloud credentials:
   - Place your Google Cloud service account JSON file in the `tools/` directory
   - Update the path in `translator.py` if needed

## Usage

1. Start the Streamlit application:
```bash
streamlit run streamlit.py
```

2. Open your browser and navigate to the local Streamlit URL (typically `http://localhost:8501`)

3. Enter a YouTube video URL

4. Select your target language for dubbing

5. Click process to generate dubbed content

## Subtitle Format

Subtitles are structured as follows:
```python
{
    'text': 'Subtitle text',
    'startTime': 4.0,           # Start time in seconds
    'duration': 3.2             # Duration in seconds
}
```

## API Backend

The application connects to a backend API for audio processing:
- **Backend URL**: `https://9fd1-35-204-219-191.ngrok-free.app`
- **Sample Rate**: 24000 Hz

## Configuration

Key settings in `streamlit.py`:
- `Page Title`: "Video Dubbing Master"
- `Layout`: Wide
- `Sample Rate`: 24000 Hz
- `Supported Languages`: Hindi, Chinese, Japanese, Spanish, French, German, Korean, Russian

## Future Enhancements

- Support for additional languages
- Local TTS engine integration
- Video download and hosting capabilities
- Batch processing for multiple videos
- Custom voice selection

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

For issues or questions, please contact [your contact information]

