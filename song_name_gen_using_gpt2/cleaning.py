file = open("lyrics\eminem.txt",encoding='UTF-8')
file = file.read()
lines = file.split('\n')
lyrics = ""

for i,line in enumerate(lines):
    lyrics+= line.replace('\"', '').replace('*', '').replace('#', '').replace('%', '').replace('&', '').replace('"', '')
    lyrics+='<|endoftext|>'

print(lyrics)