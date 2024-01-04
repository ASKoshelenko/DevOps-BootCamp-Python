>Please use branch ```clean-archive``` for this task that already exist in your forked repository after you has been started task
# clean-archive

Create script _clean_app.py_ that:  
- [ ] Take a zip archive name as an argument:


        python clean_app.py <zip-file name>


- [ ] Unzip the archive to a temp directory

- [ ] Remove folders that don't contain _\_\_init\_\_.py_. Only the root folder can be without _\_\_init\_\_.py_.

- [ ] Add cleaned.txt with a sorted list of the removed folders. Folders should be listed with relative paths. One folder per line. For instance:


        example1\handlers\actions
        example3
        …


- [ ] A folder without _\_\_init\_\_.py_ has to be removed even if its child folders contain _\_\_init\_\_.py_. In this case, only the parent folder name has to be output to _cleaned.txt_.

- [ ] _cleaned.txt_ has to be added even if no folders are removed.

- [ ] Create new archive with _\_new_ prefix (_<old_name>\_new.zip_) 

- [ ] Add logging to the script.

