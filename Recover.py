import subprocess as s
# subprocess module is a powerful part of the Python standard library that lets you run external programs and inspect their outputs easily
import re
# re module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).


# Finding out how many partitions are attached with the system
o = s.Popen('lsblk -o NAME,MOUNTPOINT | grep -e "/media/"', stdout=s.PIPE, shell=True)
y = re.sub('[^A-Za-z0-9/ \n]+', '', o.stdout.read().decode('utf-8')).splitlines()


# x contains all the partitions name which are attached with the system.
if not y:
    print("No partition found.")
    print("Check if the thumbdrive is mounted properly.")
    exit()
    
    
else:
    w = s.Popen('whoami', stdout=s.PIPE, shell=True).stdout.read().decode('ascii').strip()
    l, partitions = list(), list()
    for i in y:
        l = i.split()
        partitions.append(l)
# drives contains all the partions names or thumbdrive.

    while(1):
        print('All Partitions found are below\n____ __ __________\n')
        for i in range(1, len(partitions) + 1):
            print(str(i) + '\t' + re.sub('/media/' + w + '/', '', partitions[i-1][1]))

        c = int(input('Enter partition number to check: ' ))
        f = input('Enter temporary image name for the partition: ')
        
# Creating a dd file of that thumbdrive        
        s.Popen('umount /dev/' + partitions[c-1][0], stdout=s.PIPE, shell=True)
        p = s.Popen('sudo dd if=/dev/' + partitionsspartitions[c-1][0] + ' of=' + f, stdin=s.PIPE, stdout=s.PIPE, shell=True)
        p.communicate()
        deleted_files = list()
        
# Collecting all the files which were deleted from this partions by using the given command.
        c = s.Popen('fls ' + f + ' | grep -e "*"', stdout=s.PIPE, shell=True).stdout.read().decode('utf-8').splitlines()
        for i in c:
            l = i.split()
            l[2] = re.sub('[^0-9]+', '', l[2])
            deleted_files.append(l)
            
# files contains all the files which can be recoverred.         
        if not deleted_files:
            print('No recoverable files found. Try another partition.')
            exit()
        else:
            while(1):
                for i in range(1, len(deleted_files) + 1):
                    print(str(i) + '\t' + deleted_files[i-1][3])
                c = int(input('Enter the file number to recover : '))
                
# Given below 2 commands will recover the file from the thumbdrive.                
                print(s.Popen('istat ' + f + ' ' + deleted_files[c-1][2], stdout=s.PIPE, shell=True).stdout.read().decode('utf-8'))
                s.Popen('icat ' + f + ' ' + deleted_files[c-1][2] + ' > ' + deleted_files[c-1][3], stdout=s.PIPE, shell=True)
                c = input('Do you want to recover file from this partition again? ')
            
                if c.lower() == 'n':
                    c = s.Popen('rm -f ' + f, stdout=s.PIPE, shell=True)
                    break

        c = input('Do you want to recover file from other partitions? ')
        if c.lower() == 'n':
            exit()
