# from typing import Dict, Union

# # custom types
# Key = str
# Value = Union[int] 

# my_dict: Dict[str, int] = {
#     "name" : "Jawwad Ahmad",
#     "father_name" : "Abdul Jabbar",
#     "age" : 26,
#     "height" : 1.80,
#     "married" : False,
# }


from scipy import stats
speed = [10,10, 20, 20, 5, 5]

x = stats.mode(speed)

print(x)