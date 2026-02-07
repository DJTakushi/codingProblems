#include <iostream>
#include "medianOfTwoSortedArrays.h"

double Solution::findMedianSortedArraysClaude(vector<int> &nums1, vector<int> &nums2)
{
    int m = nums1.size();
    int n = nums2.size();
    if (m > n)
    {
        return findMedianSortedArraysClaude(nums2, nums1);
    }
    int imin = 0, imax = m, half_len = (m + n + 1) / 2;
    while (imin <= imax)
    {
        int i = (imin + imax) / 2;
        int j = half_len - i;
        if (i < imax && nums2[j - 1] > nums1[i])
        {
            imin = i + 1;
        }
        else if (i > imin && nums1[i - 1] > nums2[j])
        {
            imax = i - 1;
        }
        else
        {
            int max_of_left = 0;
            if (i == 0)
            {
                max_of_left = nums2[j - 1];
            }
            else if (j == 0)
            {
                max_of_left = nums1[i - 1];
            }
            else
            {
                max_of_left = max(nums1[i - 1], nums2[j - 1]);
            }
            if ((m + n) % 2 == 1)
            {
                return max_of_left;
            }

            int min_of_right = 0;
            if (i == m)
            {
                min_of_right = nums2[j];
            }
            else if (j == n)
            {
                min_of_right = nums1[i];
            }
            else
            {
                min_of_right = min(nums1[i], nums2[j]);
            }

            return (max_of_left + min_of_right) / 2.0;
        }
    }
    return 0.0;
}

double Solution::findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
{
    size_t lenTotal = nums1.size() + nums2.size();
    size_t idx1 = 0, idx2 = 0;
    vector<int> sorted;

    size_t sizeTgt = lenTotal / 2 + 1;
    while (sorted.size() < sizeTgt)
    {
        if (idx2 >= nums2.size()) // 
        {
            sorted.push_back(nums1[idx1]);
            idx1++;
        }
        else if (idx1 >= nums1.size())
        {
            sorted.push_back(nums2[idx2]);
            idx2++;
        }
        else
        {
            int t1 = nums1[idx1];
            int t2 = nums2[idx2];
            if (t1 <= t2)
            {
                sorted.push_back(t1);
                idx1++;
            }
            else if (t2 < t1)
            {
                sorted.push_back(t2);
                idx2++;
            }
            else
            {
                std::cout << "UGH?????" << std::endl;
            }
        }
    }

    double median = -999.9;
    if (lenTotal % 2 == 1) // odd
    {
        median = sorted.back();
    }
    else
    {
        median = (sorted.back() + sorted[sorted.size() - 2]) / 2.0;
    }

    return median;
}
