# Read user input
pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours = float(input())

# Parameters
total_flow = first_pipe_flow + second_pipe_flow
filled_volume = hours * total_flow
first_pipe_share = (first_pipe_flow / total_flow) * 100
second_pipe_share = (second_pipe_flow / total_flow) * 100

# Logic
if pool_volume >= filled_volume:
    percent_filled = filled_volume / pool_volume * 100
    print(f'The pool is {percent_filled:.2f}% full. '
          f'Pipe 1: {first_pipe_share:.2f}%. '
          f'Pipe 2: {second_pipe_share:.2f}%.')
else:
    diff = filled_volume - pool_volume
    print(f'For {hours:.2f} hours the pool overflows with {diff:.2f} liters.')
# End of Logic

# Print Output
