new = open("new.txt", "a")
new.write("""c ddbdbd sgb
afbbafbbdfb dd
ddb zd d d d  dfvdvs""")
new.close()

txt = open("new.txt", "r")
print(txt.read())