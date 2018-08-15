# +3.
# Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, пример использования:
#
# with TimeIt() as t:
#     some_long_function()
#
# print('Execution time was:', t.time)