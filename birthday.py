import time

print("🔒 A Secret Gift Is Waiting For You...")
time.sleep(2)

input("\nPress Enter to unlock your surprise... 🔑")

print("\n🎁 Preparing your gift...")
time.sleep(1)

for i in range(5, 0, -1):
    print(f"⏳ {i}")
    time.sleep(1)

print("\n📦 Opening Gift...")
time.sleep(2)

gift = [
    "🎁",
    "🎀",
    "💝"
]

for item in gift:
    print(item)
    time.sleep(0.7)

message = """

🌸━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌸

           💖 Dear Sister 💖

You are not just my sister...
You are my first best friend,
my biggest supporter,
my partner in crime,
and one of the greatest blessings in my life.

Thank you for every smile,
every laugh,
every memory,
and every moment we've shared together.

✨ May your life always be filled with:
😊 Happiness
❤️ Love
🌟 Success
💐 Good Health
🌈 Beautiful Memories
🎯 Dreams That Come True

Whenever life gets difficult,
always remember...
✨ You are stronger than you think.
✨ You are loved more than you know.
✨ You are truly special.

💌 No matter where life takes us,
you will always have a special place in my heart.

🌸 Love You Forever, My Amazing Sister! 🌸

🎉 Wishing You Endless Happiness! 🎉

🌸━━━━━━━━━━━━━━━━━━━━━━━━━━━━🌸
"""

for char in message:
    print(char, end="", flush=True)
    time.sleep(0.03)

print("\n❤️ Thank you for being the best sister in the world! ❤️")
print("🎊 Have a wonderful day! 🎊")