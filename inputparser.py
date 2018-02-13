import re

class InputParser(object):
    def __init__(self, interpreter):
        self._interpreter = interpreter
        self._re_input_line = re.compile(self._interpreter.RE_INPUT_LINE)
    
    def process_line(self, line):
        for m in self._re_input_line.finditer(line):
            keyword = m.group(1)
            arguments = None if m.group(2) is None else m.group(2).strip()
            
            keyword_handler = getattr(self._interpreter, "cmd_" + keyword + "_handler", None)
            if keyword_handler is not None:
                keyword_handler(arguments)
            else:
                self.unhandled_keyword(keyword)

    def unhandled_keyword(self, keyword):
        try:
            self._interpreter.unhandled_keyword(keyword)
            return
        except AttributeError:
            pass #to prevent exception chaining
        raise Exception('unhandled keyword: '+ keyword)
