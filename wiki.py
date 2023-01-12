import os
try:
	import wikipedia
except:
	print('Скачивание модуля wikipedia...')
	os.system('pip install wikipedia')
	exit()
def main():
	try:
		print('Введите exit, чтобы выйти')
		search = input('Введите страницу в Википедии на английском: ')
		if search != 'exit':
			wiki_page = wikipedia.page(search)
			print(wiki_page.original_title)
			print(wiki_page.summary)
	except:
		print('Такой страницы не существует, либо было найдено несколько страниц. Попробуйте расширить запрос')
	if search == 'exit':
		exit()
	main()
main()