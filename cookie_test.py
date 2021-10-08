from cookie_function import find_most_active_cookies

# test for ./most_active_cookie cookie_log.csv -d 2018-12-09
cookies = find_most_active_cookies("cookie_log.csv", "2018-12-09")
assert len(cookies) == 1
assert cookies[0] == "AtY0laUfhglK3lC7"

# test for ./most_active_cookie cookie_log.csv -d 2018-12-08
cookies = find_most_active_cookies("cookie_log.csv", "2018-12-08")
assert len(cookies) == 3
assert cookies[0] == "SAZuXPGUrfbcn5UA"
assert cookies[1] == "4sMM2LxV07bPJzwf"
assert cookies[2] == "fbcn5UAVanZf6UtG"


# test for ./most_active_cookie cookie_log.csv -d 2018-12-08
# no such cookies
assert len(find_most_active_cookies("cookie_log.csv", "2017-01-01")) == 0