"""Extra problems from the original (pre-playlist) request, in the same one-page schema
as data_problems.py. These are NOT from the linked YouTube playlist, so video_note says so
plainly instead of naming a fabricated video."""

NO_VIDEO = ("Not in the linked YouTube playlist — carried over from the original problem "
            "list you gave before the playlist link. No video source for this one.")

PROBLEMS = []

PROBLEMS.append(dict(
    title="Maximum Product Subarray", lc_num="152", difficulty="MEDIUM", pattern="DP (Track Max & Min)",
    video_note=NO_VIDEO,
    problem="Given an integer array, find the contiguous subarray with the largest product and return that product.",
    trigger="\"maximum product subarray\" with negatives in play → track BOTH a running max and running min (two negatives make a positive).",
    clarify="Can the array contain zero(s)? Negative numbers guaranteed possible?",
    brute_idea="Check every subarray's product directly.",
    brute_code="""def max_product(nums):
    best = nums[0]
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            best = max(best, product)
    return best""",
    brute_time="O(n²)", brute_space="O(1)",
    bottleneck="A single running max can't handle negatives -- a very negative running product times another negative can become the new best, so max alone loses information.",
    optimal_insight="Track both current_max and current_min ending at each index. On a negative number, swap them before combining, since multiplying by a negative flips which one becomes bigger.",
    optimal_code="""def max_product(nums):
    result = cur_max = cur_min = nums[0]
    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)
        result = max(result, cur_max)
    return result""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[2,3,-2,4] -> max builds to 6 via [2,3], dips at -2, 4 alone can't beat 6, result stays 6. Edge: zero in the array, e.g. [-2,0,-1] -> zero resets both max/min to 0, result=0.",
    other_edges="single negative number; even count of negatives (whole array is the answer); all zeros.",
    memory_hook="\"Two negatives make a positive -- track the min too, not just the max.\"",
))

PROBLEMS.append(dict(
    title="Find the Duplicate Number", lc_num="287", difficulty="MEDIUM", pattern="Fast & Slow Pointers",
    video_note=NO_VIDEO,
    problem="Given an array of n+1 integers with values in [1,n], exactly one value repeats (possibly more than twice); find it without modifying the array, in O(1) space.",
    trigger="\"array with values 1..n\", find duplicate, O(1) space → treat values as 'next pointers' into the array; a duplicate creates a cycle, find it with Floyd's algorithm.",
    clarify="Can the duplicate value repeat more than twice? Must the array stay unmodified?",
    brute_idea="Hash set: return the first value already seen.",
    brute_code="""def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="The hash set uses O(n) memory just to remember visited values, when the values themselves (being valid indices) can act as pointers with no extra memory.",
    optimal_insight="Index i 'points to' index nums[i]. A duplicate means two indices point to the same place -- a cycle. Floyd's Tortoise & Hare finds the cycle's entrance, which is the duplicate.",
    optimal_code="""def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]
    return slow""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[1,3,4,2,2] -> phase 1 meets at 2, phase 2 (reset+walk together) also converges at 2. Edge: duplicate repeats 3+ times, e.g. [1,2,2,2] with n=3 -> cycle structure still holds, still converges correctly.",
    other_edges="duplicate equal to n; duplicate equal to 1; smallest array n=1 -> [1,1].",
    memory_hook="\"Values point to indices -- a duplicate makes a loop, hunt it like a cycle.\"",
))

PROBLEMS.append(dict(
    title="Single Number", lc_num="136", difficulty="EASY", pattern="Bit Manipulation (XOR)",
    video_note=NO_VIDEO,
    problem="Every element in a non-empty array appears exactly twice except one; find that single element in O(n) time, O(1) space.",
    trigger="\"every element twice except one\", O(1) space → XOR cancels pairs.",
    clarify="Guaranteed exactly one element appears once, all others exactly twice (not three+)?",
    brute_idea="Hash map counts, then scan for the count-1 entry.",
    brute_code="""from collections import Counter

def single_number(nums):
    counts = Counter(nums)
    for val, cnt in counts.items():
        if cnt == 1:
            return val""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="Storing every value's count uses O(n) memory just to detect pairs, when an operation exists that cancels pairs automatically with no memory.",
    optimal_insight="x XOR x = 0 and x XOR 0 = x. XOR-ing the whole array cancels every duplicate pair, leaving only the singleton.",
    optimal_code="""def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[4,1,2,1,2] -> XOR-ing all: the two 1's cancel, the two 2's cancel, leaves 4. Edge: single-element array [7] -> 0 XOR 7 = 7.",
    other_edges="negative numbers (XOR works the same on two's complement); the singleton is 0 itself; singleton at the start vs end.",
    memory_hook="\"XOR cancels pairs -- whatever survives is the one without a partner.\"",
))

PROBLEMS.append(dict(
    title="Move Zeroes", lc_num="283", difficulty="EASY", pattern="Two Pointers (In-Place Partition)",
    video_note=NO_VIDEO,
    problem="Given an array, move all zeroes to the end while keeping the relative order of non-zero elements, in-place.",
    trigger="\"move/partition in-place, preserve relative order\" → Two Pointers, one marks the next write slot.",
    clarify="Must this be in-place (no new array)? Keep non-zero elements' original relative order?",
    brute_idea="Build a new list of non-zeros, then zeroes, and copy back over the original.",
    brute_code="""def move_zeroes(nums):
    non_zero = [x for x in nums if x != 0]
    zero_count = len(nums) - len(non_zero)
    nums[:] = non_zero + [0] * zero_count""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="Building a second array uses O(n) extra space when the same array can be rearranged directly with two pointers.",
    optimal_insight="insert_pos tracks where the next non-zero should go. Scan with i; on a non-zero, swap it into insert_pos and advance -- the swap pushes the displaced zero further right automatically.",
    optimal_code="""def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[0,1,0,3,12] -> swaps build up to [1,3,12,0,0]. Edge: no zeroes at all, e.g. [1,2,3] -> every swap is with itself, array unchanged.",
    other_edges="all zeroes; single element; zeroes already all at the end.",
    memory_hook="\"Slow pointer marks the next non-zero slot; swap it in as you scan.\"",
))

PROBLEMS.append(dict(
    title="Two Sum II - Input Array Is Sorted", lc_num="167", difficulty="MEDIUM", pattern="Two Pointers",
    video_note=NO_VIDEO,
    problem="Given a sorted array and a target, find two numbers that add up to it and return their 1-indexed positions.",
    trigger="\"sorted array, find a pair summing to target\" → Two Pointers converging from both ends.",
    clarify="Array guaranteed sorted ascending? Exactly one valid pair? 1-indexed output?",
    brute_idea="Check every pair of indices.",
    brute_code="""def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]""",
    brute_time="O(n²)", brute_space="O(1)",
    bottleneck="Checking every pair ignores the sorted order, which tells you exactly which direction fixes an incorrect sum.",
    optimal_insight="Sorted order means moving the left pointer right can only increase the sum, moving right left can only decrease it -- narrow from both ends.",
    optimal_code="""def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[2,7,11,15], target=9 -> 2+15 too big, shrink right twice, 2+7=9 -> [1,2]. Edge: matching pair are duplicate values -- pointers still converge correctly.",
    other_edges="smallest array (2 elements); negative numbers present; target needs first+last elements.",
    memory_hook="\"Sorted array, so walk the pointers toward the target from both ends.\"",
))

PROBLEMS.append(dict(
    title="Boats to Save People", lc_num="881", difficulty="MEDIUM", pattern="Two Pointers + Greedy",
    video_note=NO_VIDEO,
    problem="Each boat holds at most 2 people and has a weight limit. Given people's weights, find the minimum number of boats to carry everyone.",
    trigger="\"pair people/items under a limit, minimize groups\" → sort, then greedily pair heaviest with lightest.",
    clarify="Every person individually fits the limit alone? Boat can carry just 1 if pairing isn't possible?",
    brute_idea="Try many pairings and take the best (no efficient structure).",
    brute_code="""from itertools import permutations

def num_rescue_boats_brute(people, limit):
    # illustrative only -- trying arrangements directly is
    # combinatorially expensive and not a practical baseline
    return None  # see optimal; brute force here isn't meaningfully simpler""",
    brute_time="Exponential (impractical)", brute_space="O(n)",
    bottleneck="Without sorting, there's no efficient way to know which two people are the best pairing candidates.",
    optimal_insight="Sort, then two pointers: try pairing the lightest with the heaviest remaining. If they fit, both board one boat; if not, the heaviest goes alone -- it can't fit with anyone lighter either.",
    optimal_code="""def num_rescue_boats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats""",
    optimal_time="O(n log n)", optimal_space="O(1) extra",
    test="[3,2,2,1], limit=3 -> sorted [1,2,2,3]: 1+3>3 (3 alone), 1+2<=3 (pair), 2 alone -> 3 boats. Edge: everyone weighs exactly the limit -> nobody ever pairs, n boats.",
    other_edges="single person; all pairs fit perfectly (even n); odd number of people with one left over.",
    memory_hook="\"Pair the heaviest with the lightest -- if that fails, no one else fits either.\"",
))

PROBLEMS.append(dict(
    title="Minimum Size Subarray Sum", lc_num="209", difficulty="MEDIUM", pattern="Sliding Window (Variable Size)",
    video_note=NO_VIDEO,
    problem="Given positive integers and a target, find the minimal length of a contiguous subarray whose sum is >= target, or 0 if none exists.",
    trigger="\"shortest subarray with sum at least target\", all positive → Sliding Window, grow then shrink.",
    clarify="All numbers guaranteed positive? Return 0 if no valid subarray exists?",
    brute_idea="Check every subarray's sum directly.",
    brute_code="""def min_subarray_len(target, nums):
    best = float('inf')
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total >= target:
                best = min(best, j - i + 1)
                break
    return 0 if best == float('inf') else best""",
    brute_time="O(n²)", brute_space="O(1)",
    bottleneck="Recomputing sums for overlapping subarrays redoes additions already done; since all numbers are positive, a window can grow/shrink incrementally instead.",
    optimal_insight="Grow the window right, adding to a running sum. Whenever sum >= target, shrink from the left as far as possible, recording the smallest valid length.",
    optimal_code="""def min_subarray_len(target, nums):
    left = 0
    total = 0
    best = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float('inf') else best""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="target=7, [2,3,1,2,4,3] -> window shrinks/grows, smallest valid window is [4,3], length 2. Edge: target unreachable, e.g. target=100 on small numbers -> stays inf, return 0.",
    other_edges="whole array needed to reach target; single element already >= target; array of length 1.",
    memory_hook="\"Grow until it's enough, then shrink until it's not.\"",
))

PROBLEMS.append(dict(
    title="Find All Anagrams in a String", lc_num="438", difficulty="MEDIUM", pattern="Sliding Window (Fixed Size)",
    video_note=NO_VIDEO,
    problem="Given strings s and p, find all starting indices in s where a substring is an anagram of p.",
    trigger="\"find all anagram substrings\" → fixed-size sliding window + character count comparison.",
    clarify="Lowercase English letters only? Overlapping matches should all count?",
    brute_idea="For every start index, sort a same-length window and compare to sorted p.",
    brute_code="""def find_anagrams(s, p):
    result = []
    k = len(p)
    target = sorted(p)
    for i in range(len(s) - k + 1):
        if sorted(s[i:i+k]) == target:
            result.append(i)
    return result""",
    brute_time="O(n * k log k)", brute_space="O(k)",
    bottleneck="Re-sorting a whole new window at every position redoes work that overlaps almost entirely with the previous window.",
    optimal_insight="Track a 26-length running count for the window; add the incoming char, remove the outgoing char, compare to p's count array in O(1)-ish per slide.",
    optimal_code="""def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    need = [0]*26
    window = [0]*26
    for ch in p:
        need[ord(ch)-97] += 1
    result = []
    for i in range(len(s)):
        window[ord(s[i])-97] += 1
        if i >= len(p):
            window[ord(s[i-len(p)])-97] -= 1
        if i >= len(p)-1 and window == need:
            result.append(i - len(p) + 1)
    return result""",
    optimal_time="O(n)", optimal_space="O(1) (26 slots)",
    test="s='cbaebabacd', p='abc' -> matches at indices 0 and 6. Edge: p longer than s -> early return [].",
    other_edges="s equals p; no anagram exists anywhere; p has repeated letters.",
    memory_hook="\"Same letter counts, sliding window, add one / remove one.\"",
))

PROBLEMS.append(dict(
    title="Next Greater Element I", lc_num="496", difficulty="EASY", pattern="Monotonic Stack",
    video_note=NO_VIDEO,
    problem="nums1 is a subset of nums2; for each value in nums1, find its next greater element to the right in nums2, or -1.",
    trigger="\"next greater element to the right\", repeated queries → Monotonic Stack precomputes all answers in one pass.",
    clarify="Every nums1 value guaranteed to exist in nums2? Duplicates possible in nums2?",
    brute_idea="For each query value, find it in nums2 and scan forward for something bigger.",
    brute_code="""def next_greater_element(nums1, nums2):
    result = []
    for x in nums1:
        idx = nums2.index(x)
        found = -1
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > x:
                found = nums2[j]
                break
        result.append(found)
    return result""",
    brute_time="O(n * m)", brute_space="O(1) extra",
    bottleneck="Re-scanning nums2 for every query redoes work; the 'next greater' for every value in nums2 can be precomputed once.",
    optimal_insight="One pass over nums2 with a decreasing stack: when a bigger number appears, it resolves every smaller value still waiting on the stack.",
    optimal_code="""def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(x, -1) for x in nums1]""",
    optimal_time="O(n + m)", optimal_space="O(n)",
    test="nums2=[2,1,2,4,3] -> map builds {1:2, 2:4}. nums1=[2,4] -> [4,-1] (4 never resolves). Edge: largest value at the very end -> never popped, defaults to -1.",
    other_edges="strictly decreasing nums2 (all -1); nums1 equals nums2; single-element nums2.",
    memory_hook="\"Stack holds the unresolved; a bigger number resolves everyone smaller beneath it.\"",
))

PROBLEMS.append(dict(
    title="Decode String", lc_num="394", difficulty="MEDIUM", pattern="Stack",
    video_note=NO_VIDEO,
    problem="Decode a string with pattern k[encoded], meaning encoded repeats k times, with possible nesting, e.g. '3[a2[c]]'.",
    trigger="\"nested k[string] encoding\" → Stack to pause/resume the string being built at each bracket level.",
    clarify="Can nesting go arbitrarily deep? Are repeat counts always positive, possibly multi-digit?",
    brute_idea="Repeatedly expand the innermost k[...] with string replace until no brackets remain.",
    brute_code="""import re

def decode_string_brute(s):
    while '[' in s:
        s = re.sub(r'(\\d+)\\[([a-z]*)\\]',
                    lambda m: m.group(2) * int(m.group(1)), s)
    return s  # needs innermost-first matching; fragile for deep nesting""",
    brute_time="O(n²) or worse", brute_space="O(n)",
    bottleneck="Repeated whole-string expansion rebuilds and rescans the string at every nesting level instead of handling nesting directly in one pass.",
    optimal_insight="A stack pauses the current (string, count) when '[' is seen, and resumes/combines it when ']' closes that level.",
    optimal_code="""def decode_string(s):
    stack = []
    current_str = ''
    current_num = 0
    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            stack.append((current_str, current_num))
            current_str, current_num = '', 0
        elif ch == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += ch
    return current_str""",
    optimal_time="O(n * maxK)", optimal_space="O(n)",
    test="'3[a2[c]]' -> inner resolves to 'acc', outer to 'accaccacc'. Edge: no brackets at all, e.g. 'abc' -> passes through unchanged.",
    other_edges="multiple sibling groups, e.g. '2[a]3[b]'; multi-digit counts like '213[a]'; deeply nested brackets.",
    memory_hook="\"Bracket opens: pause and push. Bracket closes: pop and combine.\"",
))

PROBLEMS.append(dict(
    title="Simplify Path", lc_num="71", difficulty="MEDIUM", pattern="Stack",
    video_note=NO_VIDEO,
    problem="Given a Unix-style absolute path, simplify it into canonical form, resolving '.', '..', and collapsing repeated slashes.",
    trigger="\"simplify a Unix path\" → split on '/', treat directory names as a Stack (push names, pop on '..').",
    clarify="What happens if '..' would go above the root? Trailing slashes need removing?",
    brute_idea="Directly manipulate the raw string, searching backward for the previous slash on every '..'.",
    brute_code="""def simplify_path_brute(path):
    # repeatedly find '..' and remove it plus the preceding
    # component via string search/slicing -- fragile, O(n^2)
    # in the worst case; not shown in full, see optimal instead
    return None""",
    brute_time="O(n²)", brute_space="O(n)",
    bottleneck="Raw string surgery for 'go up a directory' is fragile and repeats backward scans; directory names naturally behave like a stack.",
    optimal_insight="Split on '/'. Skip empty/'.' pieces, pop on '..' (if non-empty), push real names. Join what remains.",
    optimal_code="""def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)""",
    optimal_time="O(n)", optimal_space="O(n)",
    test="'/a/./b/../../c/' -> a,b push then both pop via the two '..', c pushes -> '/c'. Edge: '..' at the root, e.g. '/../' -> pop guarded, stays at '/'.",
    other_edges="repeated slashes, e.g. '/a//b'; already-canonical path; path of only '.' components.",
    memory_hook="\"Split by slash; real names push, '..' pops, '.' does nothing.\"",
))

PROBLEMS.append(dict(
    title="Find K Closest Elements", lc_num="658", difficulty="MEDIUM", pattern="Binary Search",
    video_note=NO_VIDEO,
    problem="Given a sorted array, a target x, and integer k, return the k closest values to x, sorted ascending.",
    trigger="\"k closest values in a sorted array\" → the answer is a contiguous window; binary search for where it starts.",
    clarify="Ties broken toward the smaller value? Output must stay sorted ascending?",
    brute_idea="Sort all elements by distance to x, take the first k, then re-sort those by value.",
    brute_code="""def find_closest_elements(arr, k, x):
    arr2 = sorted(arr, key=lambda v: abs(v - x))
    return sorted(arr2[:k])""",
    brute_time="O(n log n)", brute_space="O(n)",
    bottleneck="Sorting the whole array by distance does far more work than needed -- the array's already sorted, so the answer is one contiguous window.",
    optimal_insight="Binary search for the window's left boundary: compare the element just before the window to the element just past it, and shift toward whichever is closer to x.",
    optimal_code="""def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]""",
    optimal_time="O(log(n-k) + k)", optimal_space="O(k)",
    test="[1,2,3,4,5], k=4, x=3 -> search settles on start=0 -> [1,2,3,4]. Edge: k equals array length -> search range collapses to one point, returns everything.",
    other_edges="x smaller than every element; x larger than every element; k=1.",
    memory_hook="\"Sorted array means the answer is one window -- binary search for where it starts.\"",
))

PROBLEMS.append(dict(
    title="Split Array Largest Sum", lc_num="410", difficulty="HARD", pattern="Binary Search on the Answer",
    video_note=NO_VIDEO,
    problem="Split an array into m contiguous subarrays to minimize the largest subarray sum; return that minimized value.",
    trigger="\"minimize the maximum / split into m parts\" → Binary Search on the answer + a greedy feasibility check.",
    clarify="All numbers non-negative? Need the actual split, or just the minimized value?",
    brute_idea="Try every placement of m-1 dividers and evaluate the resulting max subarray sum.",
    brute_code="""from itertools import combinations

def split_array_brute(nums, m):
    n = len(nums)
    best = float('inf')
    for cuts in combinations(range(1, n), m - 1):
        parts, prev = [], 0
        for c in cuts:
            parts.append(sum(nums[prev:c])); prev = c
        parts.append(sum(nums[prev:]))
        best = min(best, max(parts))
    return best  # combinatorial, impractical for larger n""",
    brute_time="Exponential", brute_space="O(m)",
    bottleneck="Exploring every split configuration directly is combinatorial; instead, binary search over candidate ANSWER values and check feasibility.",
    optimal_insight="Binary search the answer between max(nums) and sum(nums). For a candidate cap, greedily count subarrays needed to keep every part <= cap; feasible if count <= m.",
    optimal_code="""def split_array(nums, m):
    def subarrays_needed(cap):
        count, cur = 1, 0
        for num in nums:
            if cur + num > cap:
                count += 1
                cur = num
            else:
                cur += num
        return count

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if subarrays_needed(mid) <= m:
            right = mid
        else:
            left = mid + 1
    return left""",
    optimal_time="O(n log(sum-max))", optimal_space="O(1)",
    test="[7,2,5,10,8], m=2 -> binary search converges to 18 ([7,2,5] and [10,8]). Edge: m equals array length -> answer is just the largest single element.",
    other_edges="m=1 (answer is the total sum); all elements identical; one very large element dominating.",
    memory_hook="\"Binary search the answer; greedily count subarrays to test feasibility.\"",
))

PROBLEMS.append(dict(
    title="Pow(x, n)", lc_num="50", difficulty="MEDIUM", pattern="Fast Exponentiation (Divide & Conquer)",
    video_note=NO_VIDEO,
    problem="Implement pow(x, n) for integer n, which can be negative, efficiently.",
    trigger="\"compute x to the power n\" → halve the exponent and square the result (fast/binary exponentiation).",
    clarify="Can n be negative (return reciprocal)? n=0 always gives 1?",
    brute_idea="Multiply x by itself n times in a loop.",
    brute_code="""def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    for _ in range(n):
        result *= x
    return result""",
    brute_time="O(n)", brute_space="O(1)",
    bottleneck="Adding one factor of x at a time does far more multiplications than necessary -- repeated squaring covers exponentially more ground per step.",
    optimal_insight="x^n = (x^(n//2))^2, with one extra factor of x if n is odd. Recursing halves the exponent every step -- logarithmic multiplications instead of linear.",
    optimal_code="""def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    def fast_pow(base, exp):
        if exp == 0:
            return 1
        half = fast_pow(base, exp // 2)
        return half * half if exp % 2 == 0 else half * half * base
    return fast_pow(x, n)""",
    optimal_time="O(log n)", optimal_space="O(log n) recursion",
    test="2^10 -> halves 10,5,2,1,0, squaring back up gives 1024. Edge: negative exponent, e.g. 2^-2 -> flip to 0.5^2 = 0.25.",
    other_edges="n=0 (always 1); x=0 with positive n; x=1 or x=-1.",
    memory_hook="\"Halve the exponent, square the result -- add one extra factor if odd.\"",
))

PROBLEMS.append(dict(
    title="Add Two Numbers", lc_num="2", difficulty="MEDIUM", pattern="Linked List Traversal + Carry",
    video_note=NO_VIDEO,
    problem="Two linked lists represent non-negative integers with digits in reverse order; add them and return the sum as a linked list in the same format.",
    trigger="\"linked list digits in reverse, add two numbers\" → simulate elementary addition digit by digit with a carry.",
    clarify="Digits stored least-significant-first, so add directly from the heads? Lists can differ in length?",
    brute_idea="Convert both lists to integers, add, convert back (works in Python; not general/robust).",
    brute_code="""def add_two_numbers_brute(l1, l2):
    def to_int(l):
        num, mult = 0, 1
        while l:
            num += l.val * mult
            mult *= 10
            l = l.next
        return num
    total = to_int(l1) + to_int(l2)
    dummy = cur = ListNode()
    if total == 0:
        return ListNode(0)
    while total:
        cur.next = ListNode(total % 10)
        cur = cur.next
        total //= 10
    return dummy.next""",
    brute_time="O(n+m)", brute_space="O(n+m)",
    bottleneck="Works in Python (big ints), but sidesteps the intended digit-by-digit simulation and isn't safe in languages with fixed-size integers.",
    optimal_insight="Walk both lists together, summing digits plus carry, creating a new node for (sum mod 10) and carrying (sum // 10) forward.",
    optimal_code="""def add_two_numbers(l1, l2):
    dummy = cur = ListNode()
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        cur.next = ListNode(total % 10)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next""",
    optimal_time="O(max(n,m))", optimal_space="O(max(n,m))",
    test="2->4->3 (342) + 5->6->4 (465) -> 7->0->8 (807). Edge: leftover carry after both lists end, e.g. 99+1 -> loop continues once more for the extra digit, giving 100.",
    other_edges="both lists represent 0; very different lengths; sum needs a new leading digit.",
    memory_hook="\"Add node by node, carry the tens digit forward, just like paper addition.\"",
))

PROBLEMS.append(dict(
    title="Linked List Cycle", lc_num="141", difficulty="EASY", pattern="Fast & Slow Pointers",
    video_note=NO_VIDEO,
    problem="Given the head of a linked list, determine whether it contains a cycle.",
    trigger="\"does the list loop back on itself\", O(1) space → Floyd's Tortoise and Hare.",
    clarify="Just true/false needed, not the cycle's start node? Single node can point to itself?",
    brute_idea="Hash set of visited nodes; a repeat means a cycle.",
    brute_code="""def has_cycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="Remembering every visited node costs O(n) memory when two pointers at different speeds can detect a loop with none.",
    optimal_insight="Slow moves 1 step, fast moves 2. If there's a cycle, fast eventually laps slow and they meet; if not, fast hits null first.",
    optimal_code="""def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="A list that loops back into itself -- slow and fast meet after a few steps. Edge: no cycle, e.g. 1->2->3->None -> fast hits null, returns False.",
    other_edges="empty list; single node with no self-loop; single node pointing to itself.",
    memory_hook="\"Two runners on a track -- if there's a loop, the fast one always laps the slow one.\"",
))

PROBLEMS.append(dict(
    title="Intersection of Two Linked Lists", lc_num="160", difficulty="EASY", pattern="Two Pointers",
    video_note=NO_VIDEO,
    problem="Given the heads of two singly linked lists, find the node where they intersect (share the same tail), or null.",
    trigger="\"find where two linked lists merge\" → Two Pointers that switch to the other list's head when they run out.",
    clarify="Intersection means same node by reference, not just equal value? Lists can differ in length before merging?",
    brute_idea="For every node in A, scan all of B for a reference match.",
    brute_code="""def get_intersection_node(headA, headB):
    a = headA
    while a:
        b = headB
        while b:
            if a is b:
                return a
            b = b.next
        a = a.next
    return None""",
    brute_time="O(n * m)", brute_space="O(1)",
    bottleneck="Rescanning list B for every node in A redoes the same comparisons; aligning both lists' remaining lengths lets one synchronized pass work instead.",
    optimal_insight="Two pointers, one per list; each switches to the OTHER list's head when it hits null. This equalizes total distance traveled, so they meet at the intersection (or both hit null together).",
    optimal_code="""def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a""",
    optimal_time="O(n + m)", optimal_space="O(1)",
    test="A length 5, B length 6, sharing a tail -- both pointers converge on the shared node after each switches once. Edge: no intersection at all -- both become null on the same step.",
    other_edges="one list is empty; intersection at the very first node (identical lists); intersection at the very last node only.",
    memory_hook="\"When you hit your own end, switch to the other list -- you'll meet at the join.\"",
))

PROBLEMS.append(dict(
    title="Copy List with Random Pointer", lc_num="138", difficulty="MEDIUM", pattern="Hash Map (Clone Mapping)",
    video_note=NO_VIDEO,
    problem="Each node has 'next' and 'random' pointers (random can point anywhere or null); deep-copy the entire list.",
    trigger="\"deep copy with arbitrary cross-references\" → Hash Map from original node to its clone.",
    clarify="Random pointer can point to any node including itself, or null? Need a fully independent deep copy?",
    brute_idea="There's no simpler correct shortcut -- you need SOME lookup from original to clone; the two-pass hash map approach below is already the standard baseline.",
    brute_code="""# A single naive pass trying to wire pointers immediately
# breaks when random points to a node not yet cloned --
# there's no meaningfully 'slower but simpler' alternative
# here; go straight to the two-pass hash map solution.""",
    brute_time="N/A", brute_space="N/A",
    bottleneck="Wiring pointers in one pass fails whenever random points to a node not yet cloned -- need every node cloned first, then a second pass to wire.",
    optimal_insight="Pass 1: create a copy of every node's value, store original->copy in a map. Pass 2: use the map to set each copy's next/random.",
    optimal_code="""def copy_random_list(head):
    if not head:
        return None
    old_to_new = {}
    node = head
    while node:
        old_to_new[node] = Node(node.val)
        node = node.next
    node = head
    while node:
        copy = old_to_new[node]
        copy.next = old_to_new.get(node.next)
        copy.random = old_to_new.get(node.random)
        node = node.next
    return old_to_new[head]""",
    optimal_time="O(n)", optimal_space="O(n)",
    test="A(random->C), B(random->A), C(random->C) -> clones rewired identically via the map. Edge: a node's random points to itself -- map resolves it to its own clone correctly.",
    other_edges="empty list; single node with random=null; every random pointer set to null.",
    memory_hook="\"Map every original to its copy first, then rewire using the map.\"",
))

PROBLEMS.append(dict(
    title="Same Tree", lc_num="100", difficulty="EASY", pattern="DFS Recursion",
    video_note=NO_VIDEO,
    problem="Given the roots of two binary trees, determine whether they're structurally identical with the same node values.",
    trigger="\"are these two trees identical\" → simultaneous DFS recursion on both trees.",
    clarify="Same means identical structure AND identical values everywhere? Either tree could be empty?",
    brute_idea="Serialize both trees (with null markers) and compare the serialized strings.",
    brute_code="""def is_same_tree_brute(p, q):
    def serialize(node):
        if not node:
            return '#'
        return f'{node.val},{serialize(node.left)},{serialize(node.right)}'
    return serialize(p) == serialize(q)""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="Building full serialized strings is extra work when the two trees can be compared directly node by node with early exit on any mismatch.",
    optimal_insight="Compare roots: both null matches, one null mismatches, otherwise compare values and recurse into both children.",
    optimal_code="""def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)""",
    optimal_time="O(min(n,m))", optimal_space="O(min(h1,h2))",
    test="Two identical trees, root 1 with children 2,3 -> True. Edge: one tree has an extra node the other lacks -- null-vs-non-null check catches it, False.",
    other_edges="both trees empty; identical structure but one differing value; single-node trees.",
    memory_hook="\"Match the roots, then recursively match both subtree pairs.\"",
))

PROBLEMS.append(dict(
    title="Validate Binary Search Tree", lc_num="98", difficulty="MEDIUM", pattern="DFS with Valid Range",
    video_note=NO_VIDEO,
    problem="Determine whether a binary tree is a valid BST (every node strictly between its ancestors' bounds).",
    trigger="\"validate a BST\" → pass down a shrinking (low, high) valid range, not just check immediate parent/child.",
    clarify="Duplicate values allowed? Compare against ALL ancestors, not just the immediate parent?",
    brute_idea="Naive (and WRONG) shortcut: only check each node against its immediate children.",
    brute_code="""def is_valid_bst_wrong(node):
    if not node:
        return True
    if node.left and node.left.val >= node.val:
        return False
    if node.right and node.right.val <= node.val:
        return False
    return (is_valid_bst_wrong(node.left) and
            is_valid_bst_wrong(node.right))
    # BUG: misses violations from non-immediate ancestors!""",
    brute_time="O(n) but INCORRECT", brute_space="O(h)",
    bottleneck="Checking only immediate parent-child pairs misses violations from grandparents or higher ancestors -- the BST property constrains a WHOLE subtree, not just one edge.",
    optimal_insight="Pass down a valid (low, high) range. Going left tightens the upper bound to the current value; going right tightens the lower bound.",
    optimal_code="""def is_valid_bst(root):
    def validate(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    return validate(root, float('-inf'), float('inf'))""",
    optimal_time="O(n)", optimal_space="O(h)",
    test="5 with left 3 (right child 6) -> 6 violates 5's left-subtree upper bound even though it's > its direct parent 3. Edge: duplicate value, e.g. node equal to parent -- strict inequality rejects it.",
    other_edges="empty tree (valid); single node; deeply skewed valid BST.",
    memory_hook="\"Every node lives inside a shrinking range passed down from its ancestors.\"",
))

PROBLEMS.append(dict(
    title="Kth Smallest Element in a BST", lc_num="230", difficulty="MEDIUM", pattern="In-order Traversal",
    video_note=NO_VIDEO,
    problem="Given a BST and integer k, find the kth smallest value in the tree.",
    trigger="\"kth smallest in a BST\" → in-order traversal visits BST values in sorted order; stop counting at k.",
    clarify="k guaranteed valid (1..node count)? All values unique?",
    brute_idea="Full in-order traversal collecting every value, then index k-1.",
    brute_code="""def kth_smallest_brute(root, k):
    values = []
    def inorder(node):
        if node:
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
    inorder(root)
    return values[k - 1]""",
    brute_time="O(n)", brute_space="O(n)",
    bottleneck="Collecting every value even when k is small does unnecessary work and uses unnecessary memory past the kth value.",
    optimal_insight="Iterative in-order traversal with an explicit stack; stop the instant the kth node is popped, instead of visiting the whole tree.",
    optimal_code="""def kth_smallest(root, k):
    stack = []
    node = root
    count = 0
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right""",
    optimal_time="O(h + k)", optimal_space="O(h)",
    test="root=3, left=1(right=2), right=4, k=1 -> walks left to 1, returns immediately. Edge: k = total node count -> must traverse entire tree, returns the max.",
    other_edges="single-node tree with k=1; fully left/right-skewed tree; k in the middle of a balanced tree.",
    memory_hook="\"In-order traversal is sorted order -- just stop counting at k.\"",
))

PROBLEMS.append(dict(
    title="Construct Binary Tree from Preorder and Inorder Traversal", lc_num="105", difficulty="MEDIUM", pattern="Recursion + Hash Map",
    video_note=NO_VIDEO,
    problem="Given preorder and inorder traversal arrays of a tree with unique values, reconstruct and return the tree.",
    trigger="\"rebuild a tree from two traversals\" → preorder's first value is the root; find it in inorder to split left/right.",
    clarify="All node values guaranteed unique? Both arrays same length, valid traversals of the same tree?",
    brute_idea="Same recursive idea, but linear-search inorder for each root's split point every call.",
    brute_code="""def build_tree_brute(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)  # O(n) search every call
    root.left = build_tree_brute(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_brute(preorder[mid+1:], inorder[mid+1:])
    return root""",
    brute_time="O(n²)", brute_space="O(n)",
    bottleneck="Searching inorder from scratch at every recursive call redoes lookups; precomputing all positions once removes that repeated search.",
    optimal_insight="Precompute value->index in inorder (O(1) lookup). Track a running preorder pointer; build left subtree first (consumes exactly its share of preorder), then right.",
    optimal_code="""def build_tree(preorder, inorder):
    inorder_index = {val: i for i, val in enumerate(inorder)}
    self_idx = 0
    def build(left, right):
        nonlocal self_idx
        if left > right:
            return None
        root_val = preorder[self_idx]
        self_idx += 1
        root = TreeNode(root_val)
        mid = inorder_index[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    return build(0, len(inorder) - 1)""",
    optimal_time="O(n)", optimal_space="O(n)",
    test="preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] -> root 3, left 9, right 20(left 15, right 7). Edge: empty arrays -> initial range invalid, returns None.",
    other_edges="single-node tree; completely left-skewed tree; completely right-skewed tree.",
    memory_hook="\"Preorder's first value is root; inorder's position of that value splits left from right.\"",
))

PROBLEMS.append(dict(
    title="Serialize and Deserialize Binary Tree", lc_num="297", difficulty="HARD", pattern="DFS Preorder + Null Markers",
    video_note=NO_VIDEO,
    problem="Design an algorithm to serialize a binary tree to a string and deserialize it back to the original tree.",
    trigger="\"serialize/deserialize a tree\" → preorder DFS with explicit null markers makes it unambiguous to rebuild.",
    clarify="Any string format acceptable as long as it round-trips exactly? Values could contain the delimiter?",
    brute_idea="A traversal that OMITS null markers loses structural information and can't be reliably reversed.",
    brute_code="""def serialize_lossy(root):
    values = []
    def dfs(node):
        if node:
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return ','.join(values)  # ambiguous: can't tell where children are missing""",
    brute_time="O(n) but lossy", brute_space="O(n)",
    bottleneck="Without null markers, different tree shapes can produce the identical serialized sequence -- deserialization becomes ambiguous or impossible.",
    optimal_insight="Preorder DFS, writing '#' for every null child. Deserialize by reading tokens in the same preorder order with an iterator.",
    optimal_code="""def serialize(root):
    vals = []
    def dfs(node):
        if node is None:
            vals.append('#')
            return
        vals.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ','.join(vals)

def deserialize(data):
    vals = iter(data.split(','))
    def build():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    return build()""",
    optimal_time="O(n)", optimal_space="O(n)",
    test="root=1,left=2,right=3(left=4,right=5) -> '1,2,#,#,3,4,#,#,5,#,#' round-trips exactly. Edge: empty tree -> serializes to just '#', deserializes to None.",
    other_edges="single-node tree; fully left-skewed tree; values with multiple digits or negative signs.",
    memory_hook="\"Preorder plus explicit nulls -- nothing is ambiguous.\"",
))

PROBLEMS.append(dict(
    title="Balanced Binary Tree", lc_num="110", difficulty="EASY", pattern="Bottom-Up DFS",
    video_note=NO_VIDEO,
    problem="Determine whether a binary tree is height-balanced: for every node, its left/right subtree heights differ by at most 1.",
    trigger="\"height-balanced tree\" → compute height and check balance in ONE bottom-up pass, using a sentinel for 'already unbalanced'.",
    clarify="Balance must hold at EVERY node, not just the root? Empty tree counts as balanced?",
    brute_idea="At every node, independently recompute the height of its left and right subtrees from scratch.",
    brute_code="""def is_balanced_brute(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced_brute(root.left) and is_balanced_brute(root.right)""",
    brute_time="O(n²)", brute_space="O(h)",
    bottleneck="Recomputing height from scratch at every node re-walks overlapping subtrees repeatedly.",
    optimal_insight="One recursive pass returns real height, or a sentinel -1 the moment any subtree below is already unbalanced, short-circuiting further checks.",
    optimal_code="""def is_balanced(root):
    def check(node):
        if node is None:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check(root) != -1""",
    optimal_time="O(n)", optimal_space="O(h)",
    test="root=3, left=9, right=20(15,7) -> every level within 1, height 3, balanced. Edge: imbalance buried deep -- the -1 sentinel bubbles all the way up correctly.",
    other_edges="empty tree; single node; imbalance right at the root.",
    memory_hook="\"Compute height and check balance together; -1 means 'already broken, stop caring'.\"",
))

PROBLEMS.append(dict(
    title="Subtree of Another Tree", lc_num="572", difficulty="EASY", pattern="DFS Tree Matching",
    video_note=NO_VIDEO,
    problem="Given roots of two trees, determine whether subRoot exactly matches some subtree of root.",
    trigger="\"is this tree a subtree of another\" → reuse Same-Tree equality, but try it at EVERY node of root.",
    clarify="Whole subtree at the matching node must match exactly, including all descendants?",
    brute_idea="Same idea as optimal but naively re-derives same-tree logic inline every call without reuse -- functionally identical, just less clean.",
    brute_code="""def is_subtree_brute(root, sub_root):
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)
    if not root:
        return False
    if same(root, sub_root):
        return True
    return (is_subtree_brute(root.left, sub_root) or
            is_subtree_brute(root.right, sub_root))
    # This IS roughly the optimal approach -- there is no
    # meaningfully slower correct baseline beyond this shape.""",
    brute_time="O(n * m)", brute_space="O(h1+h2)",
    bottleneck="This problem doesn't have a deeper asymptotic shortcut for typical interview scope; the win is writing the same-tree check cleanly and trying it at every node.",
    optimal_insight="Reuse a same-tree helper; call it at every node of root, recursing into children if the current node doesn't match.",
    optimal_code="""def is_same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None or a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

def is_subtree(root, sub_root):
    if root is None:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)""",
    optimal_time="O(n * m)", optimal_space="O(h1+h2)",
    test="root=3(left=4(1,2), right=5), subRoot=4(1,2) -> root doesn't match, left child does -> True. Edge: matching value but different subtree shape -- same-tree check rejects it, correctly keeps searching.",
    other_edges="subRoot is a single leaf; root equals subRoot exactly; subRoot never appears (False).",
    memory_hook="\"Try an exact match at every node -- reuse Same Tree as the check.\"",
))

PROBLEMS.append(dict(
    title="Walls and Gates", lc_num="286", difficulty="MEDIUM", pattern="Multi-Source BFS",
    video_note=NO_VIDEO,
    problem="Fill each empty room in a grid with its distance to the nearest gate (0); walls (-1) unchanged.",
    trigger="\"distance to the nearest of several sources\" → Multi-Source BFS, seed the queue with ALL sources at once.",
    clarify="4-directional movement only? Multiple gates possible? Modify the grid in place?",
    brute_idea="Run a separate BFS from every empty room out to find its nearest gate.",
    brute_code="""from collections import deque

def walls_and_gates_brute(rooms):
    rows, cols = len(rooms), len(rooms[0])
    def bfs_from(sr, sc):
        visited = {(sr, sc)}
        q = deque([(sr, sc, 0)])
        while q:
            r, c, d = q.popleft()
            if rooms[r][c] == 0 and (r, c) != (sr, sc):
                return d
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and rooms[nr][nc] != -1:
                    visited.add((nr,nc)); q.append((nr,nc,d+1))
        return rooms[sr][sc]
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] not in (0, -1):
                rooms[r][c] = bfs_from(r, c)""",
    brute_time="O((rows*cols)²)", brute_space="O(rows*cols)",
    bottleneck="A full grid-sized BFS from every room redoes overlapping searches; starting from all gates at once visits every cell only once total.",
    optimal_insight="Seed the BFS queue with every gate simultaneously. BFS explores in increasing distance order, so the first time a room is reached is via its true nearest gate.",
    optimal_code="""from collections import deque

def walls_and_gates(rooms):
    rows, cols = len(rooms), len(rooms[0])
    queue = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == 2147483647:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))""",
    optimal_time="O(rows*cols)", optimal_space="O(rows*cols)",
    test="Grid with 2 gates -> BFS expands outward from both simultaneously, filling correct distances. Edge: a room walled off from every gate -- never reached, stays at the sentinel (unreachable).",
    other_edges="single gate; no gates at all (everything stays sentinel); grid that's entirely walls except one gate.",
    memory_hook="\"Start BFS from every gate at once -- first arrival is always the nearest.\"",
))

PROBLEMS.append(dict(
    title="Kth Largest Element in a Stream", lc_num="703", difficulty="EASY", pattern="Heap (size-k min-heap)",
    video_note=NO_VIDEO,
    problem="Design a class that supports adding numbers to a stream and always returning the kth largest so far.",
    trigger="\"kth largest in a stream, repeated queries\" → maintain a min-heap capped at size k.",
    clarify="k stays fixed for the object's lifetime? 'add' called many times, so must be efficient per call?",
    brute_idea="Store every number in a list; each add, re-sort and pick the kth from the end.",
    brute_code="""class KthLargestBrute:
    def __init__(self, k, nums):
        self.k = k
        self.nums = list(nums)
    def add(self, val):
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]""",
    brute_time="O(n log n) per add", brute_space="O(n)",
    bottleneck="Re-sorting the entire history on every call redoes work; only the top k values ever matter, not the full history's order.",
    optimal_insight="Keep a min-heap of exactly the k largest values seen. The heap's top (smallest of the top-k) is always the answer; push and pop only when a new value beats it.",
    optimal_code="""import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]""",
    optimal_time="O(log k) per add", optimal_space="O(k)",
    test="k=3, add 4,5,8,2 -> heap settles on {4,5,8}, kth largest=4. Edge: adding a value smaller than the current min of a full heap -- ignored, heap unchanged.",
    other_edges="k=1 (track just the max); duplicate values; initial nums array is empty.",
    memory_hook="\"Min-heap of size k; the top of the heap IS the kth largest.\"",
))

PROBLEMS.append(dict(
    title="Jump Game", lc_num="55", difficulty="MEDIUM", pattern="Greedy",
    video_note=NO_VIDEO,
    problem="Given max jump lengths per index starting at 0, determine if you can reach the last index.",
    trigger="\"can you reach the end, max jump per position\" → Greedy: track the single furthest reachable index.",
    clarify="Jump lengths can be 0 (potential trap)? Just yes/no needed, not the actual path?",
    brute_idea="Recursively try every possible jump length from each position.",
    brute_code="""def can_jump_brute(nums):
    def dfs(i):
        if i >= len(nums) - 1:
            return True
        for step in range(1, nums[i] + 1):
            if dfs(i + step):
                return True
        return False
    return dfs(0)""",
    brute_time="O(2^n)", brute_space="O(n)",
    bottleneck="Exploring every specific jump path is unnecessary -- only the single furthest reachable index matters, not which exact route got there.",
    optimal_insight="Scan left to right tracking furthest reachable. If the current index is beyond that, you're stuck; otherwise update furthest = max(furthest, i + nums[i]).",
    optimal_code="""def can_jump(nums):
    furthest = 0
    for i in range(len(nums)):
        if i > furthest:
            return False
        furthest = max(furthest, i + nums[i])
    return True""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="[2,3,1,1,4] -> furthest grows to cover index 4, True. Edge: a trapping 0, e.g. [3,2,1,0,4] -> furthest stalls at 3, index 4 unreachable, False.",
    other_edges="single-element array (trivially True); array starting with 0 (only True if length 1); long stretch of zeros.",
    memory_hook="\"Track the furthest you could ever reach -- forget the actual path.\"",
))

PROBLEMS.append(dict(
    title="Task Scheduler", lc_num="621", difficulty="MEDIUM", pattern="Greedy + Math",
    video_note=NO_VIDEO,
    problem="Given tasks and a cooldown n between repeats of the same task, find the minimum total time (with idle slots) to finish all tasks.",
    trigger="\"cooldown between repeated tasks\" → the most frequent task sets the schedule's minimum shape; a formula beats simulating minute by minute.",
    clarify="Only the SAME task needs the cooldown gap? Idle time counts toward the returned total?",
    brute_idea="Simulate minute by minute with a max-heap, always picking the most frequent available task.",
    brute_code="""import heapq
from collections import Counter

def least_interval_brute(tasks, n):
    counts = list(Counter(tasks).values())
    heap = [-c for c in counts]
    heapq.heapify(heap)
    time = 0
    q = []  # (available_time, count)
    while heap or q:
        time += 1
        if heap:
            c = heapq.heappop(heap) + 1
            if c < 0:
                q.append((time + n, c))
        if q and q[0][0] == time:
            heapq.heappush(heap, q.pop(0)[1])
    return time""",
    brute_time="O(t log 26)", brute_space="O(1)",
    bottleneck="Simulating every single minute works but is more computation than necessary; the schedule's length is fully determined by counting, not simulating.",
    optimal_insight="Let max_freq be the highest count and max_count how many tasks tie for it. Schedule = (max_freq-1) full (n+1)-wide chunks + a final chunk of max_count tasks -- unless enough OTHER tasks fill every gap, in which case the answer is just len(tasks).",
    optimal_code="""from collections import Counter

def least_interval(tasks, n):
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for c in counts.values() if c == max_freq)
    formula = (max_freq - 1) * (n + 1) + max_count
    return max(formula, len(tasks))""",
    optimal_time="O(t)", optimal_space="O(1)",
    test="A,A,A,B,B,B with n=2 -> both tie for max_freq=3, formula=(3-1)*3+2=8, matches A-B-idle-A-B-idle-A-B. Edge: n=0 (no cooldown) -> max() resolves to just len(tasks).",
    other_edges="one task type with large n (lots of idle); many distinct single-occurrence tasks (no idle needed); all tasks identical.",
    memory_hook="\"The busiest task sets the pace -- formula beats simulating minute by minute.\"",
))

PROBLEMS.append(dict(
    title="Car Pooling", lc_num="1094", difficulty="MEDIUM", pattern="Difference Array / Line Sweep",
    video_note=NO_VIDEO,
    problem="Given trips [passengers, start, end] and a car capacity, determine if all trips can be completed without exceeding capacity.",
    trigger="\"overlapping intervals with a running capacity\" → Difference Array: +passengers at start, -passengers at end, sweep with a running total.",
    clarify="Drop-off at a location frees capacity before pick-up at that same location? Locations bounded (e.g. 0-1000)?",
    brute_idea="For every location along the route, sum passengers from all currently-overlapping trips directly.",
    brute_code="""def car_pooling_brute(trips, capacity):
    max_loc = max(end for _, _, end in trips)
    for loc in range(max_loc):
        total = sum(p for p, s, e in trips if s <= loc < e)
        if total > capacity:
            return False
    return True""",
    brute_time="O(trips * max_location)", brute_space="O(1)",
    bottleneck="Recomputing the total at every single location redoes the same overlap checks; passenger count only actually changes at trip start/end points.",
    optimal_insight="Build a difference array: add passengers at start, subtract at end. Sweep once with a running sum, checking against capacity as you go.",
    optimal_code="""def car_pooling(trips, capacity):
    changes = [0] * 1001
    for passengers, start, end in trips:
        changes[start] += passengers
        changes[end] -= passengers
    current = 0
    for change in changes:
        current += change
        if current > capacity:
            return False
    return True""",
    optimal_time="O(trips + max_location)", optimal_space="O(max_location)",
    test="[[2,1,5],[3,3,7]], capacity=4 -> at location 3, both trips overlap = 5 passengers > 4, False. Edge: a drop-off and pick-up at the exact same location -- both apply at that index, correctly freeing capacity first.",
    other_edges="a single trip exactly filling capacity; non-overlapping trips; a trip with 0 passengers.",
    memory_hook="\"Add at pickup, subtract at drop-off, sweep and watch the running total.\"",
))

PROBLEMS.append(dict(
    title="Generate Parentheses", lc_num="22", difficulty="MEDIUM", pattern="Backtracking",
    video_note=NO_VIDEO,
    problem="Given n, generate all combinations of n pairs of well-formed (balanced) parentheses.",
    trigger="\"generate all valid combinations\" → Backtracking, only add ')' when it wouldn't unbalance the partial string.",
    clarify="Order of the output doesn't matter? n guaranteed small (output size grows fast)?",
    brute_idea="Generate every string of length 2n, then filter for validity.",
    brute_code="""def generate_parenthesis_brute(n):
    def is_valid(s):
        bal = 0
        for ch in s:
            bal += 1 if ch == '(' else -1
            if bal < 0:
                return False
        return bal == 0
    result = []
    def gen(s):
        if len(s) == 2 * n:
            if is_valid(s):
                result.append(s)
            return
        gen(s + '(')
        gen(s + ')')
    gen('')
    return result""",
    brute_time="O(2^(2n) * n)", brute_space="O(n)",
    bottleneck="Generating and then filtering wastes huge effort on strings that are invalid from an early character -- pruning invalid choices immediately avoids that entirely.",
    optimal_insight="Only add '(' if under n opens used; only add ')' if it wouldn't exceed the opens placed so far. Every full-length string built this way is automatically valid.",
    optimal_code="""def generate_parenthesis(n):
    result = []
    def backtrack(current, opens, closes):
        if len(current) == 2 * n:
            result.append(current)
            return
        if opens < n:
            backtrack(current + '(', opens + 1, closes)
        if closes < opens:
            backtrack(current + ')', opens, closes + 1)
    backtrack('', 0, 0)
    return result""",
    optimal_time="O(4^n / sqrt(n))", optimal_space="O(4^n / sqrt(n))",
    test="n=2 -> produces '(())' and '()()'. Edge: n=0 -> immediately returns [''] (empty string).",
    other_edges="n=1 (just '()'); verifying output count matches the nth Catalan number; ensuring no invalid string like ')(' is ever produced.",
    memory_hook="\"Only add ')' if there's an unmatched '(' waiting for it.\"",
))

PROBLEMS.append(dict(
    title="Combination Sum", lc_num="39", difficulty="MEDIUM", pattern="Backtracking",
    video_note=NO_VIDEO,
    problem="Given distinct positive candidates and a target, find all unique combinations summing to target, reusing numbers freely.",
    trigger="\"combinations summing to target, reuse allowed\" → Backtracking, forward-only index to avoid duplicate orderings.",
    clarify="Same number can be reused unlimited times? Combos with same numbers in different order count once?",
    brute_idea="Explore every sequence of chosen numbers without pruning or an ordering constraint.",
    brute_code="""def combination_sum_brute(candidates, target):
    result = []
    def dfs(path, remaining):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for c in candidates:  # no start index -> duplicates in different orders
            path.append(c)
            dfs(path, remaining - c)
            path.pop()
    dfs([], target)
    return result  # produces duplicate permutations of the same combo""",
    brute_time="Exponential w/ duplicates", brute_space="O(target/min)",
    bottleneck="Allowing any candidate at every step (not just forward) generates the same combination multiple times in different orders, wasting work and needing de-duplication.",
    optimal_insight="Only consider candidates from the current index onward (never backward); this guarantees each combination is found in exactly one canonical order.",
    optimal_code="""def combination_sum(candidates, target):
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result""",
    optimal_time="Exponential (pruned)", optimal_space="O(target/min)",
    test="[2,3,6,7], target=7 -> finds [2,2,3] and [7]. Edge: no combination reaches target, e.g. candidates=[5], target=3 -> immediately overshoots, empty result.",
    other_edges="target equals one candidate exactly; a candidate that alone exceeds target (pruned); many repetitions of the smallest candidate.",
    memory_hook="\"Only move forward through candidates; reuse allowed by staying at the same index.\"",
))

PROBLEMS.append(dict(
    title="Letter Combinations of a Phone Number", lc_num="17", difficulty="MEDIUM", pattern="Backtracking",
    video_note=NO_VIDEO,
    problem="Given a digit string (2-9), return all possible letter combinations per the phone keypad mapping.",
    trigger="\"phone keypad letter combinations\" → Backtracking, one recursive level per digit (nested loops don't generalize to variable length).",
    clarify="Standard keypad mapping? Empty input should return an empty list?",
    brute_idea="Fixed nested loops only work for a KNOWN number of digits -- doesn't generalize; would need one loop written per possible length.",
    brute_code="""def letter_combinations_fixed_3(digits):
    # Only works for exactly 3 digits -- illustrates why a
    # fixed number of nested loops doesn't generalize.
    phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
             '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = []
    for a in phone[digits[0]]:
        for b in phone[digits[1]]:
            for c in phone[digits[2]]:
                result.append(a + b + c)
    return result""",
    brute_time="O(4^n)", brute_space="O(n)",
    bottleneck="Nested loops require knowing the digit count in advance; recursion naturally handles any input length by processing one digit per level.",
    optimal_insight="Recursively try every letter for the current digit, advance to the next digit; once the combination's length matches the digit count, record it.",
    optimal_code="""def letter_combinations(digits):
    if not digits:
        return []
    phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
             '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = []
    def backtrack(i, current):
        if i == len(digits):
            result.append(current)
            return
        for ch in phone[digits[i]]:
            backtrack(i + 1, current + ch)
    backtrack(0, '')
    return result""",
    optimal_time="O(4^n * n)", optimal_space="O(n)",
    test="'23' -> pairs a,b,c with d,e,f -> 9 combos, ad through cf. Edge: empty string -> guard clause returns [] immediately.",
    other_edges="single digit; a digit mapping to 4 letters (7 or 9); repeated identical digits like '22'.",
    memory_hook="\"One recursive level per digit -- try every letter, then move to the next digit.\"",
))

PROBLEMS.append(dict(
    title="Valid Sudoku", lc_num="36", difficulty="MEDIUM", pattern="Hash Set Constraint Checking",
    video_note=NO_VIDEO,
    problem="Determine whether a 9x9 Sudoku board's current configuration is valid (no repeated digit in any row, column, or 3x3 box).",
    trigger="\"validate rows/columns/boxes have no duplicates\" → track 3 sets of hash sets, check all 3 constraints per cell in ONE pass.",
    clarify="Only checking current validity, not solvability? Empty cells always '.'",
    brute_idea="Check all rows, then all columns, then all boxes in three separate full passes.",
    brute_code="""def is_valid_sudoku_brute(board):
    def has_dup(cells):
        vals = [c for c in cells if c != '.']
        return len(vals) != len(set(vals))
    for row in board:
        if has_dup(row):
            return False
    for c in range(9):
        if has_dup([board[r][c] for r in range(9)]):
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            cells = [board[r][c] for r in range(br, br+3) for c in range(bc, bc+3)]
            if has_dup(cells):
                return False
    return True""",
    brute_time="O(1) (fixed 81 cells), 3 passes", brute_space="O(1)",
    bottleneck="Three separate full passes visit every cell three times total; all three constraints can be checked for each cell in a single pass instead.",
    optimal_insight="Keep 9 sets each for rows, columns, boxes. For each filled cell, check/add to all three relevant sets in one scan; box index = (r//3)*3 + (c//3).",
    optimal_code="""def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            b = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[b]:
                return False
            rows[r].add(val); cols[c].add(val); boxes[b].add(val)
    return True""",
    optimal_time="O(1) fixed board", optimal_space="O(1)",
    test="Digit '5' repeated in the same row -> second occurrence caught immediately. Edge: duplicate only within the same 3x3 box (different row/col) -- box index calculation catches it.",
    other_edges="completely empty board (valid); a fully correct solved board (valid); only one digit filled in anywhere.",
    memory_hook="\"One pass, three sets per cell: row, column, and box.\"",
))

PROBLEMS.append(dict(
    title="Climbing Stairs", lc_num="70", difficulty="EASY", pattern="DP (Fibonacci)",
    video_note=NO_VIDEO,
    problem="A staircase has n steps; each move climbs 1 or 2 steps. Count the distinct ways to reach the top.",
    trigger="\"count ways, each step a small fixed set of choices\" → Fibonacci-style DP, build up with rolling variables.",
    clarify="Only 1 or 2 steps per move, never more? Different orderings count as distinct ways?",
    brute_idea="Plain recursion: ways(n) = ways(n-1) + ways(n-2), no caching.",
    brute_code="""def climb_stairs_brute(n):
    if n <= 2:
        return n
    return climb_stairs_brute(n - 1) + climb_stairs_brute(n - 2)""",
    brute_time="O(2^n)", brute_space="O(n)",
    bottleneck="Recomputing the same smaller subproblems across different branches wastes exponential work; each value only needs to be computed once.",
    optimal_insight="This is exactly Fibonacci. Build up from the bottom with two rolling variables instead of full recursion or even a full array.",
    optimal_code="""def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1""",
    optimal_time="O(n)", optimal_space="O(1)",
    test="n=5 -> sequence 1,2,3,5,8 -> answer 8. Edge: n=1 -> base case returns 1 directly.",
    other_edges="n=2 (exactly 2 ways); n=0 if it occurs (edge convention); large n verifying no recursion blowup.",
    memory_hook="\"It's just Fibonacci -- today's ways is yesterday's plus the day before.\"",
))

PROBLEMS.append(dict(
    title="Perfect Squares", lc_num="279", difficulty="MEDIUM", pattern="DP (Unbounded Knapsack style)",
    video_note=NO_VIDEO,
    problem="Given n, find the minimum number of perfect squares (1,4,9,...) that sum exactly to n.",
    trigger="\"minimum number of X summing to a target, X reusable\" → DP, structurally identical to coin change.",
    clarify="Same square can be reused multiple times? Is there always a valid answer (yes, via 1's)?",
    brute_idea="Recursively try subtracting every possible square, no caching.",
    brute_code="""def num_squares_brute(n):
    if n == 0:
        return 0
    best = float('inf')
    j = 1
    while j * j <= n:
        best = min(best, 1 + num_squares_brute(n - j * j))
        j += 1
    return best""",
    brute_time="Exponential", brute_space="O(n)",
    bottleneck="Recomputing the same remainder values across different subtraction paths wastes massive redundant work.",
    optimal_insight="dp[i] = min squares summing to i. For each i, try every square j*j <= i: dp[i] = min(dp[i], dp[i-j*j] + 1), building bottom-up.",
    optimal_code="""def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]""",
    optimal_time="O(n * sqrt(n))", optimal_space="O(n)",
    test="n=12 -> dp builds up to 3 (4+4+4). Edge: n is itself a perfect square, e.g. 16 -> dp[16]=1.",
    other_edges="n=1 (trivially 1); a number needing the theoretical max of 4 squares; a prime not near any perfect square.",
    memory_hook="\"Coin change, but the coins are perfect squares.\"",
))

PROBLEMS.append(dict(
    title="Is Subsequence", lc_num="392", difficulty="EASY", pattern="Two Pointers (Greedy Matching)",
    video_note=NO_VIDEO,
    problem="Given strings s and t, determine if s is a subsequence of t (same relative order, not necessarily contiguous).",
    trigger="\"is X a subsequence of Y\" → greedily match each needed character to the earliest occurrence in the other string.",
    clarify="Characters must stay in relative order but need not be contiguous? Case-sensitive comparison?",
    brute_idea="There's no meaningfully slower correct alternative beyond generating subsequences of t, which is exponential and impractical -- the greedy scan below is already the natural approach.",
    brute_code="""def is_subsequence_brute(s, t):
    from itertools import combinations
    if not s:
        return True
    for combo in combinations(range(len(t)), len(s)):
        if all(t[combo[i]] == s[i] for i in range(len(s))):
            return True
    return False  # exponential, illustrative only""",
    brute_time="O(2^len(t))", brute_space="O(2^len(t))",
    bottleneck="Explicitly considering subsequences of t is exponential; matching greedily left to right needs only one linear pass.",
    optimal_insight="Scan t once; whenever the current character matches what s still needs next, advance s's pointer. s is a subsequence iff that pointer reaches the end.",
    optimal_code="""def is_subsequence(s, t):
    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1
    return i == len(s)""",
    optimal_time="O(len(t))", optimal_space="O(1)",
    test="s='abc', t='ahbgdc' -> matches a,b,c in order, True. Edge: s longer than t, e.g. s='abc', t='ab' -> t runs out first, False.",
    other_edges="s is empty (trivially True); s equals t; t contains all of s's letters but in the wrong order.",
    memory_hook="\"Greedily match each letter of s to the next occurrence in t.\"",
))

PROBLEMS.append(dict(
    title="Distinct Subsequences", lc_num="115", difficulty="HARD", pattern="2D DP (Counting)",
    video_note=NO_VIDEO,
    problem="Count how many distinct ways t appears as a subsequence of s (different position choices count separately).",
    trigger="\"count distinct ways one string forms a subsequence of another\" → 2D DP where a match ADDS both 'use it' and 'skip it'.",
    clarify="Different position choices spelling the same substring count as separate ways? t longer than s means 0?",
    brute_idea="Recursively try, for each character of t, every possible matching position in the rest of s.",
    brute_code="""def num_distinct_brute(s, t):
    def dfs(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        count = dfs(i + 1, j)  # skip s[i]
        if s[i] == t[j]:
            count += dfs(i + 1, j + 1)  # use s[i]
        return count
    return dfs(0, 0)""",
    brute_time="Exponential", brute_space="O(n+m)",
    bottleneck="The same (remaining s, remaining t) subproblems recur across many branches without caching.",
    optimal_insight="dp[i][j] = ways to form t[:j] using s[:i]. Always carry forward dp[i-1][j] (skip); if characters match, also add dp[i-1][j-1] (use).",
    optimal_code="""def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[m][n]""",
    optimal_time="O(m*n)", optimal_space="O(m*n)",
    test="s='rabbbit', t='rabbit' -> classic answer is 3. Edge: t longer than s, e.g. s='ab', t='abc' -> final cell stays 0.",
    other_edges="t is empty (1 way, choose nothing); s equals t (1 way); s has many repeated characters relevant to t.",
    memory_hook="\"On a match, add BOTH 'use it' and 'skip it' -- it's counting, not choosing.\"",
))

PROBLEMS.append(dict(
    title="Unique Binary Search Trees", lc_num="96", difficulty="MEDIUM", pattern="DP (Catalan Numbers)",
    video_note=NO_VIDEO,
    problem="Given n, count how many structurally unique BSTs can be formed using values 1..n.",
    trigger="\"count unique BST shapes\" → Catalan-number DP: fix a root, multiply left-count by right-count, sum over every root choice.",
    clarify="Just count distinct STRUCTURES, not enumerate/build the actual trees?",
    brute_idea="Recursively try every value as root, recursing on left/right ranges without caching by size.",
    brute_code="""def num_trees_brute(n):
    def count(lo, hi):
        if lo >= hi:
            return 1
        total = 0
        for root in range(lo, hi + 1):
            total += count(lo, root - 1) * count(root + 1, hi)
        return total
    return count(1, n)""",
    brute_time="Exponential-ish (uncached)", brute_space="O(n)",
    bottleneck="The count for a range only depends on its SIZE, not its specific values, so the same size gets recomputed repeatedly across different ranges.",
    optimal_insight="dp[i] = unique BSTs using i values in a row. For each size i, sum dp[k-1] * dp[i-k] over every root position k.",
    optimal_code="""def num_trees(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for k in range(1, i + 1):
            dp[i] += dp[k - 1] * dp[i - k]
    return dp[n]""",
    optimal_time="O(n²)", optimal_space="O(n)",
    test="n=3 -> dp builds 1,1,2,5 -> answer 5. Edge: n=0 -> dp[0]=1 base case (one empty-tree shape).",
    other_edges="n=1 (1 shape); n=2 (2 shapes); verifying the sequence matches known Catalan numbers.",
    memory_hook="\"Fix a root; multiply left-shape count by right-shape count; sum over every root choice.\"",
))

PROBLEMS.append(dict(
    title="Insert Delete GetRandom O(1)", lc_num="380", difficulty="MEDIUM", pattern="Hash Map + Array",
    video_note=NO_VIDEO,
    problem="Design a structure supporting insert, remove, and getRandom on a set of unique values, all average O(1).",
    trigger="\"O(1) insert, delete, AND random access together\" → combine a Hash Map (lookup) with an Array (random access); swap-with-last to remove in O(1).",
    clarify="All values unique (a true set)? insert/remove should return whether something actually changed?",
    brute_idea="Plain list: insert checks for duplicates and appends; remove searches for the value's position and shifts.",
    brute_code="""class RandomizedSetBrute:
    def __init__(self):
        self.values = []
    def insert(self, val):
        if val in self.values:
            return False
        self.values.append(val)
        return True
    def remove(self, val):
        if val not in self.values:
            return False
        self.values.remove(val)  # O(n) search + shift
        return True
    def get_random(self):
        import random
        return random.choice(self.values)""",
    brute_time="insert/remove O(n)", brute_space="O(n)",
    bottleneck="A list alone can't do O(1) lookup/removal by value; a hash map alone can't do O(1) random access -- need both, plus a trick to make removal O(1) too.",
    optimal_insight="Array holds values (O(1) random access); hash map holds value->index (O(1) lookup). To remove in O(1): swap the target with the array's LAST element, update the map, then pop the end.",
    optimal_code="""import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index = {}
    def insert(self, val):
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True
    def remove(self, val):
        if val not in self.index:
            return False
        i = self.index[val]
        last = self.values[-1]
        self.values[i] = last
        self.index[last] = i
        self.values.pop()
        del self.index[val]
        return True
    def get_random(self):
        return random.choice(self.values)""",
    optimal_time="O(1) average", optimal_space="O(n)",
    test="insert(1),insert(2),insert(3),remove(2) -> 3 swaps into 2's slot, map updates, last slot pops -> values=[1,3]. Edge: removing the value that's already last -- swap-with-self is harmless, still pops correctly.",
    other_edges="removing a nonexistent value (False, no change); inserting a duplicate (False); getRandom with only one element.",
    memory_hook="\"Array for random access, hash map for lookup, swap-with-last to remove.\"",
))

PROBLEMS.append(dict(
    title="Reverse Bits", lc_num="190", difficulty="EASY", pattern="Bit Manipulation",
    video_note=NO_VIDEO,
    problem="Reverse the bits of a 32-bit unsigned integer and return the resulting integer.",
    trigger="\"reverse bits of a fixed-width integer\" → shift-and-mask bit by bit, or a divide-and-conquer bit-swap trick.",
    clarify="Always exactly 32 bits, zero-padded? Output also treated as 32-bit unsigned?",
    brute_idea="Convert to a 32-character binary string, reverse the string, parse back to an integer.",
    brute_code="""def reverse_bits_brute(n):
    binary = format(n, '032b')
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)""",
    brute_time="O(1) (fixed 32 chars)", brute_space="O(1)",
    bottleneck="No real asymptotic bottleneck for a fixed 32-bit width; the point is showing direct bit manipulation with shifts/masks instead of string conversion.",
    optimal_insight="Extract the lowest bit of n, shift the result left to make room, OR the bit in, then shift n right -- 32 times builds the reversed pattern.",
    optimal_code="""def reverse_bits(n):
    result = 0
    for _ in range(32):
        bit = n & 1
        result = (result << 1) | bit
        n >>= 1
    return result""",
    optimal_time="O(1)", optimal_space="O(1)",
    test="Small 4-bit illustration: 0b1011 -> processing bit by bit gives 0b1101, the reverse. Edge: all-zero input -> stays 0 throughout.",
    other_edges="all-one input (unchanged); single set bit at the front (moves to the back); a palindromic bit pattern (unchanged).",
    memory_hook="\"Peel one bit off the front, tuck it onto the back of the result.\"",
))

PROBLEMS.append(dict(
    title="Number of 1 Bits", lc_num="191", difficulty="EASY", pattern="Bit Manipulation (Kernighan's)",
    video_note=NO_VIDEO,
    problem="Count how many bits are set to 1 in an unsigned integer's binary representation.",
    trigger="\"count set bits / Hamming weight\" → n & (n-1) clears the lowest set bit; count iterations until 0.",
    clarify="Input treated as a fixed 32-bit unsigned integer?",
    brute_idea="Check all 32 bit positions directly.",
    brute_code="""def hamming_weight_brute(n):
    count = 0
    for i in range(32):
        if (n >> i) & 1:
            count += 1
    return count""",
    brute_time="O(1) (32 fixed checks)", brute_space="O(1)",
    bottleneck="Checking every position even when many are 0 does more work than needed; a trick can skip straight from one set bit to the next.",
    optimal_insight="n & (n-1) always clears the lowest set bit. Repeat and count until n becomes 0 -- exactly as many steps as there are set bits.",
    optimal_code="""def hamming_weight(n):
    count = 0
    while n != 0:
        n &= (n - 1)
        count += 1
    return count""",
    optimal_time="O(k) (k = set bits)", optimal_space="O(1)",
    test="n=11 (0b1011) -> 3 iterations clear each set bit, count=3. Edge: n=0 -> loop condition false immediately, count=0.",
    other_edges="a power of 2 (exactly 1 set bit); all bits set for the width (e.g. 0xFFFFFFFF); n=1.",
    memory_hook="\"n AND (n-1) erases the lowest 1 -- count how many erasures until zero.\"",
))

PROBLEMS.append(dict(
    title="Pascal's Triangle", lc_num="118", difficulty="EASY", pattern="Simple DP (row from previous row)",
    video_note=NO_VIDEO,
    problem="Given numRows, generate the first numRows rows of Pascal's Triangle.",
    trigger="\"each value is the sum of the two above it\" → build each row directly from the previous row.",
    clarify="Every row starts and ends with 1? Output is a list of lists?",
    brute_idea="Compute each entry independently via the binomial coefficient formula (n choose k), recomputing factorials.",
    brute_code="""from math import comb

def generate_brute(num_rows):
    return [[comb(r, k) for k in range(r + 1)] for r in range(num_rows)]""",
    brute_time="O(numRows³) naive factorial", brute_space="O(numRows²)",
    bottleneck="Computing each entry independently via factorials redoes overlapping work; each row can be built directly and cheaply from the row before it.",
    optimal_insight="Each row starts/ends with 1; every middle value is the sum of the two values above it in the previous row.",
    optimal_code="""def generate(num_rows):
    triangle = [[1]]
    for _ in range(1, num_rows):
        prev = triangle[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i-1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle""",
    optimal_time="O(numRows²)", optimal_space="O(numRows²)",
    test="numRows=5 -> builds [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]. Edge: numRows=1 -> stays as just [[1]].",
    other_edges="numRows=2; confirming outer values are always 1; numRows=0 (empty list, if allowed).",
    memory_hook="\"Each new row: start with 1, sum adjacent pairs above, end with 1.\"",
))

PROBLEMS.append(dict(
    title="Longest Common Prefix", lc_num="14", difficulty="EASY", pattern="Vertical Scanning",
    video_note=NO_VIDEO,
    problem="Given an array of strings, find the longest common prefix shared by all of them, or '' if none.",
    trigger="\"longest common prefix among multiple strings\" → Vertical Scanning: compare one character position across ALL strings at once.",
    clarify="Case-sensitive? Can the array or an individual string be empty?",
    brute_idea="Compare every pair of strings for their pairwise common prefix, take the shortest across all pairs.",
    brute_code="""def longest_common_prefix_brute(strs):
    def common(a, b):
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return a[:i]
    prefix = strs[0]
    for s in strs[1:]:
        prefix = common(prefix, s)
    return prefix  # actually fine, but framed pairwise -- see vertical scan for the cleaner version""",
    brute_time="O(n * m)", brute_space="O(1)",
    bottleneck="Pairwise comparison works but reduces the whole set two at a time; checking all strings together at each position stops at the very first disagreement directly.",
    optimal_insight="For each character position in the first string, check if every OTHER string agrees there; stop at the first mismatch or short string.",
    optimal_code="""def longest_common_prefix(strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        ch = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]""",
    optimal_time="O(n * m)", optimal_space="O(1)",
    test="['flower','flow','flight'] -> matches 'fl', mismatches at position 2. Edge: no common prefix at all, e.g. ['dog','racecar','car'] -> mismatch at position 0, returns ''.",
    other_edges="single string in the array; one string is empty; all strings identical.",
    memory_hook="\"Check one position at a time across every string -- stop at first disagreement.\"",
))

PROBLEMS.append(dict(
    title="Integer to Roman", lc_num="12", difficulty="MEDIUM", pattern="Greedy",
    video_note=NO_VIDEO,
    problem="Convert an integer to its Roman numeral representation, including subtractive notation (IV, IX, etc.).",
    trigger="\"convert to Roman numerals\" → Greedy: ordered value list (including subtractive combos), always take the biggest value that fits.",
    clarify="Input guaranteed within the standard range (1-3999)?",
    brute_idea="Hardcode if/elif branches for every possible digit (0-9) at every place value (ones, tens, hundreds, thousands).",
    brute_code="""def int_to_roman_brute(num):
    # Illustrative only: this requires ~40 explicit branches,
    # one per digit value per place, e.g.:
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return (thousands[num // 1000] + hundreds[(num // 100) % 10] +
            tens[(num // 10) % 10] + ones[num % 10])""",
    brute_time="O(1)", brute_space="O(1)",
    bottleneck="Hardcoding every digit-place combination works but is repetitive and error-prone; a single ordered value list captures the same logic far more concisely.",
    optimal_insight="An ordered list of (value, symbol) pairs, largest to smallest, explicitly including subtractive combos (900='CM', 4='IV', etc). Greedily subtract the largest fitting value repeatedly.",
    optimal_code="""def int_to_roman(num):
    values = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
              (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
              (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = []
    for value, symbol in values:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)""",
    optimal_time="O(1)", optimal_space="O(1)",
    test="1994 -> M, CM, XC, IV -> 'MCMXCIV'. Edge: several subtractive combos in a row, e.g. 444 -> CD, XL, IV -> 'CDXLIV'.",
    other_edges="smallest input, num=1 ('I'); largest typical input, 3999; a round number like 1000 or 500 needing no subtractive parts.",
    memory_hook="\"Ordered list of values (including CM, CD, XC...) -- always take the biggest bite that fits.\"",
))

PROBLEMS.append(dict(
    title="Add Binary", lc_num="67", difficulty="EASY", pattern="Two Pointers + Carry",
    video_note=NO_VIDEO,
    problem="Given two binary strings, add them and return the sum, also as a binary string.",
    trigger="\"add two binary/base-b strings\" → simulate manual addition digit by digit with a carry, right to left.",
    clarify="Strings can be different lengths? Only '0'/'1' characters guaranteed?",
    brute_idea="Convert both to integers, add, convert back to binary (works in Python; not general to all languages).",
    brute_code="""def add_binary_brute(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]""",
    brute_time="O(n+m)", brute_space="O(n+m)",
    bottleneck="Works in Python (arbitrary-precision ints) but sidesteps demonstrating the intended digit-by-digit simulation, and isn't safe in fixed-integer-size languages.",
    optimal_insight="Process both strings right to left with two pointers, summing digits plus carry, building the result and finishing with any leftover carry.",
    optimal_code="""def add_binary(a, b):
    result = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry:
        da = int(a[i]) if i >= 0 else 0
        db = int(b[j]) if j >= 0 else 0
        total = da + db + carry
        carry = total // 2
        result.append(str(total % 2))
        i -= 1; j -= 1
    return ''.join(reversed(result))""",
    optimal_time="O(max(n,m))", optimal_space="O(max(n,m))",
    test="a='11'(3), b='1'(1) -> '100' (4). Edge: leftover carry, e.g. a='1', b='1' -> needs one extra digit, '10' (2).",
    other_edges="very different lengths; one string is just '0'; both strings all 1's (maximal carry chain).",
    memory_hook="\"Paper addition in base 2 -- sum digits plus carry, right to left.\"",
))
