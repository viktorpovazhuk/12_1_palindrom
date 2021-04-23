"""
Palindrome class realization.
"""
# https://github.com/viktorpovazhuk/12_1_palindrom

from arraystack import ArrayStack  # or from linkedstack import LinkedStack


class Palindrome:
    """Find palindromes in file"""

    def read_file(self, path):
        """read file with words"""
        with open(path) as ffile:
            lines = ffile.readlines()
        lines = [line.split()[0].strip("\n") for line in lines
                 if line.split()[0].strip("\n") != ""]
        return lines

    def find_palindromes(self, dictionary, save_path):
        """Find palindromes in list"""
        words = self.read_file(dictionary)
        stack = ArrayStack(words)
        palindromes = []
        while True:
            try:
                word = stack.pop()
                if word == word[::-1]:
                    palindromes.append(word)
            except KeyError:
                break
        self.write_to_file(save_path, palindromes)

    def write_to_file(self, path, words):
        """Save palindromes list"""
        lines = [word + "\n" for word in words]
        with open(path, 'w') as ffile:
            ffile.writelines(lines)

# if __name__ == "__main__":
#     palindrome = Palindrome()
#     palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
#     palindrome.find_palindromes("words.txt", "palindrome_en.txt")
