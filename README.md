# Video Dubbing Master

A comprehensive Streamlit-based application for dubbing and translating videos into multiple languages. This tool extracts subtitles from YouTube videos, translates them to your target language, and generates dubbed audio using advanced AI.

## Examples

| Reference Audio | Subtitles | Translated Languages |
|:---------------:|-----------|---------------------|
| Sample WAV | English News Transcript | Russian, Hindi, German |

### 🔊 Reference Audio
▶️ [Play Russian Audio](public/russian.wav)

---

### 📝 Subtitles (Original)

Now let's talk about India's oldestairline. It was once a symbol ofnational pride. But of late Air Indiahas been in the news for its challengesand this week it is facing a new set ofquestions. A report was tabled inparliament. Its revelations areshocking. It says seven out of 10 AirIndia planes have recurring technicaldefects. From tray tables to cockpitcomponents. The issues are varied butthe frequency has raised eyebrows. Ithas brought safety back into focus andthis comes at a time when the industryalready is under pressure. From crashesto near misses to mass cancellations,Indian aviation has been going throughtoo much turbulence.This latest report only adds to thegrowing public concern about India'saviation sector. Here's a report.>> There is trouble in India's skies.And at one of the country's biggestairlines,Air India is facing serious questionsabout the safety of its fleet.A new parliamentary report has exposed ashocking reality. Seven out of every 10Air India aircraft have recurringtechnical defects. That is right, 70% ofthe fleet. The numbers were presented inParliament. They cover inspectionscarried out since January last yearand they paint a worrying picture. 191of 267 aircraft operated by Air IndiaGroup were flagged for repeat issues.That includes both Air India and AirIndia Express. The inspections wereconducted by the DGCA,the Directorate General of CivilAviation. It is India's aviationregulator. These were part of regularaudits and surprise checks.Across all airlines, over 700 planeswere reviewed and more than 350 hadrecurring defects. But Air India Grouphad the highest proportion, nearly 72%of its fleet.Other airlines were also affected.Indigo had 148 defective aircraft out of405 inspected. SpiceJet had 16 out of43. Accassa Air reported 14 out of 32.Air India says it flagged these defectsvoluntarily out of an abundance ofcaution. According to one report, mostissues are low priority and they don'tinclude systems which are critical tosafety. Air India insists these do notaffect flight operations.The airline says it is already workingon a retrofit program and targetingnarrowbody aircraft over the next twoyears.The report comes at a critical time.India's aviation sector is under heavyscrutiny. The pressure follows a stringof high-profile aviation incidents.First the crash of an Air India planelast year,>> then the chaos at Indigo which led tothe cancellation of the thousands oflights within days.>> Earlier this week, there was anotherincident on an Air India plane. ADreamliner pilot flagged a suspectedfuel control switch defect on a Londonto Bengaluru flight.Despite that, the aircraft continued tooperate. The UK's Civil AviationAuthority has now stepped in. It hasasked for detailed records andexplanations.So, what does all of this mean? AirIndia says its planes are safe, that theflagged issues are minor. But forflyers, the confidence in Indianaviation is being tested, not just bycrashes or cancellations, but by thecreeping sense that internal oversightis struggling to keep pace. Theregulator is scaling up. The airlinesare defending their record. But sevenout of 10 planes with recurring defectsis a number that demands attention. 

---

### 🌍 Translated Audio Outputs

**Russian**
<audio src="public/russian.wav" controls></audio>

**Hindi**
<audio src="public/hindi.wav" controls></audio>

**German**
<audio src="public/german.wav" controls></audio>

---

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




