class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::unordered_map<int, int> count;
        std::unordered_map<int, int> unique;

        for (int v : arr) {
            count[v] = count[v] + 1;
        }

        for (const auto& entry : count) {
            int v = entry.second;
            if (unique.count(v) > 0) {
                return false;
            }
            unique[v] = 1;
        }

        return true;
    }
};