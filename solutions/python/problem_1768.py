from _pytest.fixtures import fixture

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        while 1:
            result += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
            if word1 == "" and not word2 == "":
                result += word2
                break
            elif word2 == "" and not word1 == "":
                result += word1
                break
            elif word1 == "" and word2 == "":
                break
        return result



@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    word1 = "abc"
    word2 = "pqr"
    assert sol.mergeAlternately(word1, word2) == "apbqcr"

def test_2(sol: Solution):
    word1 = "abcd"
    word2 = "pq"
    assert sol.mergeAlternately(word1, word2) == "apbqcd"




