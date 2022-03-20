
# Problem Statement: 
Design a file recovery algorithm that can recover all sorts of files from any point of time in your system. The backup and recovery process should be secure, and user authentication based on attributes should be performed before the recovery process begins.

# Watch video for Demo:

### Features
1. Recover accidentaly deleted files from your thumbstick
1. Choose which files to recover

### What won't work
1. Recover files from unallocated [or] deleted partitions

### To Run this file,
1. Make sure [SleuthKit](https://www.sleuthkit.org/sleuthkit/download.php "SleuthKit download page") and [Python 3.x](https://www.python.org/downloads/ "Python download page") is installed
1. [Clone](https://github.com/Suraj0307/DSA-Challenge4) this repo
1. Run the recover.py script
    ```cmd
      python3 recover.py
    ```
1. Select the partition with the deleted file using the corresponding number
1. Give a name for the temporary image of the partiton that will be created. This file will be as large as the partition. THIS PROCESS WILL TAKE TIME. DON'T PANIC!
1. Select the file to recover using the corresponding number

