import goslate

text = "Hello Universe!"
gs = goslate.Goslate()
print(gs.translate('hello world', 'hi')) # Hindi
print(gs.translate('hello world', 'ac')) # English ???
print(gs.translate('hello world', 'ad')) # ???
print(gs.translate('hello world', 'af')) # African ???
print(gs.translate(text,'fr')) # French
print(gs.translate(text,'de')) # Denmark ???
print(gs.translate('hello world', 'zh')) # Chinese

