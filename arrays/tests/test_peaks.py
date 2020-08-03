from arrays.peaks import peaks


def test_peaks():
    nums1 = [1]
    nums2 = [1, 2]
    nums3 = [1, 2, 1]
    nums4 = [1, 3, 2, 5, 2, 1, 4, 3]

    assert peaks(nums1) == []
    assert peaks(nums2) == []
    assert peaks(nums3) == [2]
    assert peaks(nums4) == [3, 5, 4]
