/**
 * @param {string} s
 * @return {boolean}
 */
function isValid(s) {
  const stack = [];
  const bracketsMap = {
    ')': '(',
    '}': '{',
    ']': '['
  };

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (char === '(' || char === '{' || char === '[') {
      stack.push(char);
    } else {
      const matchingOpeningBracket = bracketsMap[char];
      const lastBracket = stack.pop();

      if (lastBracket !== matchingOpeningBracket) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
