from bj_2839 import solution as solution_success
from bj_2839_fail import solution as solution_fail

for i in range(3, 5001):
    result_success = solution_success(i)
    result_fail = solution_fail(i)
    if result_success != result_fail:
        print(f'{i}: result_success: {result_success} result_fail: {result_fail}')
print(f'test finished')
