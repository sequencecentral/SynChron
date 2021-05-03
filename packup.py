with open("requirements.txt","r") as r:
    lines = [l.rstrip() for l in list(r)]
with open("requirementslist.txt","w") as w:
    w.write(str(lines))