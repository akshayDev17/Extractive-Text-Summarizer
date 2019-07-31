""" The module which gives the summary after the
preprocessing has been done"""

def select_sentence(score_dict, sentence_list, limit):

    """ Select N highest scoring sentences to form the summary, N being the
    desired length of summary."""

    sorted_values = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
    sentence_index_list = []
    for i in range(limit):
        sentence_index_list.append(sorted_values[i][0])
    sentence_index_list.sort()
    summary = []
    for i in sentence_index_list:
        summary.append(sentence_list[i])

    return '.'.join(summary)
