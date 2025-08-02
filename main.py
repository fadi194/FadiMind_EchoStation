import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"diary_{today}.txt"

with open(filename, "a", encoding="utf-8") as file:
    text = input("📝 اكتب مشاعرك اليوم: ")
    file.write(text + "\n")

print(f"✔️ تم حفظ صدى اليوم في: {filename}")
