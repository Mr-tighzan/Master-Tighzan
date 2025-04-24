import random
from art import text2art

# چاپ نام "Tighzan" با ASCII Art
ascii_art = text2art("Tighzan")
print(ascii_art)

print("              ")
print("                   ")
# دریافت 10 لینک از کاربر
links = []
for i in range(10):
    link = input(f"Please enter link {i + 1}:")
    links.append(link)

# پسوندهای تعیین شده
random_suffix1 = "<[ActiveInternet-connections(only.servers)Proto;Recv-Q;Send-Q;Local-Address;ForeignAddress/State{=*40}]28:ip6_vti0@NONE: <NOARP>mtu.1500.qdisc.noop.state.DOWN.default.qlen.1000<https://www.phishing.com>"
random_suffix2 = "<{89872e50da06bfd81e1dc8ac444f3582f2400f5a15e66f745525dba4d3b10b20}>"
final_suffix = "<https://api.shadowserver.org/malware/info?sample=dfe1832e02888422f48d6896dc8e8f73<(@Supportbot)>"
print("            ")
# انتخاب تصادفی 2 لینک و افزودن پسوند
link1 = random.choice(links) + random_suffix1
link2 = random.choice(links) + random_suffix2

# ایجاد لیست نهایی با سایر لینک‌ها
final_links = [f"[{link}]>" for link in links if link != link1 and link != link2] + [link1, link2]

# تولید نتیجه نهایی
result = ''.join(final_links) + final_suffix
print("           ")
print("Final result.")
print("              ")
print(result)