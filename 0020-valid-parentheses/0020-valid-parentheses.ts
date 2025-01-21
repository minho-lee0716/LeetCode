function isValid(s: string): boolean {
    const stack: string[] = [];
    const mapping: { [key: string]: string } = { "(": ")", "{": "}", "[": "]" };

    for (const char of s) {
        if (mapping.hasOwnProperty(char)) {
            stack.push(char);
        } else if (stack.length === 0) {
            return false;
        } else if (char === mapping[stack.pop()!]) {
            continue;
        } else {
            return false;
        }
    }

    return stack.length === 0;
  }