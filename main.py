import time
from termcolor import colored

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            print(colored(f"\rHello, World! {cursor}", "cyan"), end='', flush=True)
            time.sleep(0.2)  # Adjust speed of animation

if __name__ == "__main__":
    print(colored("Starting the cool animation...", "green"))
    time.sleep(1)  # Brief pause for dramatic effect
    try:
        spinning_cursor()
    except KeyboardInterrupt:
        print(colored("\nStopped by user. Goodbye!", "red"))
