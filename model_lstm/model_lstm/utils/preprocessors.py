def convert_labels(label):
    convert_dict = {4: 1, 0: 0}
    new_label = convert_dict[label]
    return new_label