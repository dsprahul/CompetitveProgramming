from functools import reduce

N = int(input())

cobol, vault, donut = [], [], []
for i in range(N):
    c, v, d = list(map(int, input().split()))
    cobol.append(c)
    vault.append(v)
    donut.append(d)

k = [vtime + dtime for vtime, dtime in zip(*[vault, donut])]

players_data = list(zip(*[list(range(N)), cobol, k]))
players_data = sorted(players_data, key=lambda x: x[2], reverse=True)

cum_cobol_offsets = []
cobol_offset = 0
for player in players_data:
    cum_cobol_offsets.append(cobol_offset)
    cobol_offset += player[1]

# Under the assumption that no cum[i] + k[i] > event_duration
# print((cum_cobol_offsets[-1], players_data[-1][1], players_data[-1][2]))
event_duration = (cum_cobol_offsets[-1]
                  + players_data[-1][1]
                  + players_data[-1][2])

for i, player in enumerate(players_data):
    player_id = player[0]
    if cum_cobol_offsets[i] + cobol[player_id] + k[player_id] > event_duration:
        event_duration = cum_cobol_offsets[i] + cobol[player_id] + k[player_id]

print(event_duration)
