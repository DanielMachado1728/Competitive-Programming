while True:
  try:
    grace = ''
    s = input().lower()
    s = s.split('-')
    if s[0][0] == 'c' or s[0][-1] == 'c':
      grace += 'c'
    if s[1][0] == 'o' or s[1][-1] == 'o':
      grace += 'o'
    if s[2][0] == 'b' or s[2][-1] == 'b':
      grace += 'b'
    if s[3][0] == 'o' or s[3][-1] == 'o':
      grace += 'o'
    if s[4][0] == 'l' or s[4][-1] == 'l':
      grace += 'l'
    if grace == 'cobol':
      print('GRACE HOPPER')
    else:
      print('BUG')      
  except:
    break
    
