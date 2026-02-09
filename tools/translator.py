import os
from google.cloud import translate_v2 as translate

# Set your Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "tools\gen-lang-client-0312115025-4347c6538f2e.json"

def translate_and_map(subtitles, target_lang='es'):
    """
    Translates subtitles and preserves mapping to timing data.
    """
    translate_client = translate.Client()

    # Extract texts for batch translation to preserve context/order
    texts_to_translate = [item['text'] for item in subtitles]

    # API call handles the list and returns an ordered list of results
    results = translate_client.translate(texts_to_translate, target_language=target_lang)

    # Re-map translated text to the original dictionary structure
    for i, result in enumerate(results):
        subtitles[i]['translated_text'] = result['translatedText']
        
    return subtitles

if __name__=="__main__":
    # Data Input
    data = [
        {'text': "It's a dark day in Pakistan. Another", 'startTime': 4.0, 'duration': 3.68},
        {'text': 'grim reminder of what happens to a', 'startTime': 5.92, 'duration': 3.92},
        {'text': 'country that uses terrorism as state', 'startTime': 7.68, 'duration': 3.839},
        {'text': 'policy.', 'startTime': 9.84, 'duration': 3.679}
    ]

    # Process
    translated_subs = translate_and_map(data, target_lang='hi') # Example: Hindi

    # Output Data
    for sub in translated_subs:
        print(f"Time: {sub['startTime']}s | Text: {sub['translated_text']}")