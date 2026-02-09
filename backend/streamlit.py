import streamlit as st
import requests
import base64
import io
import re
import numpy as np
from deep_translator import GoogleTranslator
from scipy.io import wavfile

# =========== PAGE CONFIGURATION ===========
st.set_page_config(page_title="Video Dubbing Master", layout="wide")

# =========== CONSTANTS ===========
BACKEND_URL = "https://9fd1-35-204-219-191.ngrok-free.app"
SAMPLE_RATE = 24000

LANG_MAP = {
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Korean": "ko",
    "Russian": "ru"
}

# Your provided subtitle format
SUBTITLE_DATA = [
    {'text': "Now let's talk about India's oldest", 'startTime': 4.0, 'duration': 3.2},
    {'text': 'airline. It was once a symbol of', 'startTime': 5.68, 'duration': 4.16},
    {'text': 'national pride. But of late Air India', 'startTime': 7.2, 'duration': 5.12},
    {'text': 'has been in the news for its challenges', 'startTime': 9.84, 'duration': 4.56},
    {'text': 'and this week it is facing a new set of', 'startTime': 12.32, 'duration': 4.32},
    {'text': 'questions. A report was tabled in', 'startTime': 14.4, 'duration': 3.84},
    {'text': 'parliament. Its revelations are', 'startTime': 16.64, 'duration': 4.399},
    {'text': 'shocking. It says seven out of 10 Air', 'startTime': 18.24, 'duration': 4.959},
    {'text': 'India planes have recurring technical', 'startTime': 21.039, 'duration': 4.721},
    {'text': 'defects. From tray tables to cockpit', 'startTime': 23.199, 'duration': 4.721},
    {'text': 'components. The issues are varied but', 'startTime': 25.76, 'duration': 4.88},
    {'text': 'the frequency has raised eyebrows. It', 'startTime': 27.92, 'duration': 5.76},
    {'text': 'has brought safety back into focus and', 'startTime': 30.64, 'duration': 4.64},
    {'text': 'this comes at a time when the industry', 'startTime': 33.68, 'duration': 3.6},
    {'text': 'already is under pressure. From crashes', 'startTime': 35.28, 'duration': 4.32},
    {'text': 'to near misses to mass cancellations,', 'startTime': 37.28, 'duration': 4.32},
    {'text': 'Indian aviation has been going through', 'startTime': 39.6, 'duration': 4.56},
    {'text': 'too much turbulence.', 'startTime': 41.6, 'duration': 4.32},
    {'text': 'This latest report only adds to the', 'startTime': 44.16, 'duration': 4.0},
    {'text': "growing public concern about India's", 'startTime': 45.92, 'duration': 6.88},
    {'text': "aviation sector. Here's a report.", 'startTime': 48.16, 'duration': 9.039},
    {'text': ">> There is trouble in India's skies.", 'startTime': 52.8, 'duration': 4.399},
    {'text': "And at one of the country's biggest", 'startTime': 58.559, 'duration': 3.84},
    {'text': 'airlines,', 'startTime': 60.239, 'duration': 4.481},
    {'text': 'Air India is facing serious questions', 'startTime': 62.399, 'duration': 4.961},
    {'text': 'about the safety of its fleet.', 'startTime': 64.72, 'duration': 4.88},
    {'text': 'A new parliamentary report has exposed a', 'startTime': 67.36, 'duration': 4.88},
    {'text': 'shocking reality. Seven out of every 10', 'startTime': 69.6, 'duration': 5.12},
    {'text': 'Air India aircraft have recurring', 'startTime': 72.24, 'duration': 6.32},
    {'text': 'technical defects. That is right, 70% of', 'startTime': 74.72, 'duration': 6.56},
    {'text': 'the fleet. The numbers were presented in', 'startTime': 78.56, 'duration': 4.559},
    {'text': 'Parliament. They cover inspections', 'startTime': 81.28, 'duration': 5.199},
    {'text': 'carried out since January last year', 'startTime': 83.119, 'duration': 6.721},
    {'text': 'and they paint a worrying picture. 191', 'startTime': 86.479, 'duration': 7.121},
    {'text': 'of 267 aircraft operated by Air India', 'startTime': 89.84, 'duration': 6.56},
    {'text': 'Group were flagged for repeat issues.', 'startTime': 93.6, 'duration': 5.199},
    {'text': 'That includes both Air India and Air', 'startTime': 96.4, 'duration': 5.28},
    {'text': 'India Express. The inspections were', 'startTime': 98.799, 'duration': 5.68},
    {'text': 'conducted by the DGCA,', 'startTime': 101.68, 'duration': 4.32},
    {'text': 'the Directorate General of Civil', 'startTime': 104.479, 'duration': 3.841},
    {'text': "Aviation. It is India's aviation", 'startTime': 106.0, 'duration': 4.399},
    {'text': 'regulator. These were part of regular', 'startTime': 108.32, 'duration': 6.52},
    {'text': 'audits and surprise checks.', 'startTime': 110.399, 'duration': 4.441},
    {'text': 'Across all airlines, over 700 planes', 'startTime': 115.04, 'duration': 6.32},
    {'text': 'were reviewed and more than 350 had', 'startTime': 118.24, 'duration': 5.68},
    {'text': 'recurring defects. But Air India Group', 'startTime': 121.36, 'duration': 5.759},
    {'text': 'had the highest proportion, nearly 72%', 'startTime': 123.92, 'duration': 5.199},
    {'text': 'of its fleet.', 'startTime': 127.119, 'duration': 4.081},
    {'text': 'Other airlines were also affected.', 'startTime': 129.119, 'duration': 5.521},
    {'text': 'Indigo had 148 defective aircraft out of', 'startTime': 131.2, 'duration': 7.44},
    {'text': '405 inspected. SpiceJet had 16 out of', 'startTime': 134.64, 'duration': 9.679},
    {'text': '43. Accassa Air reported 14 out of 32.', 'startTime': 138.64, 'duration': 8.0},
    {'text': 'Air India says it flagged these defects', 'startTime': 144.319, 'duration': 4.56},
    {'text': 'voluntarily out of an abundance of', 'startTime': 146.64, 'duration': 5.04},
    {'text': 'caution. According to one report, most', 'startTime': 148.879, 'duration': 5.36},
    {'text': "issues are low priority and they don't", 'startTime': 151.68, 'duration': 4.48},
    {'text': 'include systems which are critical to', 'startTime': 154.239, 'duration': 5.28},
    {'text': 'safety. Air India insists these do not', 'startTime': 156.16, 'duration': 6.32},
    {'text': 'affect flight operations.', 'startTime': 159.519, 'duration': 4.961},
    {'text': 'The airline says it is already working', 'startTime': 162.48, 'duration': 4.479},
    {'text': 'on a retrofit program and targeting', 'startTime': 164.48, 'duration': 4.56},
    {'text': 'narrowbody aircraft over the next two', 'startTime': 166.959, 'duration': 4.961},
    {'text': 'years.', 'startTime': 169.04, 'duration': 5.199},
    {'text': 'The report comes at a critical time.', 'startTime': 171.92, 'duration': 4.72},
    {'text': "India's aviation sector is under heavy", 'startTime': 174.239, 'duration': 4.64},
    {'text': 'scrutiny. The pressure follows a string', 'startTime': 176.64, 'duration': 5.2},
    {'text': 'of high-profile aviation incidents.', 'startTime': 178.879, 'duration': 5.201},
    {'text': 'First the crash of an Air India plane', 'startTime': 181.84, 'duration': 5.2},
    {'text': 'last year,', 'startTime': 184.08, 'duration': 5.68},
    {'text': '>> then the chaos at Indigo which led to', 'startTime': 187.04, 'duration': 4.32},
    {'text': 'the cancellation of the thousands of', 'startTime': 189.76, 'duration': 5.32},
    {'text': 'lights within days.', 'startTime': 191.36, 'duration': 3.72},
    {'text': '>> Earlier this week, there was another', 'startTime': 197.92, 'duration': 4.239},
    {'text': 'incident on an Air India plane. A', 'startTime': 199.44, 'duration': 4.879},
    {'text': 'Dreamliner pilot flagged a suspected', 'startTime': 202.159, 'duration': 4.881},
    {'text': 'fuel control switch defect on a London', 'startTime': 204.319, 'duration': 6.0},
    {'text': 'to Bengaluru flight.', 'startTime': 207.04, 'duration': 5.759},
    {'text': 'Despite that, the aircraft continued to', 'startTime': 210.319, 'duration': 5.041},
    {'text': "operate. The UK's Civil Aviation", 'startTime': 212.799, 'duration': 4.8},
    {'text': 'Authority has now stepped in. It has', 'startTime': 215.36, 'duration': 4.0},
    {'text': 'asked for detailed records and', 'startTime': 217.599, 'duration': 3.36},
    {'text': 'explanations.', 'startTime': 219.36, 'duration': 3.84},
    {'text': 'So, what does all of this mean? Air', 'startTime': 220.959, 'duration': 4.801},
    {'text': 'India says its planes are safe, that the', 'startTime': 223.2, 'duration': 5.28},
    {'text': 'flagged issues are minor. But for', 'startTime': 225.76, 'duration': 4.88},
    {'text': 'flyers, the confidence in Indian', 'startTime': 228.48, 'duration': 5.36},
    {'text': 'aviation is being tested, not just by', 'startTime': 230.64, 'duration': 5.84},
    {'text': 'crashes or cancellations, but by the', 'startTime': 233.84, 'duration': 5.119},
    {'text': 'creeping sense that internal oversight', 'startTime': 236.48, 'duration': 5.119},
    {'text': 'is struggling to keep pace. The', 'startTime': 238.959, 'duration': 5.36},
    {'text': 'regulator is scaling up. The airlines', 'startTime': 241.599, 'duration': 5.041},
    {'text': 'are defending their record. But seven', 'startTime': 244.319, 'duration': 5.2},
    {'text': 'out of 10 planes with recurring defects', 'startTime': 246.64, 'duration': 7.04},
    {'text': 'is a number that demands attention.', 'startTime': 249.519, 'duration': 6.96}
]

# --- Helper Functions ---
def merge_subtitles(data):
    """Merges broken fragments into full sentences based on punctuation."""
    merged = []
    current_text = ""
    current_start = None
    current_duration = 0
    
    for item in data:
        if current_start is None:
            current_start = item['startTime']
        current_text += " " + item['text']
        current_duration += item['duration']
        
        if re.search(r'[.!?]$', item['text'].strip()):
            merged.append({
                'text': current_text.strip(),
                'startTime': current_start,
                'totalDuration': current_duration
            })
            current_text, current_start, current_duration = "", None, 0
            
    if current_text.strip():
        merged.append({'text': current_text.strip(), 'startTime': current_start, 'totalDuration': current_duration})
    return merged

def parse_custom_subtitles(subtitle_text):
    """Parse custom subtitles from text input.
    Expected format: Text|startTime|duration (one per line)
    """
    if not subtitle_text.strip():
        return []
    
    subtitles = []
    for line in subtitle_text.strip().split('\n'):
        line = line.strip()
        if not line or '|' not in line:
            continue
        
        try:
            parts = line.split('|')
            if len(parts) != 3:
                continue
            text = parts[0].strip()
            start_time = float(parts[1].strip())
            duration = float(parts[2].strip())
            
            if text:
                subtitles.append({
                    'text': text,
                    'startTime': start_time,
                    'duration': duration
                })
        except ValueError:
            continue
    
    return subtitles

# =========== TRANSLATION ===========
def translate_text(text: str, target_lang: str) -> str:
    """Translate text to target language."""
    return GoogleTranslator(source='auto', target=LANG_MAP[target_lang]).translate(text)

# =========== AUDIO PROCESSING ===========
def create_master_array(merged_sentences: list, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """Create master audio array with correct size."""
    final_ts = merged_sentences[-1]['startTime'] + merged_sentences[-1]['totalDuration']
    return np.zeros(int((final_ts + 2) * sample_rate), dtype=np.float32)

def normalize_audio(seg_data: np.ndarray, target_dtype=np.float32) -> np.ndarray:
    """Normalize audio data to float32."""
    if seg_data.dtype != target_dtype:
        return seg_data.astype(target_dtype) / 32768.0
    return seg_data

def overlay_audio(master_array: np.ndarray, segment: np.ndarray, start_time: float, sample_rate: int) -> np.ndarray:
    """Overlay segment audio onto master array."""
    start_idx = int(start_time * sample_rate)
    end_idx = start_idx + len(segment)
    
    if end_idx > len(master_array):
        padding = np.zeros(end_idx - len(master_array))
        master_array = np.concatenate([master_array, padding])
    
    master_array[start_idx:end_idx] = segment
    return master_array

def export_audio(master_array: np.ndarray, sample_rate: int = SAMPLE_RATE) -> bytes:
    """Export audio array as WAV bytes."""
    out_buf = io.BytesIO()
    final_wav = (master_array * 32767).astype(np.int16)
    wavfile.write(out_buf, sample_rate, final_wav)
    return out_buf.getvalue()

# =========== API INTERACTION ===========
def generate_dubbed_audio(audio_file, text: str, language: str, duration: float, ref_text: str = "") -> tuple:
    """Call backend API to generate dubbed audio.
    
    Returns: (success: bool, audio_bytes or error_msg)
    """
    files = {"file": (audio_file.name, audio_file.getvalue())}
    payload = {
        "text": text,
        "language": language,
        "total_duration": duration,
        "ref_text": ref_text
    }
    headers = {"ngrok-skip-browser-warning": "67"}
    
    try:
        res = requests.post(f"{BACKEND_URL}/generate-paced-sentence", files=files, data=payload, headers=headers)
        if res.status_code == 200:
            audio_bytes = base64.b64decode(res.json()["audio"])
            return True, audio_bytes
        else:
            return False, f"Backend error: {res.text}"
    except Exception as e:
        return False, f"Connection failed: {e}"

# =========== PROCESSING PIPELINE ===========
def process_dubbing(merged_sentences: list, audio_ref, target_lang: str, ref_text: str, use_x_vector: bool) -> tuple:
    """Main dubbing processing pipeline.
    
    Returns: (success: bool, master_audio: bytes, error_msg: str or None)
    """
    sample_rate = SAMPLE_RATE
    master_array = create_master_array(merged_sentences, sample_rate)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, sentence in enumerate(merged_sentences):
        status_text.text(f"Processing Sentence {i+1}/{len(merged_sentences)}...")
        
        # Translate text
        translated = translate_text(sentence['text'], target_lang)
        
        # Generate dubbed audio from API
        success, result = generate_dubbed_audio(
            audio_ref,
            translated,
            "auto",
            sentence['totalDuration'],
            ref_text if not use_x_vector else ""
        )
        
        if success:
            sr, seg_data = wavfile.read(io.BytesIO(result))
            seg_data = normalize_audio(seg_data)
            master_array = overlay_audio(master_array, seg_data, sentence['startTime'], sample_rate)
        else:
            return False, None, result
        
        progress_bar.progress((i + 1) / len(merged_sentences))
    
    status_text.success("Dubbing Complete!")
    master_audio = export_audio(master_array, sample_rate)
    return True, master_audio, None

# =========== UI COMPONENTS ===========
def render_sidebar() -> tuple:
    """Render sidebar and return user inputs.
    
    Returns: (audio_ref, target_lang, x_vector_mode, ref_text)
    """
    with st.sidebar:
        st.header("1. Setup")
        audio_ref = st.file_uploader("Reference Voice Audio", type=["wav", "mp3"])
        target_lang = st.selectbox("Dubbing Language", list(LANG_MAP.keys()))
        
        st.header("2. Mode")
        x_vector_mode = st.toggle("X-Vector Mode", value=True, help="Infer reference text automatically from audio.")
        ref_text = ""
        if not x_vector_mode:
            ref_text = st.text_area("Reference Text", help="Manually provide what is said in the uploaded audio.")
    
    return audio_ref, target_lang, x_vector_mode, ref_text

def render_subtitles() -> tuple:
    """Render subtitles section in main area.
    
    Returns: (use_custom_subtitles, subtitle_input)
    """
    st.header("2. Subtitles")
    use_custom_subtitles = st.checkbox("Use Custom Subtitles", value=False, help="Enter your own subtitles instead of using default data.")
    
    subtitle_input = ""
    if use_custom_subtitles:
        subtitle_input = st.text_area(
            "Enter Subtitles",
            placeholder="Format: Text|startTime|duration\nExample:\nHello world|0.0|2.5\nHow are you|2.5|2.0",
            help="Each line: subtitle text | start time (seconds) | duration (seconds)",
            height=150
        )
    
    return use_custom_subtitles, subtitle_input

def render_results(master_audio: bytes, target_lang: str, ref_audio: bytes):
    """Display results section."""
    st.divider()
    st.subheader("Final Dubbed Audio")
    st.audio(master_audio, format="audio/wav")
    
    st.download_button(
        label="📥 Download Master Audio",
        data=master_audio,
        file_name=f"dubbed_{target_lang}.wav",
        mime="audio/wav"
    )
    
    st.session_state.master_audio = master_audio
    st.session_state.ref_audio_data = ref_audio

def render_comparison(target_lang: str):
    """Display comparison section."""
    if "master_audio" not in st.session_state:
        return
    
    st.divider()
    st.subheader("📊 Comparison: Original vs Dubbed")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🗣️ Original Reference")
        st.audio(st.session_state.ref_audio_data, format="audio/wav")
        st.caption("This is the voice the AI is cloning.")
    
    with col2:
        st.markdown(f"### 🌏 {target_lang} Dub")
        st.audio(st.session_state.master_audio, format="audio/wav")
        st.caption("Paced and translated master track.")
    
    st.download_button(
        label="📥 Download Master Audio",
        data=st.session_state.master_audio,
        file_name=f"dubbed_{target_lang}.wav",
        mime="audio/wav",
        use_container_width=True
    )

# =========== MAIN APPLICATION ===========
def main():
    st.title("🎙️ AI Multilingual Video Dubber")
    st.markdown("Upload reference audio, auto-translate subtitles, and generate a paced master track.")
    
    # Render sidebar and get inputs
    audio_ref, target_lang, x_vector_mode, ref_text = render_sidebar()
    
    # Render subtitles section in main area
    use_custom_subtitles, subtitle_input = render_subtitles()
    
    st.divider()
    
    # Main processing button
    if st.button("Generate Master Dubbed Track", type="primary", use_container_width=True):
        if not audio_ref:
            st.error("Please upload a reference audio file.")
        else:
            # Load and validate subtitles
            if use_custom_subtitles:
                subtitle_data = parse_custom_subtitles(subtitle_input)
                if not subtitle_data:
                    st.error("No valid subtitles found. Please check the format: Text|startTime|duration")
                    return
            else:
                subtitle_data = SUBTITLE_DATA
            
            # Merge subtitles into sentences
            merged_sentences = merge_subtitles(subtitle_data)
            
            # Process dubbing
            success, master_audio, error = process_dubbing(merged_sentences, audio_ref, target_lang, ref_text, x_vector_mode)
            
            if success:
                render_results(master_audio, target_lang, audio_ref.getvalue())
            else:
                st.error(error)
    
    # Display comparison if available
    render_comparison(target_lang)

if __name__ == "__main__":
    main()

