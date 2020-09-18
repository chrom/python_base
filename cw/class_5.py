def foo(x = []):
    x.append(1)
    print(x)



foo()
foo()
foo()
foo()

exit(1)
# FILES
file = open(r'/Users/ratio/projects/python/first/cw/dictionary.txt')
out = open(r'/Users/ratio/projects/python/first/cw/dictionary_en.txt', 'w')

dictionary = {}
for row in file:
    data = row.split(' - ')
    russ = data[0]
    list_en_words: str = data[1].split(',')
    for ru_w in list_en_words:
        dictionary[ru_w.strip()] = russ.strip()

for row_key in sorted(dictionary.keys()):
    out.write('{} - {} \n'.format(row_key, dictionary[row_key]))

print(dictionary)
out.close()
out.flush()
file.close()

# #read byte
# while True:
#     data = file.read(4)
#     print(data)
#     if not data:
#         break

out.close()
file.close()

exit(1)
string = 'Привет)э'#"Hello World"
# string = "Hello World"

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
import sys
print(sys.getsizeof(string))
print(len(string.encode("utf8")))
import io
print (io.DEFAULT_BUFFER_SIZE)


