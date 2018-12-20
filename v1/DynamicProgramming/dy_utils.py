def collection_equals(col1, col2):
  if not col1 and not col2:
    return True

  if col1 and not col2 or col2 and not col1:
    return False

  if len(col1) != len(col2):
    return False

  for e in col1:
    if e not in col2:
      return False

  for e in col2:
    if e not in col1:
      return False

  return True