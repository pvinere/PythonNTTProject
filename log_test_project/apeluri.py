from functions import *


log_file = 'output.txt'

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
print(f'Most failed third of day: {count_errors_by_third_of_day(log_file)}')

print("Ex_7:")
print(f'Longest and shortest run times: {calculate_run_times(log_file)}')

print("Ex_8:")
print(f'Most active hour for each app: {count_activities_by_hour(log_file)}')

print("Ex_9:")
print(f'Failure rate for each app: {calculate_failure_rates(log_file)}')
