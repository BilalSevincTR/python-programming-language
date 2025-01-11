# with open("brands.txt", "a") as file:
#     file.write("6-BMW")

with open("brands.txt", "r+", encoding="utf-8") as file:
    brands = file.readlines()
    brands.insert(2, "3-Renault\n")
    file.seek(0)
    # for brand in brands:
    #     file.write(brand)
    file.writelines(brands)

with open("brands.txt", "r", encoding="utf-8") as file:
    print(file.read())
