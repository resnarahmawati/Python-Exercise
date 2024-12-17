import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}")
        time.sleep(1)
        seconds -= 1
    print("Waktu habis!")

time_in_seconds = int(input("Masukkan waktu (detik): "))
countdown(time_in_seconds)
