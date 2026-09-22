class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash = {}
        for i in strs:
            count = Counter(i)
            key = tuple(sorted(count.items()))

            if key not in myhash:
                myhash[key] = [] #new anagram
            myhash[key].append(i) #group anagram

        return list(myhash.values())
