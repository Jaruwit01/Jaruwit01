on_subjects = int(input())
subsect_room = []
for i in range(on_subjects):
    subsect_room.append(input().split())
    subsect_room[i][1] = int(subsect_room[i][1])
room_left = {subsect_room[i][0]:subsect_room[i][1] for i in range(len(subsect_room))}


studen_regs = []
no_studen = int(input()) 
for i in range(no_studen):
    studen_regs.append(input().split())
    studen_regs[i][1] = float(studen_regs[i][1])
studen_regs = sorted(studen_regs)

match = []
for i in studen_regs:
    for j in subsect_room:
        if room_left[j[0]] > 0:
            amatch = dict()
            amatch['id'] = i[0]
            amatch['Subsect'] = j[0]
            match.append(amatch)
            room_left[j[0]] -= 1
            
sorted_match = sorted(match, key=lambda x: x['id'])
for i in sorted_match:
    print(f"{i['id']} {i['Subsect']}")
