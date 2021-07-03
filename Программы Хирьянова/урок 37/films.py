films = []
votes = []
N = int(input())
for i in range(N):
    name = input()
    if name not in films: # новый
        films.append(name)
        votes.append(1)  # 1-й голос
    else: # фильм уже встречался
        film_id = films.index(name)
        votes[film_id] += 1
for bypass in range(len(films) - 1):
    for i in range(0, len(films) - 1):
        if votes[i] < votes[i+1]:
            votes[i], votes[i+1] = votes[i+1], votes[i]
            films[i], films[i+1] = films[i+1], films[i]
for i in range(len(films)):
    print(films[i], votes[i])
