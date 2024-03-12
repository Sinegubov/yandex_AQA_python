times_string = '1h 45m,360s,25m,30m 120s,2h 60s'
times_list = times_string.replace(' ', ',').split(',')
minutes = 0

for time in times_list:
    if time[-1] == 'h':
        minutes += int(time[:-1])*60
    elif time[-1] == 's':
        minutes += int(time[:-1])//60
    else:
        minutes += int(time[:-1])

print(minutes)
