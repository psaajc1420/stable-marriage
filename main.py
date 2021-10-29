from random import sample

def generate_preferences(names, n=1000):
  selected_names = sample(names, n)

  return selected_names


def main():

  with open('names.txt') as f:
    names = [name.rstrip() for name in list(f.readlines())]

  generate_preferences(names)

if __name__ == '__main__':

  main()
