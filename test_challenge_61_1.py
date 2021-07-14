import hashlib
from itertools import zip_longest
from pprint import pprint
import sys
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from test_cases_61_1 import test_inp, test_out


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


@mock.patch('builtins.input', side_effect=[str(len(test_inp))] + test_inp)
def test_challenge_61_1(input: Callable) -> None:
    with Capturing() as output:
        start = perf_counter()

        import twt_62_1  # change name to your file with solution name without extension

        end = perf_counter()
    passed = 0
    out = [str(r) for r in output]
    for i, item in enumerate(out):
        if test_out[i] != item:
            print(f"Test Case No: {i}:")
            print(f"Input Number: {test_inp[i]} ->  \tGot: {item}    Expected: {test_out[i]} \n")
        else:
            passed += 1
    print(f"Your solution passed {passed}/{len(out)} cases")
    print(f"Finished in: {end - start} seconds")


if __name__ == "__main__":
    test_challenge_61_1()

