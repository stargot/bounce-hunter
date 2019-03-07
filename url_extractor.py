import re
import colorama
from helper import random_hash

ident = random_hash()
output = open(f'extractor_{ident}.txt', 'w+')

with open('check.txt') as input:
    for line in input:
        urls = re.findall(
            r'(?:https?:\/\/)?(?:www.?)?example.com\/admincp\/ezbounce.php\?u=\d*', line)
        for url in urls:
            output.write(url + '\n')

# Init colorama module
colorama.init()
print(colorama.Fore.GREEN + 'Извлечение ссылок завершено')
print(colorama.Fore.LIGHTYELLOW_EX + 'Работа программы завершена')
