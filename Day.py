SECONDS_IN_A_DAY = 60 * 60 * 24
# ...
def display_uptime(uptime_in_seconds):
percentage_run_time = (
uptime_in_seconds/SECONDS_IN_A_DAY) * 100
# "Clearly SECONDS_IN_A_DAY is a constant defined
# elsewhere in this module."
return 'The process was up {percent} percent of the day'.format(
percent=int(percentage_run_time))
# ...
uptime_in_seconds = 60 * 60 * 24
display_uptime(uptime_in_seconds)