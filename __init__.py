import datetime

class PyLogger():
    def __init__(self, logpath="log.log", console_tags_to_hide=[], 
        file_tags_to_hide=[]):
        self.console_tags_to_hide = console_tags_to_hide
        self.logpath = logpath
        self.file_tags_to_hide = file_tags_to_hide

    def log(self, msg, tag="default"):
        cur_time = datetime.datetime.now()
        log_message = "(%s) [%s]: %s" % (str(cur_time), tag, msg)

        if tag not in (self.console_tags_to_hide): 
            print(log_message)

        if tag not in (self.file_tags_to_hide):
            with open(self.logpath, "a") as log_file:
                log_file.write(log_message + "\n")
