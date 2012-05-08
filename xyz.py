//
keypad = {
    '0': '0',
    '1': '1',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def word_numbers(input):
  input = str(input)
  combinations = ['']
  for char in input:
    letters = keypad.get(char, '')
    combinations = [prefix+letter  for prefix in combinations for letter in letters ]
  print combinations

def biz():
  file = open("sample.txt")
  combo=[]
  for line in  file:
    line=line.strip('\n')
    print line
    word_numbers(line)
  
