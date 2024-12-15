from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def video_to_audio_converter(input_video_path, output_audio_path):
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_video_path)
        
        # Extract audio from the video clip
        audio_clip = video_clip.audio
        
        # Convert audio clip to AudioSegment for export
        audio_segment = AudioSegment.from_file(audio_clip, format="mp3")
        
        # Export the audio segment to the desired output path
        audio_segment.export(output_audio_path, format="mp3")
        
        print(f"Conversion completed. Audio saved at {output_audio_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Example Usage:
    input_video_path = "example_video.mp4"
    output_audio_path = "output_audio.mp3"
    video_to_audio_converter(input_video_path, output_audio_path)
