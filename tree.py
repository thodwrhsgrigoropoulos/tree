a = 0
trunkheight=4
trunkwidth=2
treeheight=10
while a < treeheight:
 print((" " * (treeheight - a)) + ("*" * (a * 2 + 1)))
 a = a + 1
b=0
while b< trunkheight:
	print((" " * (treeheight)) + ("*" * trunkwidth ))
	b= b + 1