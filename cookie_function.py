def find_most_active_cookies(file_name, date_string):
  max_cookies = []
  cookies_on_date_freq = {}
  max_freq = 0
  # Purpose of cookie_order is to print by most recent occurrence
  cookie_order = []

  with open(file_name, 'r') as f:
    i = 0
    for line in f:
      if i > 0:
        cookie, timestamp = line.split(",")
        if timestamp[0:len(date_string)] == date_string:
          if cookie in cookies_on_date_freq:
            cookies_on_date_freq[cookie] += 1
          else:
            cookies_on_date_freq[cookie] = 1
            cookie_order.append(cookie)
          max_freq = max(max_freq, cookies_on_date_freq[cookie])
      i += 1

  for cookie in cookie_order:
    if cookies_on_date_freq[cookie] == max_freq:
      max_cookies.append(cookie)

  return max_cookies