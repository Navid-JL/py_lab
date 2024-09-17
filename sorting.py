
def merge(left_seq: list, right_seq: list, seq: list):
    i = j = k = 0

    while i < len(left_seq) and j < len(right_seq):
        if left_seq[i] < right_seq[j]:
            seq[k] = left_seq[i]
            i += 1
        else:
            seq[k] = right_seq[j]
            j += 1
        k += 1

    while i < len(left_seq):
        seq[k] = left_seq[i]
        i += 1
        k += 1

    while j < len(right_seq):
        seq[k] = right_seq[j]
        j += 1
        k += 1


def merge_sort(seq: list):
    if len(seq) > 1:
        mid = len(seq) // 2
        left_seq = seq[:mid]
        right_seq = seq[mid:]
        merge_sort(left_seq)
        merge_sort(right_seq)
        merge(left_seq, right_seq, seq)


def insertion_sort(seq: list):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


def selection_sort(seq: list):
    for i in range(len(seq) - 1):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        min_value = seq.pop(min_index)
        seq.insert(i, min_value)


def bubble_sort(seq: list):
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


def counting_sort(seq: list):
    highest = max(seq) + 1
    helper_list = [0] * highest
    s_list = []

    for value in seq:
        helper_list[value] += 1

    for j in range(len(helper_list)):
        s_list.extend([j] * helper_list[j])

    return s_list
