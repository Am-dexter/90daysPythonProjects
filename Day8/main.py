#This program writes text into file and reads the text to the screen

file_one = open('sample.txt', 'w')
file_one.write('Python programming is amazing!!\n')
file_one.write('New Challenges everyday')
file_one.close()

file_one = open('sample.txt', 'r')
text = file_one.read()
print(text)

file_one.close()