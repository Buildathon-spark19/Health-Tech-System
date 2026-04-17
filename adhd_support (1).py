# ==================== ADHD / Autism / PTSD / Anxiety Support Tool ====================
# Text-only version - No audio or voice processing
# Educational prototype ONLY - Not a medical device

print("=== IMPORTANT DISCLAIMER ===")
print("This is an EDUCATIONAL prototype ONLY.")
print("It is NOT a substitute for professional medical, psychological, or psychiatric care.")
print("For children with ADHD, Autism, PTSD/Trauma, or Anxiety:")
print("- Always consult qualified doctors, therapists, or psychiatrists.")
print("- Medications and interventions must be prescribed and monitored by professionals.")
print("- If the child is in crisis or has thoughts of self-harm, seek immediate help.")
print("============================\n")

# Simple emotions suitable for kids
emotions = ['calm', 'happy', 'sad', 'angry', 'fearful', 'anxious', 'neutral']

# ==================== WELLNESS TIPS & SUPPORT RESPONSES ====================
def get_support_response(emotion):
    tips = {
        "calm": "Great! You're feeling calm. Let's keep this peaceful energy going. "
                "Try a short breathing exercise: Breathe in for 4 counts, out for 6 counts.",

        "happy": "Awesome! You're feeling happy. Channel this energy into something fun like drawing, "
                "dancing, or playing with your favorite toy.",

        "sad": "It's okay to feel sad. Would you like a cozy corner with soft toys or blankets? "
                "Or maybe listen to your favorite calm song?",

        "angry": "Big angry feelings are normal. Try these safe ideas:\n"
                "• Squeeze a stress ball or pillow\n"
                "• Do 'heavy work' like pushing against a wall\n"
                "• Jump or run in place for a minute",

        "fearful": "Feeling scared or worried? Let's do grounding:\n"
                "• Name 5 things you can see\n"
                "• 4 things you can touch\n"
                "• 3 things you can hear",

        "anxious": "Feeling anxious? Try this:\n"
                "• Slow breathing\n"
                "• Hold a favorite stuffed toy\n"
                "• Think of your 'safe place' (real or imaginary)",

        "neutral": "Let's check in. How are you feeling right now?"
    }

    general_wellness = "\n\n📌 Daily Wellness Tips for Kids:\n" + \
                       "• Follow a predictable daily routine with visual schedule\n" + \
                       "• Use sensory tools (fidget toys, weighted blanket, noise-cancelling headphones)\n" + \
                       "• Take movement breaks between tasks\n" + \
                       "• Practice naming feelings using pictures or emoji charts\n" + \
                       "• Get enough sleep and playtime outdoors"

    interventions = "\n\n🛠️ Common Evidence-Based Supports (Professional Guidance Needed):\n" + \
                    "• ADHD: Behavioral parent training, school accommodations\n" + \
                    "• Autism + Anxiety: Adapted CBT with visual supports\n" + \
                    "• PTSD/Trauma: Trauma-Focused CBT (TF-CBT)\n" + \
                    "• Generalized Anxiety: Play therapy or CBT"

    medication_note = "\n\n💊 Medications: Only use medicines prescribed by a doctor " \
                      "(e.g., stimulants for ADHD, SSRIs for anxiety in some cases). " \
                      "Never start or stop without medical advice."

    base_response = f"Detected feeling: **{emotion.capitalize()}**\n\n{tips.get(emotion, tips['neutral'])}"

    return base_response + general_wellness + interventions + medication_note


# ==================== MAIN INTERACTIVE LOOP ====================
def main():
    print("\n=== Kid Support Tool - ADHD, Autism, PTSD/Trauma, Anxiety ===\n")
    print("How to use:")
    print("• Type how the child is feeling (e.g., angry, sad, anxious, calm)")
    print("• Or type 'help' to see all options")
    print("• Type 'quit' to exit\n")

    while True:
        user_input = input("How are you feeling? (or type 'quit'): ").strip().lower()

        if user_input == 'quit':
            print("Thank you for using the tool. Take care!")
            break

        elif user_input == 'help':
            print("\nAvailable feelings: calm, happy, sad, angry, fearful, anxious, neutral")
            continue

        # Match input to closest emotion
        detected_emotion = "neutral"
        for emo in emotions:
            if emo in user_input:
                detected_emotion = emo
                break

        print("\n" + "="*60)
        print(get_support_response(detected_emotion))
        print("="*60 + "\n")


if __name__ == "__main__":
    main()