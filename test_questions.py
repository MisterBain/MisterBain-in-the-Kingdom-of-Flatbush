import random

def generate_flatbush_question(current_location, challenge_type, art_form=None, music_era_focus=None, involved_entity_type=None, narrative_tone=None):
    """
    Generates a storytelling question for "MisterBain and the Kingdom of Flatbush"
    based on provided parameters.
    """
    questions = []

    # --- General/Core Questions ---
    if challenge_type == "observation":
        if current_location == "Brooklyn Bridge":
            questions.append(f"As you walk across the Brooklyn Bridge, what peculiar detail about its structure or the view catches your eye, hinting at something unusual?")
        elif current_location == "A bustling Flatbush Avenue street market":
            questions.append(f"Amidst the vibrant chaos of the Flatbush Avenue market, what single, unusual object among the stalls catches your eye, and why does it feel significant?")
        elif current_location == "Prospect Park Lake":
            questions.append(f"Looking out over Prospect Park Lake, what strange ripple or unsettling reflection do you notice in the water?")

    elif challenge_type == "choice":
        if current_location == "Under the Manhattan Bridge archway in Dumbo":
            questions.append(f"Under the echoing archway of the Manhattan Bridge in Dumbo, a shadowy figure steps forward and offers you two starkly different paths. What are these paths, and which do you choose?")
        elif current_location == "A quiet brownstone stoop in Bed-Stuy":
            questions.append(f"You find a cryptic note left on a Bed-Stuy brownstone stoop, presenting you with an impossible dilemma. What is the choice, and what are its potential consequences?")

    elif challenge_type == "action":
        if current_location == "A crowded subway platform":
            questions.append(f"The subway doors are closing, but you spot a crucial clue on the platform you just left. What desperate action do you take to retrieve it?")
        elif current_location == "A hidden speakeasy":
            questions.append(f"In the secrecy of a Flatbush speakeasy, you're challenged to prove your loyalty. What action do you take to gain trust, or to deceive?")

    elif challenge_type == "reaction":
        if current_location == "Prospect Park Lake":
            questions.append(f"You're by Prospect Park Lake when suddenly, the water begins to glow with an ethereal, unnatural light. What is your immediate reaction?")
        elif current_location == "A noisy basketball court":
            questions.append(f"During a tense streetball game, a sudden, blinding flash erupts from one of the players. How do you react to this impossible event?")

    # --- Music/Arts/Camera Specific Questions ---
    if art_form == "music":
        if music_era_focus == "jazz":
            if current_location == "A dimly lit Jazz club in Flatbush":
                if involved_entity_type == "instrument":
                    questions.append(f"Inside the smoky Flatbush jazz club, the saxophone player hits a note that seems to vibrate the very air around you, revealing something hidden in the rhythm. What do you notice, or what emotion does it stir within you?")
                elif involved_entity_type == "person":
                    questions.append(f"A veteran jazz musician in the club recognizes you and offers a cryptic piece of advice in song lyrics. What do they sing, and what do you understand?")
        elif music_era_focus in ["60s_pop", "70s_funk", "80s_hiphop", "90s_rnb", "2000s_rock"]:
            if current_location == "A bustling record store in Flatbush":
                if involved_entity_type == "person":
                    questions.append(f"The eccentric owner of the Flatbush record store holds up two dusty vinyls – one a rare {music_era_focus.replace('_', ' ')} single, the other a mysterious blank disc. He says you can only take one. Which do you choose, and what do you hope to gain?")
                elif involved_entity_type == "object":
                    questions.append(f"You spot a hidden compartment behind a rack of {music_era_focus.replace('_', ' ')} records. Inside, there's a device humming softly. What does it look like, and how do you interact with it?")

    if art_form == "photography":
        if involved_entity_type == "camera":
            if current_location == "An abandoned disco roller rink (now a street art gallery)":
                questions.append(f"You're in the decaying glamour of the old Flatbush roller rink, now covered in vibrant street art, with your camera in hand. What specific detail or hidden message do you try to capture with your lens that speaks to the spirit of Flatbush?")
            elif current_location == "A lively street festival":
                questions.append(f"Amidst the vibrant chaos of a Flatbush street festival, you need to capture one defining image that encapsulates the moment. What do you frame in your camera, and what story does it tell?")

    # Fallback if no specific question is generated
    if not questions:
        return f"The story continues in {current_location}. What happens next?"

    return random.choice(questions)

# --- Test Cases ---

print("--- Test Case 1: Music-Related (Jazz) Observation ---")
q1_params = {
    "current_location": "A dimly lit Jazz club in Flatbush",
    "challenge_type": "observation",
    "art_form": "music",
    "music_era_focus": "jazz",
    "involved_entity_type": "instrument",
    "narrative_tone": "melodic"
}
print("Input Params:", q1_params)
print("Generated Question:", generate_flatbush_question(**q1_params))
print("-" * 30)

print("--- Test Case 2: Photography/Camera-Related Creative Challenge ---")
q2_params = {
    "current_location": "An abandoned disco roller rink (now a street art gallery)",
    "challenge_type": "creative_expression", # Note: Function needs to handle this 'challenge_type'
    "art_form": "photography",
    "music_era_focus": "80s_hiphop",
    "involved_entity_type": "camera",
    "narrative_tone": "gritty"
}
print("Input Params:", q2_params)
print("Generated Question:", generate_flatbush_question(**q2_params))
print("-" * 30)

print("--- Test Case 3: Character Interaction (Music Dilemma) ---")
q3_params = {
    "current_location": "A bustling record store in Flatbush",
    "challenge_type": "dilemma",
    "art_form": "music",
    "music_era_focus": "60s_pop",
    "involved_entity_type": "person",
    "narrative_tone": "intriguing"
}
print("Input Params:", q3_params)
print("Generated Question:", generate_flatbush_question(**q3_params))
print("-" * 30)

print("--- Test Case 4: General/Fallback (Not covered by specific rules yet) ---")
q4_params = {
    "current_location": "A mysterious alley behind Nostrand Ave",
    "challenge_type": "investigation",
    "narrative_tone": "suspenseful"
}
print("Input Params:", q4_params)
print("Generated Question:", generate_flatbush_question(**q4_params))
print("-" * 30)
