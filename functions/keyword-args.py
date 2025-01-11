def full_name(firstname: str, lastname: str) -> str:
    return f"Your name is {firstname} {lastname}"

sonuc = full_name("Bilal","Sevinc")
sonuc = full_name(lastname="Sevinc",firstname="Bilal")
sonuc = full_name(lastname="Sevinc",firstname="Bilal")
sonuc = full_name(firstname="Bilal",lastname="Sevinc")

print(sonuc)

# Output:

"""

Your name is Bilal Sevinc

"""