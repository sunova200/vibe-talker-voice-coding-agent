from dotenv import load_dotenv
import os
import speech_recognition as sr
from langgraph.checkpoint.mongodb import MongoDBSaver
from .graph import create_chat_graph

load_dotenv()

MONGODB_URI = "mongodb://admin1:admin1@localhost:27017"
config = {"configurable": {"thread_id": "1"}}

def main():
    with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
        graph = create_chat_graph(checkpointer)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Say something!")
            audio = r.listen(source)
            r.pause_threshold = 0.5

        while True:
            print("Processing audio...")
            try:
                stt = r.recognize_google(audio)   # ✅ stt, recognize_google
                print("You said:", stt)

                for event in graph.stream(
                    {"messages": [{"role": "user", "content": stt}]},  # ✅ messages
                    config=config,
                    stream_mode="values"
                ):
                    if "messages" in event:                             # ✅ messages
                        event["messages"][-1].pretty_print()            # ✅ messages

            except sr.UnknownValueError:
                print("Could not understand audio — please speak clearly")
            except sr.RequestError as e:
                print(f"Speech API error: {e}")

main()


#############################___________________________________________________________##########################################################



# from dotenv import load_dotenv
# import os
# import speech_recognition as sr
# from langgraph.checkpoint.mongodb import MongoDBSaver
# from .graph import create_chat_graph
# import asyncio
# import edge_tts
# import tempfile
# import sounddevice as sd                               # ✅ Production standard
# import numpy as np
# from pydub import AudioSegment

# load_dotenv()

# MONGODB_URI = os.getenv("MONGODB_URI")
# config = {"configurable": {"thread_id": "7"}}

# async def speak(text: str):
#     communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
#         temp_path = f.name

#     await communicate.save(temp_path)

#     # ✅ Production way — sounddevice (no popups, async friendly, lightweight)
#     audio = AudioSegment.from_mp3(temp_path)
#     samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
#     samples /= 32768.0                                 # ✅ normalize audio

#     sd.play(samples, samplerate=audio.frame_rate)
#     sd.wait()                                          # ✅ waits until fully done

#     os.remove(temp_path)                               # ✅ safe cleanup after finish

# async def main():
#     with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
#         graph = create_chat_graph(checkpointer=checkpointer)

#         r = sr.Recognizer()
#         r.pause_threshold = 2

#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             print("🎙️ Vibe Talker Ready! (Ctrl+C to quit)\n")

#             while True:
#                 try:
#                     print("Listening...")
#                     audio = r.listen(source)

#                     print("Processing audio...")
#                     stt = r.recognize_google(audio)
#                     print("You said:", stt)

#                     ai_response = ""

#                     for event in graph.stream(
#                         {"messages": [{"role": "user", "content": stt}]},
#                         config,
#                         stream_mode="values"
#                     ):
#                         if "messages" in event:
#                             last_msg = event["messages"][-1]
#                             last_msg.pretty_print()
#                             ai_response = last_msg.content

#                     if ai_response:
#                         await speak(ai_response)

#                     print()

#                 except sr.UnknownValueError:
#                     print("Could not understand — please speak clearly\n")
#                 except sr.RequestError as e:
#                     print(f"Speech API error: {e}\n")
#                 except KeyboardInterrupt:
#                     print("\n👋 Vibe Talker stopped!")
#                     break

# if __name__ == "__main__":
#     asyncio.run(main())