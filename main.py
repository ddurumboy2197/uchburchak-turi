def uchburchak_turi(a, b, c):
    if a == b == c:
        return "Teng tomonli uchburchak"
    elif a == b or b == c or a == c:
        return "Teng yonli uchburchak"
    else:
        return "Har xil uchburchak"

# Test qilish
print(uchburchak_turi(5, 5, 5))  # Teng tomonli uchburchak
print(uchburchak_turi(5, 5, 6))  # Teng yonli uchburchak
print(uchburchak_turi(5, 6, 7))  # Har xil uchburchak
