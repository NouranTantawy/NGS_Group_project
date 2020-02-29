#Import_library_os_to_use_terminal_and_shutil_to_use_move_function
import os 
import shutil
#creat_two_list_to_add_the_name_of_forward_and_reverse_samples
forward_read=[]
revers_read=[]
#write_the_full_path_of_my_samples
path='/home/emam/ngs2/fqData/extracted/'
#change_python_directory_to_fqdatafile(extracted)
os.chdir(path) 
#we_have_fixed_patern_in_both_forward_and_reverse_reads
#forward_read_naming_ends_.1.fq
#reverse_read_name_end_.2.fq
data=os.listdir()
for i in data: 
     if i[-4]=='1': 
        forward_read.append(i) 
    
for i in data: 
     if i[-4]=='2': 
        revers_read.append(i)

#move_forward_reads_into_new_dirctory
os.mkdir("/home/emam/ngs2/fqData/extracted/forward")  
forward_distination='/home/emam/ngs2/fqData/extracted/forward/'
forward_read.sort()
for i in forward_read: 
    shutil.move(path+i, forward_distination)
    
#move_reverse_reads_into_new_dirctory
os.mkdir("/home/emam/ngs2/fqData/extracted/reverse")  
reverse_distination='/home/emam/ngs2/fqData/extracted/reverse/'
reverse_read.sort()
for i in reverse_read: 
    shutil.move(path+i, reverse_distination) 
