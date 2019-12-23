class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
            j += 1
        return i == len(name)

    def isLongPressedName_own_DP(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        m, n = len(name), len(typed)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m):
            for j in range(n):
                if j > 0 and typed[j] == typed[j-1]:
                    if name[i] == typed[j]:
                        dp[i+1][j+1] = dp[i][j]
                    dp[i+1][j+1] = dp[i+1][j+1] or dp[i+1][j]
                else:
                    if name[i] == typed[j]:
                        dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]

    def test(self):
        testCases = [
            ["alex", "aaleex"],
            ["saeed", "ssaaedd"],
            ["leelee", "lleeelee"],
            ["laiden", "laiden"],
            [
                "jadtsqddmmdzvwervizcudgedrguuyuzoaikzkhuxbzszqarfzywsgyvqefopkvrgapixgofzqtxlolqivjuajmxstqxsqxtawetkkelzvtqfbyxaxtceegxkolmgighpaynnkttszkcusamvyjmltsmepajibculdyilseuvmsszujnknxcxndyfamobqoocjdmjiwq",
                "jaaddtssqqddmmdzvvwwerrvviizcudgeedgguuuuyuzzoaikzkhhuxbbzsszzqaarrfzzywssggyyvqefooppkvrrggaapixxgoofzzqqttxxlloollqiivjuuajjmmxssttqqxssqqxxtawettkkkelzzvtqffbbyyxxaaxttcceeggxxkollmmgighhppaayynnnnktttszkkccussaamvvyjmmlttssmmeeppaajjibccuulldyilsseeuuvvmssszzuujjnknxxcxndyyfaamobqqooocjjdmjiiwwqq",
            ],
        ]
        for name, typed in testCases:
            res = self.isLongPressedName(name, typed)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
