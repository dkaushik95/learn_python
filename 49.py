import re
sentence = 'Dogs and Cats are Domestic Animals. But, I love Rabbits'
matched = re.match(r'Cats', sentence)
print matched.group()
