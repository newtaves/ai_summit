from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url:str):
    # Extract the video id from url
    import re
    patterns = [
        r"(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url


def get_subtitles(url:str):
    """
    Returns the subtitles of a Youtube video as a string.
    
    Args:
        url: Url of the Youtube video
        example: "https://www.youtube.com/watch?v=CKS1glzmDVc"
    Returns:
        A dictionary with a "status" key indicating success or error, and a "subtitles" key containing the subtitles if successful.
        Success: {"status":"success","subtitles":<subtitles_string>}
        Error: {"status":"error","message":<error_message>}

    """
    vid_id = extract_video_id(url)

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(vid_id)
    output = {"status":"success", "subtitles":[]}

    # is iterable
    for snippet in fetched_transcript:
        output["subtitles"].append(
            {
                "text":snippet.text,
                "startTime":snippet.start,
                "duration":snippet.duration
            }
        )
    if not output["subtitles"]:
        output["status"]="error"
        output["message"]="No subtitles found!"
        return output 
    return output


if __name__ == "__main__":
    url = input("Enter the youtube url: ")
    subtitles = get_subtitles(url)
    script = ""
    for i in subtitles["subtitles"]:
        # script+="|"+i["text"]
        print(i)
    # print(len(script))
    for i in script.split("."):
        print(i)