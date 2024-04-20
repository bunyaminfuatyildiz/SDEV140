# Write your code here
def myRange(start=None, stop=None, step=None):
  """
  This function mimics the behavior of Python's built-in range function but returns a list of integers.

  Args:
      start (int, optional): The starting point of the range. Defaults to None.
      stop (int, optional): The stopping point of the range. Defaults to None.
      step (int, optional): The step value for incrementing or decrementing. Defaults to None.

  Returns:
      list: A list of integers within the specified range.
  """

  # Handle default values and argument combinations
  if stop is None:
    stop = start
    start = 0
  if step is None:
    step = 1

  # Check for invalid step values that would cause infinite loops
  if step == 0 or ((step > 0 and start > stop) or (step < 0 and start < stop)):
    return []

  # Construct the list of integers based on start, stop, and step
  result = []
  current = start
  while (step > 0 and current < stop) or (step < 0 and current > stop):
    result.append(current)
    current += step
  return result

def main():
  # Test cases with various arguments
  print(myRange(10))
  print(myRange(1, 10))
  print(myRange(1, 10, 2))
  print(myRange(10, 1, -1))

if __name__ == "__main__":
  main()
