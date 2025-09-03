# ✅↓ Write your code here ↓✅
def sing():
    letra = ""
    for i in range (11):
        if i == 4:
            letra += "there will be an answer,\n"
        elif i == 10:
            letra += "whisper words of wisdom, let it be"
        else:
            letra += "let it be,\n"
    return letra

sing()