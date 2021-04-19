student_dict = {
    "student": ["Angela", "Brad", "Caroline"],
    "score": [85, 96, 73]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)