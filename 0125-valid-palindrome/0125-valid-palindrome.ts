function isPalindrome(s: string): boolean {
    s = Array.from(s).filter(char => /[a-zA-Z0-9]/.test(char)).join('').toLowerCase();

    const size = s.length;
    const half = Math.floor(size / 2);

    if (size % 2 === 0) {
        return s.slice(0, half) === s.slice(half).split('').reverse().join('');
    } else {
        return s.slice(0, half) === s.slice(half + 1).split('').reverse().join('');
    }
};