from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        pass


# KMP + Binary Search
"""
    void computeLPSArray(string &pat, int M, int *lps)
	{
		int len = 0;
		lps[0] = 0;
		int i = 1;

		while (i < M)
		{
			if (pat[i] == pat[len])
			{
				len++;
				lps[i] = len;
				i++;
			}
			else
			{
				if (len != 0)
				{
					len = lps[len - 1];
				}
				else
				{
					lps[i] = 0;
					i++;
				}
			}
		}
	}

	vector<int> KMPSearch(string &pat, string &txt)
	{
		vector<int> v;
		int M = pat.length();
		int N = txt.length();
		int lps[M];
		computeLPSArray(pat, M, lps);

		int i = 0;
		int j = 0;
		while (i < N)
		{
			if (pat[j] == txt[i])
			{
				j++;
				i++;
			}

			if (j == M)
			{
				v.push_back(i - j);
				j = lps[j - 1];
			}
			else if (i < N && pat[j] != txt[i])
			{
				if (j != 0)
					j = lps[j - 1];
				else
					i = i + 1;
			}
		}

		return v;
	}
	vector<int> beautifulIndices(string s, string a, string b, int k)
	{
		vector<int> indA = KMPSearch(a, s);
		vector<int> indB = KMPSearch(b, s);
		vector<int> result;

		for (int i = 0; i < indA.size(); i++)
		{
			auto it1 = lower_bound(indB.begin(), indB.end(), indA[i]);
			auto it2 = lower_bound(indB.begin(), indB.end(), indA[i] - k);
			if (it1 != indB.end() && abs(*it1 - indA[i]) <= k)
			{
				result.push_back(indA[i]);
				continue;
			}
			if (it2 != indB.end() && abs(*it2 - indA[i]) <= k)
			{
				result.push_back(indA[i]);
			}
		}
		return result;
	}
"""
