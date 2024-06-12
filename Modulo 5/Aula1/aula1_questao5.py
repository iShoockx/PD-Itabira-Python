import emoji

print("Emojis disponiveis: ")

print(emoji.emojize("🧠")," -",emoji.demojize("🧠"))

print(emoji.emojize("🫀")," -",emoji.demojize("🫀"))

print(emoji.emojize("🫁")," -",emoji.demojize("🫁"))

print(emoji.emojize("🦷")," -",emoji.demojize("🦷"))

print(emoji.emojize("🦴")," -",emoji.demojize("🦴"))

Frase = str(input("Digite uma frase e ela sera emojizada"))

print("Frase emojizada:",emoji.emojize(Frase))