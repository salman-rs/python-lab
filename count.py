text = input("Enter text: ")
words = text.split()
word_count = {}
for w in words:
   if w in word_count:
      word_count[w] += 1
   else:
    word_count[w] = 1
print("Word occurrences:", word_count)
