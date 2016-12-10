def build_movements(keys):
    """Build a movement table."""
    movements = {}
    rows = len(keys)
    cols = len(keys[0])
    for row, col in [(r, c) for r in xrange(0, rows) for c in xrange(0, cols)]:
        from_key = keys[row][col]
        from_here = movements.get(from_key, {})

        def is_good(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            return keys[r][c] != ' ' 

        from_here['U'] = keys[row - 1][col] if is_good(row - 1, col) else from_key
        from_here['D'] = keys[row + 1][col] if is_good(row + 1, col) else from_key
        from_here['L'] = keys[row][col - 1] if is_good(row, col - 1) else from_key
        from_here['R'] = keys[row][col + 1] if is_good(row, col + 1) else from_key

        movements[from_key] = from_here
    return movements
         

class Keypad(object):
    def __init__(self, keys):
        self.key = '5'
        self.code = ''
        self.movements = build_movements(keys)
    
    def move(self, instruction):
        from_here = self.movements[self.key]
        self.key  = from_here[instruction]
    
    def follow(self, lines_of_instructions):
        for instructions in lines_of_instructions:
            for i in instructions:
                self.move(i)
            self.code += self.key

    @classmethod
    def parse_keys(clazz, text):
        """Parse keys from a keypad image.

        >>> Keypad.parse_keys("123\\n456\\n789")
        [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        >>> Keypad.parse_keys("  123\\na456b\\n789  ")
        [[' ', ' ', '1', '2', '3'], ['a', '4', '5', '6', 'b'], ['7', '8', '9', ' ', ' ']]
        """
        lines = text.split('\n')
        keys = [list(x) for x in lines]
        return keys