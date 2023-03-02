function findMedianSortedArrays(nums1, nums2) {
  let l1 = 0,
    r1 = nums1.length - 1;
  let l2 = 0,
    r2 = nums2.length - 1;

  if (nums1.length === 0 && nums2.length === 0) {
    return 0;
  } else if (nums1.length === 0) {
    if (nums2.length % 2) {
      return nums2[Math.floor(nums2.length / 2)];
    } else {
      return (
        (nums2[Math.floor(nums2.length / 2)] +
          nums2[Math.floor(nums2.length / 2) + 1]) /
        2
      );
    }
  } else if (nums2.length === 0) {
    if (nums1.length % 2) {
      return nums1[Math.floor(nums1.length / 2)];
    } else {
      return (
        (nums1[Math.floor(nums1.length / 2)] +
          nums1[Math.floor(nums1.length / 2) + 1]) /
        2
      );
    }
  }

  while (l1 < r1 || l2 < r2) {
    const m1 = Math.floor((l1 + r1) / 2);
    const m2 = Math.floor((l2 + r2) / 2);

    if (nums1[m1] < nums2[m2]) {
      l1 = m1 + 1;
      r2 = m2;
    } else if (nums1[m1] > nums2[m2]) {
      r1 = m1;
      l2 = m2 + 1;
    } else {
      return nums1[m1];
    }
  }

  if ((nums1.length + nums2.length) % 2) {
    return Math.min(nums1[l1], nums2[l2]);
  } else {
    return (nums1[l1] + nums2[l2]) / 2;
  }
}

console.log(findMedianSortedArrays([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]));
