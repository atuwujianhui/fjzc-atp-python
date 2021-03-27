#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-21
# 文件：case_assert.py
# 说明：用例执行结果断言，适合接口自动化测试，
#       因为接口自动化测试一般返回JSON或者XML格式，用例执行的正确性判断比较有规律。
#       此处使用Python代码片段作为断言执行脚本
# （待完善）

'''
证明Web UI操作成功的方式：
1、某一特定组件出现，一般是页面跳转（简单）；
2、某一特定数据出现/或者消失，一般是数据处理，数据变化但页面不跳转（稍微复杂）；
3、某一特特定数据添加或者修改成功，但是不在页面上显示，这时候可能需要查询、查看明细字段（复杂）。
4、其他
所以：暂时认为断言还是让测试人员自己写逻辑比较合适。
'''

class CaseAssert():

    def __init__(self):
        self.assert_result = {"status": "1"}

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-21
    @ 说明：用例执行结果断言（执行测试人员编写的基于Python语法的断言脚本）
            但是函数“exec”没有返回值，还需要进一步获取断言结果，待完善。
    @ 参数：
    '''
    def case_aseert(self, python_code, __response_data__):
        print(self.assert_result)
        # 执行Python代码片段，片段中的变量与参数“__response_data__”的名称一致即可使用该参数
        exec(python_code)
        print(self.assert_result)

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-21
@ 说明：测试
@ 参数：
'''
if __name__ == "__main__":

    # Python脚本片段，注意：需要遵循Python的语法格式，从顶格开始
    python_code = """
print(__response_data__.get("status"), __response_data__.get("msg"))
    """
    # 返回断言结果脚本片段
    python_code += "\nself.assert_result['status'] = 0"

    # 返回数据数据，参考借口自动化测试返回结果
    response_data = {
        "msg": "登录异常，请刷新后重试",
        "data": "",
        "status": 10014
    }

    # 执行Python代码片段
    case_assert = CaseAssert()
    case_assert.case_aseert(python_code, response_data)

