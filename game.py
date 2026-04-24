
import random
import time

def print_banner():
    print("""
    ╔═══════════════════════════════════════╗
    ║   🎮 NUMBER GUESSING GAME 🎮          ║
    ║   Running in a Docker Container!      ║
    ╔═══════════════════════════════════════╗
    """)

def play_game():
    print_banner()
    
    print("🎯 I'm thinking of a number between 1 and 100...")
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    while True:
        try:
            guess = input("\n🤔 Your guess: ")
            
            if guess.lower() == 'quit':
                print(f"\n👋 Thanks for playing! The number was {secret_number}")
                break
                
            guess = int(guess)
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("⚠️  Please guess between 1 and 100!")
                continue
            
            if guess < secret_number:
                print("📈 Higher! Try a bigger number.")
            elif guess > secret_number:
                print("📉 Lower! Try a smaller number.")
            else:
                elapsed_time = int(time.time() - start_time)
                print(f"\n🎉 CORRECT! You found it!")
                print(f"✨ Number: {secret_number}")
                print(f"🎯 Attempts: {attempts}")
                print(f"⏱️  Time: {elapsed_time} seconds")
                
                # Calculate score
                score = max(100 - (attempts * 5) - elapsed_time, 0)
                print(f"⭐ Score: {score} points")
                
                play_again = input("\n🔄 Play again? (yes/no): ")
                if play_again.lower() in ['yes', 'y']:
                    play_game()
                else:
                    print("\n👋 Thanks for playing!")
                break
                
        except ValueError:
            print("❌ Please enter a valid number (or 'quit' to exit)")
        except KeyboardInterrupt:
            print(f"\n\n👋 Game interrupted! The number was {secret_number}")
            break

if __name__ == "__main__":
    play_game()