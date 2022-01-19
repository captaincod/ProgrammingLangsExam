import pytest

from tests_6 import DictWithFileLog

path_to_file = "for_test.txt"


class TestDictWithFileLog:
    def test_init(self):
        logged_dict1 = DictWithFileLog(path_to_file)
        logged_dict2 = DictWithFileLog("not the path")
        assert logged_dict1 == logged_dict2 == {}
        logged_dict = DictWithFileLog(path_to_file, {'Fallout': 1})
        assert logged_dict == {'Fallout': 1}

        with pytest.raises(TypeError):
            logged_dict1 = DictWithFileLog(path_to_file, {0})
            logged_dict2 = DictWithFileLog(path_to_file, [1, 2])
            logged_dict3 = DictWithFileLog(path_to_file, {'': ''}, {'': ''})

        with pytest.raises(ValueError):
            logged_dict1 = DictWithFileLog(path_to_file, {'error'})
            logged_dict2 = DictWithFileLog(path_to_file, 'error')

        with pytest.raises(FileNotFoundError):
            logged_dict = DictWithFileLog("")

        with pytest.raises(PermissionError):
            only_dir = "D:/PycharmProjects/ProgrammingLangsExam/tests_6"
            logged_dict = DictWithFileLog(only_dir)

        """
        >>> Failed: DID NOT RAISE <class 'OSError'>
        with pytest.raises(OSError):
            logged_dict = DictWithFileLog(4)
        """

    def test_set(self):
        logged_dict = DictWithFileLog(path_to_file, {'Fallout': 1})
        logged_dict[1] = 'Interplay Entertainment'
        logged_dict['Fallout 2'] = 'Black Isle Studios'
        assert logged_dict[1] == 'Interplay Entertainment'
        assert logged_dict['Fallout 2'] == 'Black Isle Studios'
        logged_dict['Fallout'] = 'New Vegas'
        assert logged_dict.log()[-1].__contains__('set')
        with pytest.raises(TypeError):
            logged_dict[{}] = 'dict'
        with pytest.raises(TypeError):
            logged_dict[[]] = 'list'

    def test_get(self):
        logged_dict = DictWithFileLog(path_to_file)
        logged_dict[1] = 'Interplay Entertainment'
        assert logged_dict[1] == 'Interplay Entertainment'
        assert logged_dict.log()[-1].__contains__('get')
        storage = logged_dict[1]
        assert logged_dict.log()[-1].__contains__('get')

        with pytest.raises(KeyError):
            storage = logged_dict['error']
        with pytest.raises(TypeError):
            storage = logged_dict[{}]

    def test_del(self):
        logged_dict = DictWithFileLog(path_to_file)
        logged_dict[1] = 'Interplay Entertainment'
        logged_dict.__delitem__(1)
        assert logged_dict.log()[-1].__contains__('del')

        with pytest.raises(KeyError):
            logged_dict.__delitem__('error')
        with pytest.raises(TypeError):
            logged_dict.__delitem__()






