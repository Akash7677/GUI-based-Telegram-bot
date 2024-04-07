# # def test(s: str):
# #     count = 1
# #     result = []
# #     s_list = list(s)
# #     for i, ch in enumerate(s_list):
# #         if i == 0:
# #             continue
# #         prev = i - 1
# #         if ch == s_list[prev]:
# #             count += 1
# #         else:
# #             result.append(f"{count}{s_list[prev]}")
# #             count = 1  # Reset count for the current character
# #             print(result)
# #     result.append(f"{count}{s_list[-1]}")  # Append the count for the last character
# #     result_string = "".join(result)
# #     return result_string
# #
# # s = "aaabbbcd"
# # r = test(s)
# # print(r)
#
# #
# # def test_2(arr: list[int], k):
# #     set_ = set(arr)
# #     list_ = list(set_)
# #     result=[]
# #     for i in range(k):
# #         max_num = max(list_)
# #         result.append(max_num)
# #         list_.remove(max_num)
# #     return result
# # arr = [1, 5, 4, 4, 2]
# # k =
# # r = test_2(arr, k)
# # print(r)
#
#
# A = [1,2,3]
# B = [2,2,3]
# C = [3,3,3]
#
# D = [1,2,2,2,3,3,3,3,3]
#
# result = A + B + C
# res_list = []
# for i in range(len(result)):
#     v = min(result)
#     res_list.append(v)
#     result.remove(v)
# print(res_list)

a = "hellow this is new work"

# Define a custom sorting function
def custom_sort(word):
    return (len(word), word)

# Split the string into a list of words
words = a.split()

# Sort the list of words using the custom sorting function
sorted_words = sorted(words, key=custom_sort)

# Join the sorted words back into a string
sorted_string = ' '.join(sorted_words)

print(sorted_string)