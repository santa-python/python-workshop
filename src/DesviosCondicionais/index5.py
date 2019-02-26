string = input('digite o que quiser:')
occurrence = input('digite sua ocorrência:')
while len(occurrence) > 1:
	occurrence = input('digite apenas uma letra:')
if occurrence in string:
	print('achei')
else:
	print(':(')