gap = [
    ["Otabek", "Anvarov"],
    ["Jasur", "Karimov"],
    ["Bekzod", "Toshmatov"],
    ["Dilshod", "Rahimov"],
    ["Sardor", "Qodirov"],
    ["Aziz", "Yusupov"],
    ["Farrux", "Islomov"],
    ["Shoxrux", "Nazarov"],
    ["Umid", "Ergashev"],
    ["Rustam", "Aliyev"],
    ["Sanjar", "Mirzayev"],
    ["Doston", "Raxmonov"],
    ["Oybek", "Nuriddinov"],
    ["Zafar", "Abdullayev"],
    ["Kamol", "Saidov"],
    ["Murod", "Xolmatov"],
    ["Jamshid", "Bozorov"],
    ["Akmal", "Ganiyev"],
    ["Bobur", "Tursunov"],
    ["Sherzod", "Pulatov"]
]

#soz = gap.split(" ")

for i in range(len(soz)):
    for j in range(len(soz) - 1):
        if gap[j][1] > gap[j + 1][1]:
            gap[j],gap[j+1]=gap[j+1],gap[j]


print(gap)