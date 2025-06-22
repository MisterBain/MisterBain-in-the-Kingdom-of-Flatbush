import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")

genai.configure(api_key=API_KEY)

# Initialize the generative model
# You can choose a different model if you prefer (e.g., 'gemini-1.5-pro-latest')
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Story Lore & Initial Prompt (as discussed) ---
# This initial prompt will define the universe for the AI
story_lore = """
The year is 2025. In the heart of Flatbush Brooklyn, ancient energies stir beneath the mundane. This vibrant borough is the deep wellspring from which the city's hidden pulse originates, and the base for MisterBain, the Sovereign of Sonic Memory and a master of Visual Thaumaturgy. His journey began not with mere luck, but as a deliberate orchestration by ancient Jazz Gatekeepers. A special agent, observing MisterBain's latent abilities through similar unseen technology, guided him through a series of trials. This culminated in a pre-arranged New York Lottery win, where the specific winning numbers were channeled to him at the right place and time, providing the resources to establish his true calling. The agent then, in the guise of a store clerk, sold him his iconic camera – a tool of Visual Thaumaturgy, akin to Mjölnir or the sunglasses from They Live. MisterBain later discovered its profound power to encapsulate the true energetic signatures of powerful, often unaware, individuals across NYC, revealing their hidden potential.

The Capsulocity Network, a clandestine collective, gathers NYC's most potent seers and sonic architects from across all five boroughs. Their combined harmony is the primary defense against unseen dissonances and negative agents. The Network is fortified by the Sonic Echoes of jazz legends like Louis Armstrong, Ella Fitzgerald, Sarah Vaughan, Duke Ellington, and James Brown, whose essence resides within the Network's deepest frequencies, ready to aid MisterBain and his bandmates.

A new villain, Gigless, is systematically ruining the New York economy and closing all venues related to traditional art and genres like Jazz. By ending these music ventures, Gigless removes the sonic healing, creativity, joy, and opportunities for the seers to perform and raise the vibration, aiming to create a "Sonic Vacuum."

Allalanda is a lost district, existing on an inter-dimensional, energetic plane. It's a sanctuary of pure frequency, accessible through a specific sonic code, where the chosen and seers can visit away from antagonists like Gigless.

---
"""

initial_scenario = """
You, as a newly 'encapsulated' member whose unique sensitivity allows you to feel the city's vast vibrations, stand with MisterBain in his makeshift studio, nestled deep within the Kingdom of Flatbush. MisterBain's latest video, documenting a vibrant block party on Nostrand Avenue, flickers with an unusual glitch – a silent crackle in the audio, a phantom shadow that shouldn't exist. It's a localized symptom of a city-wide threat, a sign the collective harmony of the Network, essential for evaporating negative agents, is weakening. The everyday bustle of the Unknowing continues across the boroughs, oblivious to the subtle weakening of New York's protective frequencies and the true villains that prey on its unseen energies.

MisterBain points to the moment in the video, his gaze distant, seeing beyond the frames, beyond Brooklyn, to the whole of NYC.

'The beat's off, my friend,' MisterBain murmurs, his voice a low thrum. 'A sour note in our symphony, reaching out from the heart of this great city. Perhaps a forgotten echo needs to be played, or a new rhythm found to restore the flow. What do you observe, and how do you propose we address this nascent disharmony, before it unravels the very chords of Flatbush and beyond?'

What do you do?
1.  Examine the video footage closely, focusing on the 'glitch'.
2.  Access the Capsulocity Network's encrypted archives.
3.  Venture out into Flatbush to seek a local manifestation of this widespread disharmony.
"""

# --- Game Loop ---
def start_game():
    print("Welcome to The Harmonic Vigil!")
    print("-" * 40)

    # Initialize conversation history with the lore and initial scenario
    # This helps the AI remember the context throughout the game
    global chat_history
    chat_history = [
        {'role': 'user', 'parts': [story_lore]},
        {'role': 'model', 'parts': ["Understood. I am ready to facilitate a story within these parameters."]},
        {'role': 'user', 'parts': [initial_scenario]}
    ]

    # Display the initial scenario
    print(initial_scenario)

    while True:
        player_choice = input("\nYour action: ").strip()

        # Exit condition (for testing)
        if player_choice.lower() == 'quit':
            print("The Harmonic Vigil concludes for now. Farewell!")
            break

        # Append player's choice to history
        chat_history.append({'role': 'user', 'parts': [f"Player's action: {player_choice}\n\nContinue the story, keeping the tone and lore consistent. Introduce the next scene or dialogue and offer 2-3 new, distinct choices for the player's next action."]})

        try:
            # Generate AI response
            # Using stream=True for real-time output (optional, but good for longer responses)
            response = model.start_chat(history=chat_history).send_message(player_choice, stream=True)

            print("\n" + "=" * 40)
            print("MISTERBAIN'S REALM RESONATES...")
            print("=" * 40)
            generated_text = ""
            for chunk in response:
                generated_text += chunk.text
                print(chunk.text, end='', flush=True) # Print as it's generated
            print() # New line after the streamed output

            # Append AI's response to history
            chat_history.append({'role': 'model', 'parts': [generated_text]})

        except Exception as e:
            print(f"\nAn error occurred while generating response: {e}")
            print("Please try again or check your API key/internet connection.")
            # Optionally, you could try to pop the last user choice to prevent
            # sending a problematic prompt again
            if chat_history and chat_history[-1]['role'] == 'user':
                chat_history.pop()

# --- Run the game ---
if __name__ == "__main__":
    start_game()
