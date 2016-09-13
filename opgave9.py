def linear_merge(list1, list2):
  merged_list = []
  i = 0
  j = 0

  while True:
    if i == len(list1):
        return merged_list + list2[j:]
    if j == len(list2):
        return merged_list + list1[i:]

    if list1[i] <= list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

    print(merged_list)

linear_merge([1,3,6,9], [8,5,9,6])
