import pygtrie as trie
import requests
from requests.exceptions import HTTPError
from typing import List, Set, Tuple


class pangramgame:
    def __init__(self, letters: List[str], required: List[str], lenRange: Tuple[int, int]):
        self._letters = set([s.lower() for s in letters])
        self._vowels = self._letters.intersection(
            set(['a', 'e', 'i', 'o', 'u']))
        self._consonants = self._letters - self._vowels
        self._required = set([s.lower() for s in required])
        self._lenRange = lenRange
        self._dictionary = None

        # Setting default debug attrs
        self.debug_attrs()

    def debug_attrs(self, onlyGeneration: bool = False, allowRepeat: bool = True, useHeuristics: bool = False, useLocalDict: bool = True, useTrie: bool = True, trimInvalidPrefixes: bool = True):
        self._onlyGeneration = onlyGeneration
        self._allowRepeat = allowRepeat
        self._useHeuristics = useHeuristics
        self._useLocalDict = useLocalDict
        self._useTrie = useTrie
        self._trimInvalidPrefixes = trimInvalidPrefixes

    def _loadDictionary(self):
        with open('words_alpha.txt') as word_file:
            valid_words = set(word_file.read().split())

        if self._useTrie:
            self._dictionary = trie.CharTrie.fromkeys(valid_words, True)
        else:
            self._dictionary = valid_words

    def _isDictionaryWord(self, word: str) -> bool:
        if self._useLocalDict:
            if not self._dictionary:
                self._loadDictionary()
            return word in self._dictionary
        else:
            return self._isOwlBotWord(word)

    def _isValidPrefix(self, prefix: str) -> bool:
        if not self._onlyGeneration and self._trimInvalidPrefixes:
            if not self._dictionary:
                self._loadDictionary()
            return self._dictionary.has_subtrie(prefix)
        else:
            return True

    def _isOwlBotWord(self, word: str) -> bool:
        url = "https://owlbot.info/api/v4/dictionary/" + word
        try:
            response = requests.get(url,
                                    headers={"Authorization": "Token yourapikey"},)
            response.raise_for_status()
        except Exception:
            return False
        else:
            return True

    def _isPossibleWord(self, word: str) -> bool:
        # Must have required letters
        if len(self._required.intersection(word)) != len(self._required):
            return False

        if self._useHeuristics:
            # A valid word should have at least one vowel
            if not self._vowels.intersection(word):
                return False

            # No more than 2 consecutive consonants
            i = 0
            while i < (len(word)-2):
                if word[i] in self._consonants:
                    if word[i+1] in self._consonants:
                        if word[i+2] in self._consonants:
                            return False
                        else:
                            i += 3
                    else:
                        i += 2
                else:
                    i += 1

            # No more than 2 consecutive vowels
            i = 0
            while i < (len(word)-2):
                if word[i] in self._vowels:
                    if word[i+1] in self._vowels:
                        if word[i+2] in self._vowels:
                            return False
                        else:
                            i += 3
                    else:
                        i += 2
                else:
                    i += 1

            # v, j, k, w and x should never repeat
            nonrepeat = set(["v", "j", "k", "w", "x"])
            if nonrepeat.intersection(self._letters):
                if nonrepeat.intersection(word):
                    for i in range(0, len(word)-1):
                        if word[i] in nonrepeat and word[i] == word[i+1]:
                            return False

            # Word should not repeat a letter in the beginning except when e, o or l.
            if word[0] not in "eol" and word[0] == word[1]:
                return False

            # q is always followed by u
            if "q" in self._letters and "q" in word:
                if "u" in self._letters and "u" in word:
                    if "qu" not in word:
                        return False
                else:
                    return False

        if not self._onlyGeneration:
            # Verify in dict
            if not self._isDictionaryWord(word):
                return False

        return True

    def _solveHelper(self, used: Set[str], curr: str, result: List[str]):
        if not self._isValidPrefix(curr) or len(curr) > self._lenRange[1]:
            return

        if (self._lenRange[0] <= len(curr) <= self._lenRange[1]):
            if (self._isPossibleWord(curr)):
                # print(curr)
                result.append(curr)

        for l in self._letters:
            if self._allowRepeat:
                self._solveHelper(used, curr+l, result)
            else:
                if l not in used:
                    used.add(l)
                    self._solveHelper(used, curr+l, result)
                    used.remove(l)

    def solve(self) -> List[str]:
        result = []
        self._solveHelper(set(), "", result)
        return result
