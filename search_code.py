import os

def search_keyboard_events_in_py_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if ccc in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")
def search_keyboard_events_in_txt_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if ccc in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")

def search_keyboard_events_in_cpp_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".cpp"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if ccc in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")
def search_keyboard_events_in_c_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".c"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if ccc in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")
def search_keyboard_events_in_java_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if ccc in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")

if __name__ == "__main__":
    launage = input("Please choose the language you use（en/cn）")
    if launage == "cn":
        code_launage = input("请选择你使用的代码语言（python/C++/C/Java/txt文件）")
        aa = input("使用默认路径吗？（y/n）(默认为程序运行目录)")
        if aa == "n":
            directory = input("请输入搜索路径(绝对路径分隔符为\\)")
        elif aa == "y":
            directory = os.getcwd()
        ccc = input("请输入搜索内容")
        if code_launage == "txt文件" or code_launage == "txt":
            search_keyboard_events_in_txt_files(directory)
        elif code_launage == "python":
            search_keyboard_events_in_py_files(directory)
        elif code_launage == "C++":
            search_keyboard_events_in_cpp_files(directory)
        elif code_launage == "C":
            search_keyboard_events_in_c_files(directory)
        elif code_launage == "Java":
            search_keyboard_events_in_java_files(directory)
        else:
            print("错误: 无效的代码语言")            
    elif launage == "en":
        code_launage = input("Please choose the code language you use（python/C++/C/Java or txt files）")
        aa = input("Do you want to use the default path? (y/n) (The default path is the directory where the program is running)")
        if aa == "n":
            directory = input("Please enter the search path (The absolute path separator is \\")
        elif aa == "y":
            directory = os.getcwd()
        ccc = input("Please enter the search content")
        if code_launage == "txt files":
            search_keyboard_events_in_txt_files(directory)
        elif code_launage == "python":
            search_keyboard_events_in_py_files(directory)
        elif code_launage == "C++":
            search_keyboard_events_in_cpp_files(directory)
        elif code_launage == "C":
            search_keyboard_events_in_c_files(directory)
        elif code_launage == "Java":
            search_keyboard_events_in_java_files(directory)
        else:
            print("Error: Invalid code language")
input()