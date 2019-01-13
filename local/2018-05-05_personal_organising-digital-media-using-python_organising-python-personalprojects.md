Because i'm looking to travel a lot over the next few years, I've been making special efforts to organise my stuff. For a very long time, digitising photos has been an item on the to do list. It took a whole afternoon, but I managed to digitise all of my physical photos from before the age of 21 or so. That task seems easy compared to sorting out digital media! I have come across so many directories of photos, and copies all over my computers.

I've written this script to help collate all of the photos in one place, and to attempt to check for duplicates along the way. If you have a similar task to do, and want to explore some basic python at the same time, feel free to play with this script.

Importantly, we do not do any deletion operations here. We only copy files (selectively) into new folders. Personally, i'm anticipating a lot more work to manually sort through the photos to detect duplicates and other junk.

```  
    import os  
    import hashlib  
    from tqdm import tnrange  
    import pandas as pd  
    import shutil  
    # List of all directories that we want to check, full file paths  
    directories = [  
    r"C:\Users\Damnt\Google Drive\Google Photos",  
    r'C:\Users\Damnt\Pictures\All pictures',  
    r'C:\Users\Damnt\Pictures\Facebook1',  
    r'C:\Users\Damnt\Pictures\Facebook2',  
    r'C:\Users\Damnt\Pictures\Google Photos',  
    r'C:\Users\Damnt\Pictures\Photos',  
    r'C:\Users\Damnt\Pictures\Pictures',  
    r'C:\Users\Damnt\Pictures\Recent iphone',  
    r'C:\Users\Damnt\Pictures\Recent iphone2'  
    ]


    # Where we're going to put new files  
    new_base_dir = r"C:\Users\Damnt\Pictures\Collated"

    # This will help produce an excel spreadsheet with info about the files  
    manifest = pd.DataFrame(columns=["original_filename", "original_dir", "new_filename", "new_dir",   
                                     "file_hash", "file_size", "file_type", "copied"])


    # This section walks through each of our directories and sub directories looking for files.  
    # The tnrange import allows us to easily monitor progress and ETA!  
    count = 0  
    for i in tnrange(len(directories)):  
        for root, subdirs, files in os.walk(directories[i]):

            for f in tnrange(len(files), leave=False):

                # Split a filename into two parts, the filename and the extension  
                try:  
                    fname, ftype = files[f].split(".")  
                except:  
                    print("File with bad extension or filename", root, files[f])  
                    raise

                # The first time you run this, you may want to comment out everything below  
                # This will make sure the above lines work, that is, all files are well formed names

                # Record information about the files  
                manifest.loc[count, "original_filename"] = files[f]  
                manifest.loc[count, "original_dir"] = root

                new_filename = str(count) + "." + ftype.lower()  
                manifest.loc[count, "new_filename"] = new_filename

                # New files go into a directory with the rest of their file types  
                new_directory = os.path.join(new_base_dir, ftype.upper())  
                manifest.loc[count, "new_directory"] = new_directory

                # Make new directories for different extensions  
                if not os.path.exists(new_directory):  
                    os.makedirs(new_directory)  
                    print("Made directory", new_directory)

                full_original_path = os.path.join(root, files[f])  
                full_new_path = os.path.join(new_base_dir, ftype.upper(), new_filename)

                # Hashing! This helps us work out if two files are the same.   
                # Great for automatically skipping duplicates.  
                pre_hash = manifest["file_hash"].tolist()  
                file_hash = hashlib.md5(open(full_original_path, 'rb').read()).hexdigest()  
                manifest.loc[count, "file_hash"] = file_hash

                # Get the filesize information  
                file_size = os.path.getsize(full_original_path)  
                manifest.loc[count, "file_size"] = file_size  
                manifest.loc[count, "file_type"] = ftype.upper()

                # Make sure file not in the hash list, if it's not, then copy the file to the new directory  
                if file_hash not in pre_hash:  
                    manifest.loc[count, "copied"] = True  
                    shutil.copy(full_original_path, full_new_path)

                # increment the manifest  
                count+=1

    manifest.to_excel("180505_pictures_manifest.xlsx")
```

Best of luck with your collection!