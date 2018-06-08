import csv, re, itertools

langs = []
languages = dict()
levels = {"a1":0, "a2":0, "b1":0, "b2":0, "c1":0, "c2":0}
level_values = [1,2,3,4,5,6]
level_letters = ["A1", "A2", "B1", "B2", "C1", "C2"]
ch = {"š":"s","đ":"dj","ž":"z","č":"c","ć":"c"}

males = 0
male_levels = {"a1":0, "a2":0, "b1":0, "b2":0, "c1":0, "c2":0}
male_languages = dict()
male_langs = []
females = 0
female_levels = {"a1":0, "a2":0, "b1":0, "b2":0, "c1":0, "c2":0}
female_languages = dict()
female_langs = []

le2 = re.compile("(\w+)\s*\W*\s*([a-cA-C]-*\d)*")

with open(r"C:\Users\Germanistika biblio\Desktop\UPITNIK ZA GERMANISTE\UPITNIK ZA GERMANISTE – FORMA A.csv",
          "r", encoding="utf8") as cf:
    content = csv.DictReader(cf)
    for row in content:
        r: str = row["POZNAVANJE DRUGIH JEZIKA (upisati jezik i procenjeni nivo znanja)"]
        # print(r)
        r = r.replace(" jezik", "")
        langs.append(r)
        if row["POL"] == "M":
            male_langs.append(r)
            males += 1
        else:
            female_langs.append(r)
            females += 1

# print(langs)
# print(male_langs)
# print(female_langs)

for male, female, lang in itertools.zip_longest(male_langs, female_langs, langs):

    res = re.findall(le2, lang.strip())
    if male is not None:
        res_male = re.findall(le2, male.strip())
    else:
        res_male = [("","")]
    if female is not None:
        res_female = re.findall(le2, female.strip())
    else:
        res_female = [("","")]
    print("Result:", res, res_female, res_male)

    for m, f, r in itertools.zip_longest(res_male, res_female, res):
        print(m, f, r)
        if r is None:
            pass
        else:
            la = r[0].lower()
            le = r[1].lower().replace("-", "") if len(r) > 1 else "b2"
            if le == "":
                le = "b1"
            elif le == "b3":
                le = "b2"
            for k, v in ch.items():
                la = la.replace(k, v)
            if la in ("visi", "nivo", "i", "c1", "b1"):
                continue
            elif la in ("engkeski", "ebgleski"):
                la = "engleski"
            elif la == "holanski":
                la = "holandski"
            if languages.get(la, 0):
                languages[la]["br"] += 1
            else:
                languages[la] = {"br": 1, "a1": 0, "a2": 0, "b1": 0, "b2": 0, "c1": 0, "c2": 0}
            levels[le] += 1
            languages[la][le] += 1

        if m is None or m[0] == "":
            pass
        else:
            m_la = m[0].lower()
            m_le = m[1].lower().replace("-", "") if len(m) > 1 else "b2"
            if m_le == "":
                m_le = "b1"
            elif m_le == "b3":
                m_le = "b2"
            for k, v in ch.items():
                m_la = m_la.replace(k, v)
            if m_la in ("visi", "nivo", "i", "c1", "b1"):
                continue
            elif m_la in ("engkeski", "ebgleski"):
                m_la = "engleski"
            elif m_la == "holanski":
                m_la = "holandski"
            if male_languages.get(m_la, 0):
                male_languages[m_la]["br"] += 1
            else:
                male_languages[m_la] = {"br": 1, "a1": 0, "a2": 0, "b1": 0, "b2": 0, "c1": 0, "c2": 0}
            male_levels[m_le] += 1
            male_languages[m_la][m_le] += 1

        if f is None or f[0] == "":
            pass
        else:
            f_la = f[0].lower()
            f_le = f[1].lower().replace("-", "") if len(f) > 1 else "b2"
            if f_le == "":
                f_le = "b1"
            elif f_le == "b3":
                f_le = "b2"
            for k, v in ch.items():
                f_la = f_la.replace(k, v)
            if f_la in ("visi", "nivo", "i", "c1", "b1"):
                continue
            elif f_la in ("engkeski", "ebgleski"):
                f_la = "engleski"
            elif f_la == "holanski":
                f_la = "holandski"
            if female_languages.get(f_la, 0):
                female_languages[f_la]["br"] += 1
            else:
                female_languages[f_la] = {"br": 1, "a1": 0, "a2": 0, "b1": 0, "b2": 0, "c1": 0, "c2": 0}
            female_levels[f_le] += 1
            female_languages[f_la][f_le] += 1


# print(languages)
for lang, v in languages.items():
    print("{0} - {1}:\nA1 - {2}\nA2 - {3}\nB1 - {4}\nB2 - {5}"
          "\nC1 - {6}\nC2 - {7}".format(lang, v["br"], v["a1"], v["a2"], v["b1"], v["b2"], v["c1"], v["c2"]))
    mean = (v["a1"] * level_values[0] + v["a2"] * level_values[1] + v["b1"] * level_values[2] + v["b2"] * level_values[3]
           + v["c1"] * level_values[4] + v["c2"] * level_values[5]) / v["br"]
    print(mean)
    print("Prosek: {}\n".format(level_letters[round(mean)-1]))

# for lang, v in languages.items():
#     print()
print("Jezici po popularnosti:")
for lang in sorted(languages.keys(), key=lambda x: (languages[x]['br']), reverse=True):
    print("{0:<15} - {1:<10}".format(lang, languages[lang]["br"]))
print()

m_mean = (male_levels["a1"] * level_values[0] + male_levels["a2"] * level_values[1] + male_levels["b1"] * level_values[2] + male_levels["b2"] * level_values[3]
           + male_levels["c1"] * level_values[4] + male_levels["c2"] * level_values[5]) / sum(male_levels.values())
f_mean = (female_levels["a1"] * level_values[0] + female_levels["a2"] * level_values[1] + female_levels["b1"] * level_values[2] + female_levels["b2"] * level_values[3]
           + female_levels["c1"] * level_values[4] + female_levels["c2"] * level_values[5]) / sum(female_levels.values())

print("Muskarci: {}".format(males))
print("Prosek: {} - {}\nBroj jezika: {}\n"
      .format(m_mean, level_letters[round(m_mean-1)], len(male_languages.keys())))
print("Jezici po popularnosti:")
for lang in sorted(male_languages.keys(), key=lambda x: (male_languages[x]['br']), reverse=True):
    print("{0:<15} - {1:<10} ({2:.2f}%)".format(lang, male_languages[lang]["br"], (male_languages[lang]["br"]*100)/males))

print("\nZene: {}".format(females))
print("Prosek: {:<15} - {}\nBroj jezika: {}\n"
      .format(f_mean, level_letters[round(f_mean-1)], len(female_languages.keys())))
for lang in sorted(female_languages.keys(), key=lambda x: (female_languages[x]['br']), reverse=True):
    print("{0:<15} - {1:<10} ({2:.2f}%)".format(lang, female_languages[lang]["br"], female_languages[lang]["br"]*100/females))

print("\nUkupno nivoa:\nA1 - {}\nA2 - {}\nB1 - {}\nB2 - {}\nC1 - {}\nC2 - {}".format(levels["a1"], levels["a2"],
                                                            levels["b1"], levels["b2"], levels["c1"], levels["c2"]))
