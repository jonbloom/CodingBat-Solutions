def alarm_clock(day, vacation):
  if vacation:
    if day in [0,6]:
      return 'off'
    return '10:00'
  if day in [0,6]:
      return '10:00'
  return '7:00'