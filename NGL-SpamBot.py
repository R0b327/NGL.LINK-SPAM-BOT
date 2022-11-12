#!/usr/bin/env python3

import time
try:
	import requests
	import colorama
except Exception as err:
	exit(err)


colorama.init(autoreset=True)
LB = colorama.Fore.LIGHTBLUE_EX
LG = colorama.Fore.LIGHTGREEN_EX
LR = colorama.Fore.LIGHTRED_EX
LY = colorama.Fore.LIGHTYELLOW_EX
RESET = colorama.Fore.RESET


class NGL_Spammer:
	def __init__(self, username, message, spamtime):
		self._username = username
		self._message = message
		self._spamtime = spamtime
		self._url = f"https://ngl.link/{self._username}"
		self._totalsent = []
		self._total = 0


	def create_msg(self):
		return f"""
		{self._message}


		-ngl.link SpamBot By R0b327
		"""

	def start(self, spam):
		UA = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.7 (build 538; iPhone 11 Pro Max; iOS 14.7.1)'
		}
		payload = {
		"question": self.create_msg()
		}
		print(f"\n{LB}[{LG}+{LB}] {LY}STARTED!")
		print(f"{LB}[{LG}+{LB}] {LY}SpamTime{LR}:{LG} {spam}\n")
		S = requests.Session()
		while time.time() < self._spamtime:
			try:
				S.post(self._url, headers=UA, data=payload)
				self._total += 1
				self._totalsent.append(self._total)
				print(f"{LB}[{LG}{self._total}{LB}]{LY} Message Sent to{LR}:{LG} {self._username}", end="\r")
			except requests.exceptions.ConnectionError:
				self._total += 1
				print(f"{LB}[{LR}{self._total}{LB}]{LR} Internet Connection Error", end="\r")

		exit(f"\n{LB}[{LG}{len(self._totalsent)}{LB}]{LY} Message has been sent successfully!!")


def main():
		print("\033c")
		print(f"{LG}="*50)
		print(f"{LR}[{LY} ngl.link SpamBot Coded By R0b327{LR}		 ]")
		print(f"{LR}<"+f"{LG}="*48+f"{LR}>")
		print(f"{LR}[ {LY}Github{LR}:{RESET} https://github.com/R0b327		 {LR}]\n{LR}[ {LY}Facebook{LR}:{RESET} https://facebook.com/R0b327{LR}		 ]")
		print(f"{LG}="*50)

		try:
			user = str(input(f"{LB}[{LG}+{LB}] {LY}Enter Target Username:{RESET} "))
			msg = str(input(f"{LB}[{LG}+{LB}] {LY}Enter Your Message:{RESET} "))
			spam = int(input(f"{LB}[{LG}+{LB}] {LY}Time:{RESET} "))
		except Exception:
			exit(f"{LB}[{LR}!{LB}]{LR} Invalid SpamTime, Try again.")

		ngl = NGL_Spammer(username=user, message=msg, spamtime=time.time() + spam)
		ngl.start(spam)


if __name__ == "__main__":
	main()
