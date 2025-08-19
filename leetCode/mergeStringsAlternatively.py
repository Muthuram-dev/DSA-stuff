word1 = "ab"
word2 = "pqcde"

min_len = min(len(word1), len(word2))
result = ""

for i in range(min_len):
    result += word1[i] + word2[i]

result += word1[min_len:] + word2[min_len:]

print(result)
