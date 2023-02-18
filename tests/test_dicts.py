import unittest
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get_val(self):
        self.assertIs(dicts.get_val({"vcs": "mercurial"}, "vcs"), 'mercurial')
        self.assertIs(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), 'mercurial')
        self.assertIs(dicts.get_val({}, "vcs", "git"), 'git')
        self.assertIs(dicts.get_val({}, "vcs", "bazaar"), 'bazaar')
        self.assertIs(dicts.get_val([2, 3], "vcs", "bazaar"), 'bazaar')
        self.assertIs(dicts.get_val([2, 3], "vcs"), 'git')


if __name__ == "__main__":
    unittest.main()
