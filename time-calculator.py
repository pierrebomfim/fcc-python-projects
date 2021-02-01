def add_time(x, y, day = ''):

    start = x.split()
    time = start[0]
    find_x = time.find(':')
    start_h = time[0:find_x]
    start_m = time[find_x + 1:]
    period = start[1]

    find_y = y.find(':')
    duration_h = y[0:find_y]
    duration_m = y[find_y + 1:]
    text = ''

    result_h = int(start_h) + int(duration_h)
    if int(start_m) + int(duration_m) <= 59:
        result_m = int(start_m) + int(duration_m)
    else:
        result_h = result_h + ((int(start_m) + int(duration_m))) / 60
        result_m = (int(start_m) + int(duration_m)) % 60
       
    if period == 'AM' and result_h > 11:
        n = 1
        if result_h < 24:
            period = 'PM'
            if result_h > 12:
                result_h = result_h % 12 
        elif result_h < 48:
            if result_h > 35:
                period = 'PM'
                if result_h > 36:
                    result_h = (result_h - 24) % 12 
            else:
                result_h = result_h - 24
            print('Next day')
        else:
            n = int(result_h / 24)
            result_h = int(result_h % 24) 
            print(result_h)
            if result_h >= 12:
                period = 'PM'
                if result_h > 12:
                    result_h = result_h % 12
            print(f'{n} days later')

    #if period == 'AM' and result_h < 12
    
   
    if period == 'PM':
        text = '(Next day)'
        n = 1
        if result_h < 24:
            result_h = result_h = result_h % 12 
            text = ''
        
        if result_h < 36:
            if result_h >= 24:
                period = 'AM'
                result_h = result_h % 12
                

        if result_h < 48:

            if result_h == 36:    
                result_h = int(result_h / 3)
                
            else:
                result_h = result_h % 12
                
        
    
        if result_h >= 48:
            n = int(result_h / 24)
            text = f'({n} days later)'
            a = result_h / 12
            b = a % 2
            if b == 0:
                period = 'AM'
            result_h = result_h % 12
            if result_h == 0 and b != 0:
                result_h = 12
    
    if day == '':
        print(str(round(result_h)) + ':' + str(result_m).zfill(2) + ' ' + period + ', ' + ' ' + text)
    else:
        days = ['Sunday', 'Monday', 'tuesday', 'Wednesday', 'thursday', 'Friday', 'Saturday']
        d = days.index(day)
        day_new = days[(d + n) % 7]
        print(str(round(result_h)) + ':' + str(result_m).zfill(2) + ' ' + period + ', ' + day_new + ' ' + text)           

add_time("08:16 PM", "466:02", 'tuesday')


#   ** Resolver os dígitos em minutos **

# add_time("8:16 PM", "466:02", "tuesday")
# 12:03 AM, Thursday (2 days later)