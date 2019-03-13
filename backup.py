import shutil
shutil.copyfile('./config.fish',
                '../../Documents/Backups/config.fish')
print("I have succesfully backed up the config.fish on the hour!")
