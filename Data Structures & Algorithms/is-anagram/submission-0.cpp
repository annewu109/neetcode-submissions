class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int sLetters[26] = {0};
        int tLetters[26] = {0};

        for (int i = 0; i < s.length(); i++) {
            sLetters[s[i] - 'a']++;
            tLetters[t[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (sLetters[i] != tLetters[i]) {
                return false;
            }
        }

        return true;
    }
};
