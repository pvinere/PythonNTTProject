import re, unittest

log_file = 'sampleFile.txt'
logs = 'aceeasiAplicatie.txt'



def count_logs(log_file):
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0}
    info_counter = 0

    with open(log_file, 'r') as file:
        for line in file:
            if 'INFO' in line:
                info_counter += 1
                if info_counter % 2 == 0:
                    counts['INFO'] += 1
            elif 'DEBUG' in line:
                counts['DEBUG'] += 1
            elif 'ERROR' in line:
                counts['ERROR'] += 1

    return counts


def avg(apps):
    average = {}
    for apps, data in apps.items():

        #division by 0!!
        if(sum(data)==0 or len(data) == 0):
            continue
        else:
            average[apps] = sum(data) / len(data)

    return average


def calculate_average_run_time(log_file):
    run_times = {'FrontendApp': [], 'BackendApp': [], 'API': [], 'SYSTEM': []}

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(
                r'\d+:\d+:\d+ - \[(INFO|ERROR|DEBUG)\] - (\w+) has (started running|ran successfully|failed) in (\d+)ms',
                line)
            if match:
                status, app_type, action, run_time = match.groups()
                #print(f"Match found: status={status}, app_type={app_type}, action={action}, run_time={run_time}")
                if app_type == 'SYSTEM':
                    continue
                if action == 'ran successfully':
                    if app_type == 'BackendApp':
                        run_times['BackendApp'].append(int(run_time))
                    elif app_type == 'FrontendApp':
                        run_times['FrontendApp'].append(int(run_time))
                    elif app_type == 'API':
                        run_times['API'].append(int(run_time))

    return run_times


def most_failed_runs(log_file):
    apps_counter = {'FrontendApp' : 0, 'BackendApp' : 0,'API' : 0, 'SYSTEM' : 0}

    with open(log_file, 'r') as file:
        for line in file:
            strings = line.split('-')
            if 'ERROR' in strings[1]:
                aux = strings[2].split()
                apps_counter[aux[0]] +=1
    app = max(apps_counter, key=apps_counter.get)
    print(f'App with the most failed runs is {app} with {apps_counter[app]}')
    return app, apps_counter[app]


def most_succesful_runs(log_file):
    apps_counter = {'FrontendApp' : 0, 'BackendApp' : 0,'API' : 0, 'SYSTEM' : 0}
    info_counter = 0
    maxi = 0

    with open(log_file, 'r') as file:
        for line in file:
            strings = line.split('-')
            if 'INFO' in strings[1]:
                info_counter += 1
                if info_counter % 2 == 0:
                    aux = strings[2].split()
                    apps_counter[aux[0]] +=1
        app = max(apps_counter, key=apps_counter.get)
        print(f'App with the most succesful runs is {app} with {apps_counter[app]}')
        return app, apps_counter[app]


def errors_app_daily(log_file):

    apps_counter = {'FrontendApp' : 0, 'BackendApp' : 0,'API' : 0, 'SYSTEM' : 0}
    current_time = [0, 0, 0]
    day = 1

    with open(log_file, 'r') as file:
        for line in file:
            strings = line.split('-')
            if 'ERROR' in strings[1]:
                aux = strings[2].split()
                apps_counter[aux[0]] +=1

            time_list = strings[0].split(':')
            ceck = False
            if int(time_list[0]) > int(current_time[0]):
                ceck = True
            elif int(time_list[1]) > int(current_time[1]):
                ceck = True
            elif int(time_list[2]) > int(current_time[2]):
                ceck = True

            if ceck:

                print(f"Day {day} "
                      f"FrontendApp ={apps_counter['FrontendApp']} "
                      f"BackendApp ={apps_counter['BackendApp']} "
                      f"API ={apps_counter['API']} "
                      f"SYSTEM ={apps_counter['SYSTEM']}")
                day +=1
                apps_counter['FrontendApp'] = 0
                apps_counter['BackendApp'] = 0
                apps_counter['API'] = 0
                apps_counter['SYSTEM'] = 0
            current_time = [time_list[0],time_list[1],time_list[2]]
        return day


def count_errors_by_third_of_day(log_file):
    third_of_day = {'00:00:00 - 07:59:59': 0, '08:00:00 - 15:59:59': 0, '16:00:00 - 23:59:59': 0}
    default = {'00:00:00 - 07:59:59': 0, '08:00:00 - 15:59:59': 0, '16:00:00 - 23:59:59': 0}
    with open(log_file, 'r') as file:
        for line in file:
            time = line.split(' - ')[0]
            log_type = line.split(' - ')[1]
            message = line.split(' - ')[2]
            app = message.split(' ')[0]
            if 'ERROR' in log_type and app != 'SYSTEM':
                if '00:00:00' <= time < '08:00:00':
                    third_of_day['00:00:00 - 07:59:59'] += 1
                elif '08:00:00' <= time < '16:00:00':
                    third_of_day['08:00:00 - 15:59:59'] += 1
                else:
                    third_of_day['16:00:00 - 23:59:59'] += 1
    if default != third_of_day:
        return max(third_of_day, key=third_of_day.get)
    else:
        return 'No errors'


def calculate_run_times(log_file):
    run_times = {'FrontendApp': [], 'BackendApp': [], 'API': []}
    with open(log_file, 'r') as file:
        for line in file:
            time = line.split(' - ')[0]
            log_type = line.split(' - ')[1]
            message = line.split(' - ')[2]
            app = message.split(' ')[0]
            if 'has ran successfully' in message and app in run_times:
                ms = message.split(' ')[-1]
                duration = int(ms.split('m')[0])
                run_times[app].append((time, duration))
    longest_shortest_run = {}
    for app, times in run_times.items():
        if times:
            times.sort(key=lambda x: x[1])
            longest_shortest_run[app] = {'shortest': times[0], 'longest': times[-1]}
    return longest_shortest_run


def count_activities_by_hour(log_file):
    app_activities = {'FrontendApp': [0]*24, 'BackendApp': [0]*24, 'API': [0]*24}
    default = {'FrontendApp': [0]*24, 'BackendApp': [0]*24, 'API': [0]*24}
    with open(log_file, 'r') as file:
        for line in file:
            time = line.split(' - ')[0]
            log_type = line.split(' - ')[1]
            message = line.split(' - ')[2]
            app = message.split(' ')[0]
            if app in app_activities:
                hour = int(time.split(':')[0])
                app_activities[app][hour] += 1
    most_active_hour = {}
    if default != app_activities:
        for app in app_activities:
            max_activity = max(app_activities[app])
            if max_activity != 0:
                most_active_hour_index = app_activities[app].index(max_activity)
                most_active_hour[app] = most_active_hour_index
    return most_active_hour


def calculate_failure_rates(log_file):
    failure_rate = {'FrontendApp': [0, 0], 'BackendApp': [0, 0], 'API': [0, 0], 'SYSTEM': [0, 0]}
    with open(log_file, 'r') as file:
        for line in file:
            time = line.split(' - ')[0]
            log_type = line.split(' - ')[1]
            message = line.split(' - ')[2]
            app = message.split(' ')[0]
            failure_rate[app][1] += 1
            if 'ERROR' in log_type:
                failure_rate[app][0] += 1
    failure_rates = {}
    for app in failure_rate:
        num_errors = failure_rate[app][0]
        total_logs = failure_rate[app][1]
        if total_logs != 0:
            failure_rate_percent = (num_errors / total_logs) * 100
            failure_rates[app] = round(failure_rate_percent,2)
    return failure_rates

print("Ex_1:")
print(count_logs(log_file))

print("Ex_2:")
print(calculate_average_run_time(log_file))
average = avg(calculate_average_run_time(log_file))
print(average)

print("Ex_3:")
errors_app_daily(log_file)

print("Ex_4:")
most_failed_runs(log_file)

print("Ex_5:")
print(f"{most_succesful_runs(log_file)}")

print("Ex_6:")
print(f'Most failed third of day: {count_errors_by_third_of_day(logs)}')

print("Ex_7:")
print(f'Longest and shortest run times: {calculate_run_times(logs)}')

print("Ex_8:")
print(f'Most active hour for each app: {count_activities_by_hour(logs)}')

print("Ex_9:")
print(f'Failure rate for each app: {calculate_failure_rates(logs)}')
