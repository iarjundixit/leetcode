class Solution {
public:
    int minimumPushes(string word) {
        vector<int> freq(26, 0);

        // Count frequency of each character
        for (char c : word) {
            freq[c - 'a']++;
        }

        // Sort frequencies in descending order
        sort(freq.begin(), freq.end(), greater<int>());

        int pushes = 0;

        // Assign costs: first 8 -> 1 push, next 8 -> 2 pushes, etc.
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) break;
            pushes += freq[i] * (i / 8 + 1);
        }

        return pushes;
    }
};