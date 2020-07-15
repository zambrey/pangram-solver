# pangram-solver
Python code to solve Pangram word game.
<br/><br/>
### One's gotta start somewhere.

I will start generating the words of the given length by permutating the given letters without repetition 🐣.

Let's take the next step. Allow repetition 🐤.

Why don't I validate the strings against a dictionary? [Free public APIS](https://github.com/public-apis/public-apis#dictionaries)? [Owlbot](https://owlbot.info/) looks good. No batch API 😞. This is taking crazy long to finish.

Can I clean up the strings that can never be valid words with some basic rules of thumb of English spelling 🤞? Oh, that's a big drop in the number of strings that I need to validate. But it's still not enough. 

I must have my own dictionary. May I borrow [your dictionary](https://github.com/dwyl/english-words) please 🙏? This should be a `set()` to make lookups faster. 

The string lengths get longer and `set()` approach falls short. The permutations code is a CPU sapper 😠.

💡 [Trie!](https://github.com/google/pygtrie) Make the dictionary a Trie. Also, start trimming the branches 🪓 where no subtrie exists for the prefix.

It takes a little bit longer to initialize, but that's ok. More the strings to validate, better this will perform than earlier approaches.

This is amazingly fast 🥇.
<br/><br/>
### The proof of the pudding is in the eating! 🍰

_Letters:_ ["d", "m", "l", "c", "i", "e", "a"]

_Required:_ ["a"]

_Running tests for words length 8 and 1 required letter._
1. run_onlygeneration_norepeat_test : 33.2841 ms (Count: 0)
2. run_onlygeneration_repeat_test : 26562.5082 ms (Count: 4085185)
3. run_onlygeneration_useheuristics_test : 36085.7912 ms (Count: 1038400)
4. run_uselocaldictasset_test : 29273.6755 ms (Count: 50)
5. run_uselocaldictastrie_test : 45191.4711 ms (Count: 50)
6. run_uselocaldictastrie_trimbranches_test : 5842.4606 ms (Count: 50)
7. run_onlygeneration_useowlbot_test: ~too long
