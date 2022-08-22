#
# from string import ascii_lowercase
#
# # print(ascii_lowercase)
#
# # for i in ascii_lowercase:
# #     for j in ascii_lowercase:
# #         print(i + j)
# N = 5
# # def get_sum(N):
# #     for i in range(1, N + 1):
# #         j_s = 0
# #         for j in range(0, i+1):
# #             j_s += j
# #         yield j_s
# #
# #
# # print(get_sum(N).__next__(), sep=' ')
# # lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
# ############################################################################
#
# # lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
# #
# # lst = zip(*lst_in)
# # lst_1 = zip(*lst)
# # # for i in lst_1:
# # #     ls = [r for r in i if r != ' ']
# # #     print(*ls)
# # [print(*[r for r in i if r != ' ']) for i in lst_1]
#
# #############################################################################
#
# s = input()
# N = 10
# lst = list(zip(s, [i for i in range(N)]))
# print(lst)


# class PropertyLesson3:
#
#     def init(self):
#         self.__a = 5
#
#     @property
#     def a(self):
#         """
#         documentation
#         """
#
#     @a.getter
#     def a(self):
#         print("getter")
#         return self.__a
#
#     @a.setter
#     def a(self, val): # val = a + 1
#         print("setter")
#         self.__a = val



class AccountUser:

    def __init__(self, pin):
        self.__pin = pin
        self.__coast = 0


    def get_pin(self):
        return input('Enter pin:') == self.__pin


    @property
    def balance(self):
        if self.get_pin():
            return self.__coast

    # @balance.getter
    # def balance(self):
    #     if self.get_pin():
    #         return self.__coast

    @balance.setter
    def balance(self, val):
        self.__coast = val


user_1 = AccountUser('1234')
print(user_1.balance)
user_1.balance += 100
user_1.balance -= 10
print(user_1.balance)







