n = int(input())
sentences = []

for _ in range(n):
    sentences.append(input())

for name in sorted(sorted(list(set(sentences))), key=len):
    print(name)