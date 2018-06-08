import csv, re, typing, math

with open(r"C:\Users\Germanistika biblio\Desktop\UPITNIK ZA GERMANISTE\UPITNIK ZA GERMANISTE – FORMA A.csv",
          "r", encoding="utf8") as cf:
    content = csv.DictReader(cf)
    for row in content:
        r: str = row["POZNAVANJE DRUGIH JEZIKA (upisati jezik i procenjeni nivo znanja)"]
        # print(r)

