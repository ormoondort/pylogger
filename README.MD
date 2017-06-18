# pylogger
Library used for logging to console and to file.

## Usage
```
from pylogger import PyLogger

logger = PyLogger(logpath="log.log", console_tags_to_hide=[], 
    file_tags_to_hide=[])

logger.log("Something")
logger.log("Something", tag="tag1")
logger.log("something else", "tag2")
```