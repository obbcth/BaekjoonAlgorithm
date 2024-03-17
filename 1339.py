n = int(input())

words = {}

for i in range(n):
    word = input()

    for idx in range(len(word)):

        if word[idx] in words:
            words[word[idx]] += 10 ** (len(word) - idx - 1)
        
        else:
            words[word[idx]] = 10 ** (len(word) - idx - 1)

numbers = list(words.values())
numbers.sort(reverse=True)

answer = 0

for i in range(len(numbers)):
    answer += numbers[i] * (9-i)

print(answer)
