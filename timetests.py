import time
from pangramsolver import pangramgame
from typing import Callable, List

wordLen = 7


def printList(l: List[str]):
    for item in l:
        print(item)


def run_timer_tests():
    print(f"Running tests for words length {wordLen} and 1 required letter.")
    run_onlygeneration_norepeat_test()
    run_onlygeneration_repeat_test()
    run_onlygeneration_useheuristics_test()
    run_uselocaldictasset_test()
    run_uselocaldictastrie_test()
    run_uselocaldictastrie_trimbranches_test()
    run_full_test()
    # run_useowlbot_test()


def runtimetest_generic(testname: str, func: Callable[[], type(None)]):
    tic = time.perf_counter_ns()
    result = func()
    toc = time.perf_counter_ns()
    print(
        f"* {testname} : {((toc - tic)/pow(10, 6)):0.4f} ms (Count: {str(len(result))})")
    printList(result)


def run_onlygeneration_norepeat_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=True,
        allowRepeat=False,
        useHeuristics=False,
        useLocalDict=False,
        useTrie=False,
        trimInvalidPrefixes=False)
    runtimetest_generic("run_onlygeneration_norepeat_test",
                        lambda: game.solve())


def run_onlygeneration_repeat_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=True,
        allowRepeat=True,
        useHeuristics=False,
        useLocalDict=False,
        useTrie=False,
        trimInvalidPrefixes=False)
    runtimetest_generic("run_onlygeneration_repeat_test", lambda: game.solve())


def run_onlygeneration_useheuristics_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=True,
        allowRepeat=True,
        useHeuristics=True,
        useLocalDict=False,
        useTrie=False,
        trimInvalidPrefixes=False)
    runtimetest_generic(
        "run_onlygeneration_useheuristics_test", lambda: game.solve())


def run_uselocaldictasset_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=False,
        allowRepeat=True,
        useHeuristics=False,
        useLocalDict=True,
        useTrie=False,
        trimInvalidPrefixes=False)
    runtimetest_generic(
        "run_uselocaldictasset_test", lambda: game.solve())


def run_uselocaldictastrie_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=False,
        allowRepeat=True,
        useHeuristics=False,
        useLocalDict=True,
        useTrie=True,
        trimInvalidPrefixes=False)
    runtimetest_generic(
        "run_uselocaldictastrie_test", lambda: game.solve())


def run_uselocaldictastrie_trimbranches_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=False,
        allowRepeat=True,
        useHeuristics=False,
        useLocalDict=True,
        useTrie=True,
        trimInvalidPrefixes=True)
    runtimetest_generic(
        "run_uselocaldictastrie_trimbranches_test", lambda: game.solve())


def run_full_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (4, 10))
    game.debug_attrs(
        onlyGeneration=False,
        allowRepeat=True,
        useHeuristics=False,
        useLocalDict=True,
        useTrie=True,
        trimInvalidPrefixes=True)
    runtimetest_generic(
        "run_full_test", lambda: game.solve())


def run_useowlbot_test():
    game = pangramgame(["d", "m", "l", "c", "i", "e", "a"],
                       ["a"], (wordLen, wordLen))
    game.debug_attrs(
        onlyGeneration=False,
        allowRepeat=True,
        useHeuristics=True,
        useLocalDict=False,
        useTrie=False,
        trimInvalidPrefixes=False)
    runtimetest_generic("run_useowlbot_test",
                        lambda: game.solve())


run_timer_tests()
