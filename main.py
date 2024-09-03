with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(str):
  words = str.split()
  return len(words)

chars_count = {}

def count_chars(str):
  for c in str:
    if c.lower() in chars_count:
      chars_count[c.lower()] += 1
    else:
      chars_count[c.lower()] = 1
  return chars_count

dict_list = []
def create_dict_list(dictionary):
  for key, value in dictionary.items():
    if key.isalpha():
      dict_list.append({"name": key, "value": value})

def sort_on(dict):
  return dict["value"]

def main():
  count_chars(file_contents)
  create_dict_list(chars_count)
  dict_list.sort(reverse=True, key=sort_on)
  print('--- Begin report of books/frankenstein.txt ---')
  print(f'{count_words(file_contents)} words  found in the document\n')
  for item in dict_list:
    print(f'the \'{item["name"]}\' character was found {item["value"]} times')

main()