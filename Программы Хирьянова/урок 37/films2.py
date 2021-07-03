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
sorted_filmvotes = sorted(zip(films, votes),
                          key=lambda pair: pair[1],
                          reverse=True)
for film, vote in sorted_filmvotes:
    print(film, vote)
