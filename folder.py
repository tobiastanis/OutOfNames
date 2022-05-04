import os.path

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'Structure')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)



