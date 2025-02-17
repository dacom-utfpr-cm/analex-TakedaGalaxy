# Expande um intervalo de caracteres e remove os especificados na lista exclude.
def expand_range(state, char_range, exclude = []):
  transitions = {}
  
  if '-' in char_range and len(char_range) == 3:
    start, end = char_range.split('-')
    for c in range(ord(start), ord(end) + 1):
      char = chr(c)
      if char not in exclude:
        transitions[char] = state
    return transitions
    
  for char in char_range:
    if char not in exclude:
      transitions[char] = state
      
  return transitions
  