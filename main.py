import random as rd
import platform as pf
import subprocess as sp
from gpuinfo import GPUInfo as gp
import sys

sys.tracebacklimit = 0

def linuxCpuInfo(target):
	command = "cat /proc/cpuinfo"
	all_info = sp.check_output(command, shell=True).strip().decode('utf-8')

	for i in all_info.split("\n"):
		if target in i:
			i = i.split(": ")
			return i[1]

def cpu():
	if debugMode:
		print ("[] function cpu")
	system = pf.system()
	if "Linux" in system:
		info = linuxCpuInfo("model name")
		if "Intel" in info:
			if "Pentium" in info:
				print ("Wow, Pentium... that's slow.")
			elif "Core" in info:
				if "i3" in info:
					print ("i3... that's a waste of money.")
				if "i5" in info:
					print ("Go get a i7, i5 is too weak to write program.")
				elif "i7" in info:
					print ("i7 is toy, Zeon is for adults.")
			elif "Zeon" in info:
				print ("I prefer Threadripper, name's cooler and model numbers are easier.")
			elif "Atom" in info:
				print ("Wait, someone actually use a Atom?")
	elif "Windows" in system:
		print ("Windows")

def machine():
	if debugMode:
		print ("[] function machine")
	machine = pf.machine()
	if machine == "x86_64" or machine == "AMD64":
		print ("eww... x86_64? Are you afriad to use arm?")
	elif machine == "x86" or machine == "AMD64":
		print ("Still using x86 cpu? switch to a 64 bit already you old man")
	elif "arm" in machine:
		print ("low power? more like low performance")
	elif machine == "":
		print ("Trying to hide something? Like your machine type?")
	else :
		print ("Unknown Processor? How's the performance?")

def network():
	if debugMode:
		print ("[]function network")
	print ("So... your network name is",pf.node(), ", aren't you?")

def OS():
	if debugMode:
		print ("[] function OS")
	system = pf.system()
	if "Linux" in system or "linux" in system:
		distro = pf.linux_distribution()[0]
		if distro == "Ubuntu":
			print ("Ahh.. Ubuntu...That.. that is good stuff")
		elif distro == "Kubuntu":
			print ("Gnome is much better, isn't it?")
		elif distro == "Debian":
			print ("Debian...eww")
		elif distro == "Arch":
			print ("BTW you use Arch")
		elif distro == "Mint":
			print ("Afraid of windows I see, Mint users...")
		elif distro == "Manjaro":
			print ("It's not arch? what the hell is it?")
		elif distro == "Deepin":
			print ("Deepin, send my data")
		elif distro == "Kali":
			print ("Would mind if I send your data to the NSA? (Y/n)")
			kaliAns = str(input())
			if kaliAns == 'n' or kaliAns == 'N':
				print ("Meh.. I already did")
			else:
				print ("What the hell is wrong with you?")
		elif distro == "Elementary":
			print ("Your linux skill is the same as this distro's name")
		elif "Red Star" in distro:
			print ("wait.. is it North korea?")
		elif distro == "Fedora":
			print ("Do you really need Fedora? (Y/n)")
			fedoraAns = input()
			print ("yeah, you need one")
		elif distro == "MX Linux":
			print ("What is MX?")
		else:
			print ("What is this?")
	elif "BSD" in system:
		print ("BSD... that's something")
	elif "Windows" in system:
		print ("Updating Windows is full of BS")
	else:
		print ("I Have no idea what the hell you're using")

def gpu() :
	if debugMode:
		print ("[] function gpu")
	system = pf.system()
	if "Linux" in system:
		print ("Linux gpu") # Future update
	elif "Windows" in system:
		print ("Windows GPU") # Future Update
	elif "Mac" in system:
		print ("mac GPU") # Future Update


rude = [machine,
		network,
		OS,
		cpu,
		gpu]

debugMode = False

if "-D" in sys.argv:
	debugMode = True
rd.choice(rude)()
