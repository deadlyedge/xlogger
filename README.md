# Something about xlogger
I'm a python starter, when I learn the logging section, 
I thought that writing the logging format is so 'non-python',
and I have to write the same 'anti-human' codes every where.
Logs are important and should be used more. And in more simple way.

So I checked StackOverflow for some inspiration, and I actually learned some.

Here is the module I made, in fact, it's the first one I wrote that should be
shared at pypi I thought.

Hope you guys enjoy it:)

## Usage
Install or just copy the code, it have no dependencies.

add line to your code:
```python
from xlogger.xlogger import get_my_logger

logger = get_my_logger(__name__)
```
and then just use logger as usual.

![](https://github.com/deadlyedge/xlogger/blob/master/static/screenshot1.png)

## Main references
'How can I color Python logging output?'

https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output

## Thank
Sergey Pleshakov - my code base on your code.
