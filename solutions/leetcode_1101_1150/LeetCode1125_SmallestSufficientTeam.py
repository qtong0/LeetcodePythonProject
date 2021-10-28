from typing import List


class Solution:
    # TC: O(people * 2 ^ skills)
    # SC: O(2 ^ skill)
    #
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skillmap = {skill: i for i, skill in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            p_skill = 0
            for skill in p:
                if skill in skillmap:
                    p_skill |= 1 << skillmap[skill]
            for skill_set, need in list(dp.items()):
                with_him = skill_set | p_skill
                if with_him == skill_set:
                    continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]



    # Own DFS, TLE
    def smallestSufficientTeam_own_DFS_TLE(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sorted_people = sorted([[skills, i] for i, skills in enumerate(people)], key=lambda x: -len(x[0]))
        self.res = []
        self.dfs(sorted_people, 0, [], set(req_skills))
        return self.res

    def dfs(self, sorted_people, i, curr, req_skills):
        if not req_skills:
            if not self.res or len(self.res) > len(curr):
                self.res = list(curr)
            return
        if self.res and len(curr) > len(self.res):
            return
        for idx in range(i, len(sorted_people)):
            p_skills = sorted_people[idx][0]
            common = set(p_skills) & req_skills
            req_skills = req_skills - common
            curr.append(sorted_people[idx][1])
            self.dfs(sorted_people, i+1, curr, req_skills)
            req_skills = req_skills.union(common)
            curr.pop()



    def test(self):
        test_cases = [
            # [
            #     ["java","nodejs","reactjs"],
            #     [["java"],["nodejs"],["nodejs","reactjs"]],
            # ],
            [
                ["algorithms","math","java","reactjs","csharp","aws"],
                [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]],
            ],
        ]
        for req_skills, people in test_cases:
            res = self.smallestSufficientTeam(req_skills, people)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
