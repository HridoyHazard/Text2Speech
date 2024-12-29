import asyncio
import edge_tts

async def main():
    # Configuration settings for TTS conversion
    text = (
        "এই বিষয়গুলো জানা আমাদের প্রত্যেকের জন্যই খুবই দরকার।"
    )
    voice = "bn-BD-PradeepNeural"  # Voice ID: Choose from available options
    rate = "-5%"               # Speed adjustment: e.g., +5% for faster, -10% for slower
    pitch = "+0Hz"             # Pitch adjustment: e.g., +2Hz for higher, -3Hz for lower
    output_file = "output_audio.mp3"  # File name for saving the generated audio

    # Initialize the Communicate object with the text
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)

    # Optional: Fetch and display available voices (uncomment if needed)
    # voices_manager = await edge_tts.VoicesManager.create()
    # for voice in voices_manager.voices:
    #     print(f"Voice Name: {voice['Name']}, Locale: {voice['Locale']}, Gender: {voice['Gender']}")

    try:
        print("Starting Text-to-Speech conversion...")

        # Generate speech asynchronously and save to the output file
        await communicate.save(output_file)

        print(f"TTS conversion completed successfully. Audio saved to: {output_file}")

    except Exception as e:
        # Handle any errors that occur during the TTS conversion
        print(f"An error occurred during TTS processing: {e}")

# Entry point for the script
if __name__ == "__main__":
    # Run the asyncio event loop for the main function
    asyncio.run(main())
