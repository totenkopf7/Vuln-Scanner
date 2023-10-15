#!/usr/bin/evn python

import scanner


# target_url = input("Enter target website: ")

target_url = "http://testphp.vulnweb.com"
links_to_ignore = [""]
data_dict = {"uname":"test", "pass":"test", "Login":"submit"}


# if target_url == "1":
#     target_url = "http://testphp.vulnweb.com/"
main = scanner.Scanner(target_url, links_to_ignore)
main.session.post("http://testphp.vulnweb.com/login.php", data=data_dict)
main.crawl()








