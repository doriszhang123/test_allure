import pytest,allure

class Test_Abc:
    def setup(self):
        pass
    def teardown(self):
        pass
    @pytest.mark.parametrize('a',[1,2,3])
    @allure.severity("CRITICAL")
    @allure.step('我是测试步骤001')
    def test_abc_001(self,a):
        allure.attach('描述','我是测试步骤001的描述~~~~~~~')
        assert a != 2

if __name__ == '__main__':
    pytest.main(["-s","--alluredir report","test_001.py"])
