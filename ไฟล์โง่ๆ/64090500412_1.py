message = "Dear Amanda I haven't knew how joyous life could be until I saw your face.My heart leaps like a hummingbird in flight every time I see your face.This is something I have never felt before, and it is you that inspires it.".split()
message = list(message)
key_message = {'.':'.',
'Amanda' : 'Doctor',
"haven't" : 'am',
'knew' : 'now',
'how' : 'in',
'joyous' : 'great',
'could' : 'threatening',
'be' : 'danger,',
'until' : 'please',
'saw' : 'need',
'face': 'help',
'leaps' : 'beats',
'hummingbird' : 'machine ',
'in':'very',
'flight' : 'alarmingly',
'time' : 'hour,',
'see' : 'need',
'you' : 'the drug',
'inspires' : 'causes',}
s = ''
for i in key_message:
    for x in range(len(message)):
        if i== message[x]:
            message[x] = key_message[i]
        else:
            pass
print(*message[:2],'\n',*message[2:])
