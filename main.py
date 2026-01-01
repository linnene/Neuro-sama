
# from config import config
# import os

"""
test1:
测试将 output 目录下的所有文件，使用 BaseMes 进行解析后，保存到 pending_data 目录下
"""

# from src.neuro_sama.parser import parse_jsonl_file, save_as_jsonl
# from src.neuro_sama.models.dialogue import BaseMes

# output_path = config.cleaned_dir
# files = os.listdir(config.raw_dir)

# for file in files:
#     save_as_jsonl(parse_jsonl_file(config.raw_dir+file,BaseMes),output_path+file)


"""
test2:
测试将 pending_data 目录下的所有文件，使用 build_repeat_segments 进行解析后，打印结果
"""

# from src.neuro_sama.parser import build_repeat_segments_Iterator, read_jsonl_file

# files = os.listdir(config.cleaned_dir)

# for file in files:
#     print(build_repeat_segments_Iterator(read_jsonl_file(config.cleaned_dir+file)))
