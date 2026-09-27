VNOTE = lambda title, channel: (f'Video: "{title}" — {channel}. Transcript not retrievable in this '
    f'session (YouTube is blocked by this environment’s network policy); explained from general '
    f'algorithmic knowledge, not the video.')

PROBLEMS = []

PROBLEMS.append(dict(
    title="Two Sum", lc_num="1", difficulty="EASY", pattern="Hash Map",
    video_note=VNOTE("Two Sum - Leetcode 1 - HashMap - Python", "NeetCode"),
    problem="Given an array of integers and a target, return the indices of the two numbers that add up to the target. Exactly one solution exists; can't use the same element twice.",
    trigger="\"find two numbers that add up to X\" + need better than O(n²) → Hash Map (store complements as you scan).",
    brute_idea="Check every pair of indices and test if they sum to target.",
    brute_code="""def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []""",
    brute_time="O(n²)", brute_space="O(1)",
    optimal_insight="Store each value's index as you scan; before adding, check if target minus current value was already seen — one pass instead of two nested loops.",
    optimal_code="""def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Duplicate values, e.g. nums=[3,3], target=6 — works because we check the map BEFORE inserting the current number, so a number never pairs with itself at the same index.",
    memory_hook="\"I need the complement — remember what I've already seen.\"",
))

PROBLEMS.append(dict(
    title="Contains Duplicate", lc_num="217", difficulty="EASY", pattern="Hash Set",
    video_note=VNOTE("Contains Duplicate - Leetcode 217 - Python", "NeetCode"),
    problem="Given an array of integers, return true if any value appears at least twice, and false if every element is distinct.",
    trigger="\"has any value appeared before\" → Hash Set for O(1) membership checks.",
    brute_idea="Compare every pair of elements for equality.",
    brute_code="""def contains_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False""",
    brute_time="O(n²)", brute_space="O(1)",
    optimal_insight="A hash set lets me check 'have I seen this before' in O(1) average time, so one pass suffices.",
    optimal_code="""def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# One-liner alt: len(set(nums)) != len(nums)""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Empty array or single-element array — loop never finds a duplicate, correctly returns False.",
    memory_hook="\"Seen it before? Set tells you instantly.\"",
))

PROBLEMS.append(dict(
    title="Group Anagrams", lc_num="49", difficulty="MEDIUM", pattern="Hash Map",
    video_note=VNOTE("Group Anagrams - Categorize Strings by Count - Leetcode 49", "NeetCode"),
    problem="Given an array of strings, group the anagrams together (any order). Two strings are anagrams if they contain the same letters with the same counts.",
    trigger="\"group strings that are permutations of each other\" → canonical key + Hash Map.",
    brute_idea="Compare every string against every other by sorting both and checking equality.",
    brute_code="""def group_anagrams(strs):
    groups = []
    used = [False] * len(strs)
    for i in range(len(strs)):
        if used[i]:
            continue
        group = [strs[i]]
        for j in range(i + 1, len(strs)):
            if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                used[j] = True
        groups.append(group)
    return groups""",
    brute_time="O(n² * k log k)", brute_space="O(n * k)",
    optimal_insight="A 26-count tuple (or sorted string) is identical for all anagrams of a word, so it works as a hash map key that groups them in one pass.",
    optimal_code="""from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())""",
    optimal_time="O(n * k)", optimal_space="O(n * k)",
    edge_case="Empty string in the list — its count key is all zeros, forms its own group.",
    memory_hook="\"Same letter counts = same key = same bucket.\"",
))

PROBLEMS.append(dict(
    title="Product of Array Except Self", lc_num="238", difficulty="MEDIUM", pattern="Prefix/Suffix Products",
    video_note=VNOTE("Product of Array Except Self - Leetcode 238 - Python", "NeetCode"),
    problem="Given an array, return an array where each element is the product of all other elements, without using division, in O(n).",
    trigger="\"product/sum of everything except index i\", no division allowed → Prefix * Suffix products.",
    brute_idea="For each index, loop over the rest of the array and multiply everything else.",
    brute_code="""def product_except_self(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        result.append(product)
    return result""",
    brute_time="O(n²)", brute_space="O(1) extra",
    optimal_insight="Answer at i = (product of everything left of i) * (product of everything right of i). Build prefix products left-to-right, then fold in suffix products right-to-left.",
    optimal_code="""def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result""",
    optimal_time="O(n)", optimal_space="O(1) extra",
    edge_case="Array with one zero — every index except the zero's own becomes 0; array with two zeros — every index becomes 0.",
    memory_hook="\"Everything to my left, times everything to my right.\"",
))

PROBLEMS.append(dict(
    title="Subarray Sum Equals K", lc_num="560", difficulty="MEDIUM", pattern="Prefix Sum + Hash Map",
    video_note=VNOTE("Subarray Sum Equals K - Prefix Sums - Leetcode 560 - Python", "NeetCode"),
    problem="Given an array of integers and an integer k, return the total number of contiguous subarrays whose sum equals k. Numbers can be negative.",
    trigger="\"number of subarrays summing to k\", negatives allowed (rules out sliding window) → Prefix Sum + Hash Map.",
    brute_idea="Check every subarray's sum directly (or extend a running sum per start index).",
    brute_code="""def subarray_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count""",
    brute_time="O(n²)", brute_space="O(1)",
    optimal_insight="sum(i..j) = prefix[j] - prefix[i-1]. So sum(i..j)==k means prefix[i-1] == prefix[j]-k. Track how many times each prefix sum has occurred so far.",
    optimal_code="""from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    seen = defaultdict(int)
    seen[0] = 1  # empty prefix
    for num in nums:
        prefix_sum += num
        count += seen[prefix_sum - k]
        seen[prefix_sum] += 1
    return count""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="seen[0]=1 is required upfront — handles subarrays starting at index 0 whose sum is exactly k.",
    memory_hook="\"Two equal prefix sums — the gap between them sums to k.\"",
))

PROBLEMS.append(dict(
    title="Valid Palindrome", lc_num="125", difficulty="EASY", pattern="Two Pointers",
    video_note=VNOTE("Valid Palindrome - Leetcode 125 - Python", "NeetCode"),
    problem="Given a string, return true if it's a palindrome after converting to lowercase and removing all non-alphanumeric characters.",
    trigger="\"is this a palindrome\", need O(1) space → Two Pointers converging from both ends.",
    brute_idea="Build a cleaned version of the string, then compare it to its reverse.",
    brute_code="""def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]""",
    brute_time="O(n)", brute_space="O(n)",
    optimal_insight="Use two pointers from both ends, skipping non-alphanumeric characters in place, comparing directly — no extra string built.",
    optimal_code="""def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True""",
    optimal_time="O(n)", optimal_space="O(1)",
    edge_case="String with only non-alphanumeric characters, e.g. \".,\" — pointers cross without ever comparing, correctly returns True (empty string is a palindrome).",
    memory_hook="\"Skip junk, compare from both ends inward.\"",
))

PROBLEMS.append(dict(
    title="Container With Most Water", lc_num="11", difficulty="MEDIUM", pattern="Two Pointers",
    video_note=VNOTE("Container with Most Water - Leetcode 11 - Python", "NeetCode"),
    problem="Given heights of vertical lines, find two lines that together with the x-axis form a container holding the most water. Return the max area.",
    trigger="\"maximize area between two lines/indices\" → Two Pointers, always move the shorter side.",
    brute_idea="Check every pair of lines and compute the area they'd contain.",
    brute_code="""def max_area(height):
    best = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            best = max(best, area)
    return best""",
    brute_time="O(n²)", brute_space="O(1)",
    optimal_insight="Start with the widest container (both ends). The shorter wall is always the bottleneck, so move it inward — moving the taller wall could never help.",
    optimal_code="""def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, (right - left) * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best""",
    optimal_time="O(n)", optimal_space="O(1)",
    edge_case="All lines the same height — area is maximized by the widest pair, which the pointers reach immediately at the start.",
    memory_hook="\"Move the shorter wall — the taller one was never the limit.\"",
))

PROBLEMS.append(dict(
    title="Longest Substring Without Repeating Characters", lc_num="3", difficulty="MEDIUM", pattern="Sliding Window",
    video_note=VNOTE("Longest Substring Without Repeating Characters - Leetcode 3 - Python", "NeetCode"),
    problem="Given a string, find the length of the longest substring without repeating characters.",
    trigger="\"longest substring with no repeats / unique characters\" → Sliding Window + Hash Set.",
    brute_idea="Check every substring for uniqueness directly.",
    brute_code="""def length_of_longest_substring(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best""",
    brute_time="O(n²)", brute_space="O(min(n, charset))",
    optimal_insight="Expand the window right; if the new character is already in the window, shrink from the left until the duplicate is gone — window never revisits a position twice.",
    optimal_code="""def length_of_longest_substring(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best""",
    optimal_time="O(n)", optimal_space="O(min(n, charset))",
    edge_case="Empty string — loop never runs, best stays 0. All identical characters, e.g. \"aaaa\" — window size stays 1.",
    memory_hook="\"Duplicate found? Shrink from the left until it's gone.\"",
))

PROBLEMS.append(dict(
    title="Minimum Window Substring", lc_num="76", difficulty="HARD", pattern="Sliding Window",
    video_note=VNOTE("Minimum Window Substring - Airbnb Interview Question - Leetcode 76", "NeetCode"),
    problem="Given strings s and t, find the minimum window substring of s that contains every character of t (with at least its multiplicity), or empty string if none exists.",
    trigger="\"smallest window containing all characters of another string\" → Sliding Window + character-count matching.",
    brute_idea="Check every substring of s and test whether it contains all of t's characters.",
    brute_code="""from collections import Counter

def min_window(s, t):
    need = Counter(t)
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            window = Counter(s[i:j+1])
            if all(window[c] >= need[c] for c in need):
                if best == "" or j - i + 1 < len(best):
                    best = s[i:j+1]
    return best""",
    brute_time="O(n³)", brute_space="O(n)",
    optimal_insight="Expand right until the window satisfies all of t's counts; then shrink from the left as much as possible while still valid, recording the smallest valid window found.",
    optimal_code="""from collections import Counter

def min_window(s, t):
    if not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (float('inf'), 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float('inf') else s[best[1]:best[2]+1]""",
    optimal_time="O(n + m)", optimal_space="O(charset)",
    edge_case="t longer than s, or t has characters not in s — missing never reaches 0, correctly returns empty string.",
    memory_hook="\"Expand until valid, then shrink until it breaks — record the smallest valid window.\"",
))

PROBLEMS.append(dict(
    title="Valid Parentheses", lc_num="20", difficulty="EASY", pattern="Stack",
    video_note=VNOTE("Valid Parentheses - Stack - Leetcode 20 - Python", "NeetCode"),
    problem="Given a string of just '()[]{}' characters, determine if the brackets are validly matched and nested.",
    trigger="\"matching brackets / valid nesting\" → Stack.",
    brute_idea="Repeatedly remove any adjacent matched pair like '()' , '[]', '{}' from the string until no more removals are possible; valid iff the string becomes empty.",
    brute_code="""def is_valid(s):
    pairs = ["()", "[]", "{}"]
    changed = True
    while changed:
        changed = False
        for p in pairs:
            if p in s:
                s = s.replace(p, "", 1)
                changed = True
    return len(s) == 0""",
    brute_time="O(n²)", brute_space="O(n)",
    optimal_insight="Push opening brackets. On a closing bracket, it must match the top of the stack (the most recently opened, still-unclosed bracket); if not, invalid.",
    optimal_code="""def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Unmatched closing bracket with an empty stack, e.g. \")(\" — caught by 'not stack' check before popping.",
    memory_hook="\"Push opens; a close must match the most recent open.\"",
))

PROBLEMS.append(dict(
    title="Design Min Stack", lc_num="155", difficulty="MEDIUM", pattern="Stack (Auxiliary Min Stack)",
    video_note=VNOTE("Design Min Stack - Amazon Interview Question - Leetcode 155 - Python", "NeetCode"),
    problem="Design a stack supporting push, pop, top, and getMin, all in O(1) time.",
    trigger="\"design a stack with O(1) getMin/getMax\" → parallel auxiliary min-stack.",
    brute_idea="Plain stack; getMin scans the whole stack every time it's called.",
    brute_code="""class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return min(self.stack)   # O(n) !""",
    brute_time="push/pop/top O(1), getMin O(n)", brute_space="O(n)",
    optimal_insight="Maintain a second stack that always stores the running minimum alongside each push, so it's popped in lockstep and always instantly available.",
    optimal_code="""class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        m = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(m)
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]""",
    optimal_time="O(1) all ops", optimal_space="O(n)",
    edge_case="Pushing duplicate minimum values then popping one — min_stack's per-push min() means the remaining copy is still correctly reported.",
    memory_hook="\"A second stack, always remembering the min-so-far.\"",
))

PROBLEMS.append(dict(
    title="Daily Temperatures", lc_num="739", difficulty="MEDIUM", pattern="Monotonic Stack",
    video_note=VNOTE("Daily Temperatures - Monotonic Stack - Leetcode 739 - Python", "NeetCode"),
    problem="Given daily temperatures, return an array where answer[i] is how many days until a warmer temperature; 0 if none exists.",
    trigger="\"next greater/warmer element to the right\" → Monotonic (decreasing) Stack.",
    brute_idea="For each day, scan forward until a warmer day is found.",
    brute_code="""def daily_temperatures(temps):
    n = len(temps)
    answer = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temps[j] > temps[i]:
                answer[i] = j - i
                break
    return answer""",
    brute_time="O(n²)", brute_space="O(1) extra",
    optimal_insight="Keep a stack of day-indices whose warmer day hasn't been found yet. When a warmer day appears, it resolves every cooler day still waiting on the stack.",
    optimal_code="""def daily_temperatures(temps):
    answer = [0] * len(temps)
    stack = []  # indices, decreasing temps
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Strictly decreasing temperatures — nothing ever gets popped, every answer stays 0.",
    memory_hook="\"Stack of unresolved days; a warmer day resolves everyone smaller beneath it.\"",
))

PROBLEMS.append(dict(
    title="Evaluate Reverse Polish Notation", lc_num="150", difficulty="MEDIUM", pattern="Stack",
    video_note=VNOTE("Evaluate Reverse Polish Notation - Leetcode 150 - Python", "NeetCode"),
    problem="Given tokens of a postfix arithmetic expression (+ - * /), evaluate it and return the integer result.",
    trigger="\"postfix / Reverse Polish Notation evaluation\" → Stack.",
    brute_idea="There's no simpler alternative to a stack here; a naive idea (convert to infix and use a general parser) is more complex, not simpler.",
    brute_code="""# A general infix-parser approach still needs precedence
# handling and is strictly more complex than the stack
# approach below for postfix notation - not shown as a
# separate 'slower but simpler' baseline; go straight to
# the stack-based evaluation, which is already optimal.""",
    brute_time="N/A", brute_space="N/A",
    optimal_insight="Postfix means an operator always combines the two MOST RECENT operands — a stack naturally holds 'most recent' in order.",
    optimal_code="""def eval_rpn(tokens):
    stack = []
    ops = {'+', '-', '*', '/'}
    for tok in tokens:
        if tok not in ops:
            stack.append(int(tok))
        else:
            b = stack.pop()
            a = stack.pop()
            if tok == '+': stack.append(a + b)
            elif tok == '-': stack.append(a - b)
            elif tok == '*': stack.append(a * b)
            else: stack.append(int(a / b))  # truncate toward 0
    return stack.pop()""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Negative division, e.g. -7/2 — use int(a/b), not a//b, since // floors toward -inf but this problem truncates toward 0.",
    memory_hook="\"Numbers pile up; an operator pops the top two and pushes the result.\"",
))

PROBLEMS.append(dict(
    title="Implement Queue using Stacks", lc_num="232", difficulty="EASY", pattern="Stack (Two-Stack Trick)",
    video_note=VNOTE("Implement Queue using Stacks - Leetcode 232 - Python", "NeetCodeIO"),
    problem="Implement a FIFO queue using only two stacks, supporting push, pop, peek, and empty.",
    trigger="\"implement X using only Y\" → look for a two-structure trick (here: two stacks, one for in, one for out).",
    brute_idea="Use one stack for input; to pop/peek (need the OLDEST item), pop everything into a temp list, take the item, then push everything back — done every single call.",
    brute_code="""class MyQueue:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        result = self.stack.pop()
        while temp:
            self.stack.append(temp.pop())
        return result   # O(n) every call!""",
    brute_time="pop/peek O(n) every call", brute_space="O(n)",
    optimal_insight="Two stacks: 'in_stack' for pushes, 'out_stack' for pops. Only transfer in->out when out_stack is empty; each element is moved at most once, ever.",
    optimal_code="""class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x):
        self.in_stack.append(x)
    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
    def pop(self):
        self._shift()
        return self.out_stack.pop()
    def peek(self):
        self._shift()
        return self.out_stack[-1]
    def empty(self):
        return not self.in_stack and not self.out_stack""",
    optimal_time="O(1) amortized", optimal_space="O(n)",
    edge_case="Interleaved push/pop calls — out_stack only refills once it's fully drained, so relative FIFO order is still preserved correctly.",
    memory_hook="\"Two stacks: reverse once into 'out', drain it fully before refilling.\"",
))

PROBLEMS.append(dict(
    title="Implement Stack using Queues", lc_num="225", difficulty="EASY", pattern="Queue (Rotation Trick)",
    video_note=VNOTE("Implement Stack using Queues - Leetcode 225 - Python", "NeetCode"),
    problem="Implement a LIFO stack using only queues, supporting push, pop, top, and empty.",
    trigger="\"implement X using only Y\" → use a rotation trick so the newest element ends up at the front of the queue.",
    brute_idea="Use two queues; to push, add to the empty one, then move everything from the other queue behind it, then swap names — O(n) per push done via an extra queue.",
    brute_code="""from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        return self.q1.popleft()
    def top(self):
        return self.q1[0]
    def empty(self):
        return not self.q1""",
    brute_time="push O(n)", brute_space="O(n)",
    optimal_insight="Single queue: after appending the new element, rotate the queue by rotating everything BEFORE it to behind it — the new element ends up at the front, acting like the top of a stack.",
    optimal_code="""from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return not self.q""",
    optimal_time="push O(n), pop/top O(1)", optimal_space="O(n)",
    edge_case="Single-element stack — the rotation loop runs zero times (len(q)-1 == 0), element just stays at the front.",
    memory_hook="\"Rotate the queue so the newest push lands at the front.\"",
))

PROBLEMS.append(dict(
    title="Maximum Depth of Binary Tree", lc_num="104", difficulty="EASY", pattern="DFS / Recursion",
    video_note=VNOTE("Maximum Depth of Binary Tree - 3 Solutions - Leetcode 104 - Python", "NeetCode"),
    problem="Given the root of a binary tree, return its maximum depth (number of nodes on the longest root-to-leaf path).",
    trigger="\"depth/height of a tree\" → DFS Recursion: 1 + max(left, right).",
    brute_idea="There isn't a distinct slower approach here; the natural solution IS the recursive one below. An alternative worth showing is iterative BFS (level counting).",
    brute_code="""from collections import deque

def max_depth_bfs(root):
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth""",
    brute_time="O(n)", brute_space="O(n) worst case",
    optimal_insight="Depth of a tree = 1 + max(depth of left subtree, depth of right subtree); null node has depth 0. Direct recursive definition.",
    optimal_code="""def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)""",
    optimal_time="O(n)", optimal_space="O(h)",
    edge_case="Empty tree (root=None) — base case returns 0 immediately.",
    memory_hook="\"1 plus whichever child subtree goes deeper.\"",
))

PROBLEMS.append(dict(
    title="Binary Tree Level Order Traversal", lc_num="102", difficulty="MEDIUM", pattern="BFS",
    video_note=VNOTE("Binary Tree Level Order Traversal - BFS - Leetcode 102", "NeetCode"),
    problem="Given the root of a binary tree, return the node values grouped level by level (left to right), as a list of lists.",
    trigger="\"process a tree/grid level by level\" → BFS with a queue, snapshotting queue size per level.",
    brute_idea="DFS could work but requires tracking depth explicitly and appending to the right list — more error-prone than BFS's natural level grouping.",
    brute_code="""def level_order_dfs(root):
    result = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(result):
            result.append([])
        result[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    dfs(root, 0)
    return result""",
    brute_time="O(n)", brute_space="O(n)",
    optimal_insight="BFS naturally processes one level at a time. Snapshot the queue's current size before processing, so that batch is exactly one level's worth of nodes.",
    optimal_code="""from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="Empty tree — guard clause returns [] immediately.",
    memory_hook="\"Snapshot queue size = process exactly one level.\"",
))

PROBLEMS.append(dict(
    title="Binary Tree Vertical Order Traversal", lc_num="314", difficulty="MEDIUM", pattern="BFS + Hash Map (Column Index)",
    video_note=VNOTE("Binary Tree Vertical Order Traversal - Leetcode 314 - Python", "NeetCodeIO"),
    problem="Given a binary tree, return the node values grouped by vertical column, ordered left to right; within a column, top to bottom, and left-to-right for ties at the same node depth.",
    trigger="\"vertical columns of a tree\" → track a column index while doing BFS, group by column in a hash map.",
    brute_idea="DFS while tracking (column, row) pairs, then sort all (column, row, value) triples at the end.",
    brute_code="""def vertical_order_dfs(root):
    triples = []
    def dfs(node, col, row):
        if not node:
            return
        triples.append((col, row, node.val))
        dfs(node.left, col - 1, row + 1)
        dfs(node.right, col + 1, row + 1)
    dfs(root, 0, 0)
    triples.sort()  # by col, then row, then value
    result = {}
    for col, row, val in triples:
        result.setdefault(col, []).append(val)
    return [result[c] for c in sorted(result)]""",
    brute_time="O(n log n)", brute_space="O(n)",
    optimal_insight="BFS processes nodes level by level (top to bottom, left to right) automatically, so within a column, values are already appended in correct order — no final sort needed, just group by column index and sort column KEYS at the end.",
    optimal_code="""from collections import deque, defaultdict

def vertical_order(root):
    if not root:
        return []
    columns = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, col = queue.popleft()
        columns[col].append(node.val)
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
    return [columns[c] for c in sorted(columns)]""",
    optimal_time="O(n log n)", optimal_space="O(n)",
    edge_case="Two nodes landing in the same column AND same BFS level (siblings from different parents) — BFS's left-to-right level processing naturally orders them correctly.",
    memory_hook="\"BFS order is already top-to-bottom, left-to-right — just bucket by column.\"",
))

PROBLEMS.append(dict(
    title="Clone Graph", lc_num="133", difficulty="MEDIUM", pattern="DFS/BFS + Hash Map",
    video_note=VNOTE("Clone Graph - Depth First Search - Leetcode 133", "NeetCode"),
    problem="Given a reference node in a connected undirected graph, return a deep copy (clone) of the entire graph.",
    trigger="\"deep copy a graph/structure with arbitrary cross-references\" → Hash Map from original node to its clone.",
    brute_idea="There isn't a meaningfully 'slower' correct alternative — you fundamentally need some way to avoid re-cloning (and infinitely looping on) a node you've already visited. Naive recursion WITHOUT a visited map would infinite-loop on any cycle.",
    brute_code="""# Recursion without tracking visited nodes:
def clone_graph_broken(node):
    if not node:
        return None
    copy = Node(node.val)
    for neighbor in node.neighbors:
        copy.neighbors.append(clone_graph_broken(neighbor))
    return copy
# BROKEN: infinite recursion on any cycle back to a
# node already being cloned (graphs here are typically cyclic).""",
    brute_time="Infinite loop on cycles", brute_space="N/A",
    optimal_insight="A hash map from original node to its clone both (a) prevents infinite recursion on cycles and (b) lets neighbors correctly reference already-created clones.",
    optimal_code="""def clone_graph(node):
    if not node:
        return None
    old_to_new = {}
    def dfs(n):
        if n in old_to_new:
            return old_to_new[n]
        copy = Node(n.val)
        old_to_new[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)""",
    optimal_time="O(V + E)", optimal_space="O(V)",
    edge_case="Single node with a self-loop neighbor — map entry is created BEFORE recursing into neighbors, so the self-reference resolves to the already-created clone instead of looping forever.",
    memory_hook="\"Map original -> clone FIRST, then recurse into neighbors.\"",
))

PROBLEMS.append(dict(
    title="Course Schedule", lc_num="207", difficulty="MEDIUM", pattern="Graph DFS / Topological Sort (Cycle Detection)",
    video_note=VNOTE("Course Schedule - Graph Adjacency List - Leetcode 207", "NeetCode"),
    problem="Given numCourses and prerequisite pairs [a, b] (must take b before a), return whether it's possible to finish all courses (i.e., the prerequisite graph has no cycle).",
    trigger="\"can all tasks be completed given dependencies\" → cycle detection in a directed graph (DFS with a recursion-stack marker, or Topological Sort / Kahn's algorithm).",
    brute_idea="Try every possible course order (permutations) and check if any order satisfies all prerequisites — combinatorially expensive.",
    brute_code="""from itertools import permutations

def can_finish_brute(numCourses, prerequisites):
    for order in permutations(range(numCourses)):
        position = {c: i for i, c in enumerate(order)}
        if all(position[b] < position[a] for a, b in prerequisites):
            return True
    return False  # O(n!) - only feasible for tiny n""",
    brute_time="O(n!)", brute_space="O(n)",
    optimal_insight="A valid course order exists iff the prerequisite graph has no cycle. DFS each course, marking nodes 'in current path'; if DFS revisits a node still in the current path, that's a cycle.",
    optimal_code="""def can_finish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[a].append(b)
    state = [0] * numCourses  # 0=unvisited,1=visiting,2=done
    def dfs(course):
        if state[course] == 1:
            return False  # cycle!
        if state[course] == 2:
            return True
        state[course] = 1
        for pre in graph[course]:
            if not dfs(pre):
                return False
        state[course] = 2
        return True
    return all(dfs(c) for c in range(numCourses))""",
    optimal_time="O(V + E)", optimal_space="O(V + E)",
    edge_case="A course that depends on itself, e.g. [0,0] — DFS immediately revisits course 0 while it's still marked 'visiting' (state 1), correctly detecting the cycle.",
    memory_hook="\"Mark 'in-progress'; revisiting an in-progress node means a cycle.\"",
))

PROBLEMS.append(dict(
    title="Binary Search", lc_num="704", difficulty="EASY", pattern="Binary Search",
    video_note=VNOTE("Binary Search - Leetcode 704 - Python", "NeetCode"),
    problem="Given a sorted array of integers and a target, return its index, or -1 if not present, in O(log n).",
    trigger="\"sorted array + search for a value\" → Binary Search.",
    brute_idea="Scan every element left to right until the target is found.",
    brute_code="""def search(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1""",
    brute_time="O(n)", brute_space="O(1)",
    optimal_insight="Sorted order means comparing the middle element tells you which entire half to discard — halving the search space every step.",
    optimal_code="""def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1""",
    optimal_time="O(log n)", optimal_space="O(1)",
    edge_case="Target not present, e.g. searching for a value between two elements — left ends up greater than right, loop exits, returns -1.",
    memory_hook="\"Middle tells you which whole half to throw away.\"",
))

PROBLEMS.append(dict(
    title="Find Minimum in Rotated Sorted Array", lc_num="153", difficulty="MEDIUM", pattern="Binary Search (Modified)",
    video_note=VNOTE("Find Minimum in Rotated Sorted Array - Binary Search - Leetcode 153 - Python", "NeetCode"),
    problem="Given a rotated sorted array with all-unique values, find the minimum element in O(log n).",
    trigger="\"rotated sorted array\" → Binary Search comparing mid against the right boundary to decide which half is 'still sorted'.",
    brute_idea="Scan the whole array to find the minimum directly.",
    brute_code="""def find_min(nums):
    return min(nums)  # O(n), ignores the sorted structure""",
    brute_time="O(n)", brute_space="O(1)",
    optimal_insight="Compare nums[mid] to nums[right]. If nums[mid] > nums[right], the minimum is in the right half (rotation point is there); otherwise it's in the left half (mid could BE the minimum, so don't exclude it).",
    optimal_code="""def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]""",
    optimal_time="O(log n)", optimal_space="O(1)",
    edge_case="Array not rotated at all (already fully sorted) — nums[mid] is never greater than nums[right], so right keeps shrinking to index 0, correctly returning nums[0].",
    memory_hook="\"Compare mid to the right edge — that tells you which side hides the rotation.\"",
))

PROBLEMS.append(dict(
    title="LRU Cache", lc_num="146", difficulty="MEDIUM", pattern="Hash Map + Doubly Linked List",
    video_note=VNOTE("LRU Cache - Twitch Interview Question - Leetcode 146", "NeetCode"),
    problem="Design a Least Recently Used (LRU) cache with a fixed capacity, supporting get(key) and put(key, value), both in O(1) average time.",
    trigger="\"design a cache with O(1) get/put and eviction of the least recently used item\" → Hash Map (O(1) lookup) + Doubly Linked List (O(1) reorder/evict).",
    brute_idea="Use a plain dict for values plus a separate list tracking usage order; every get/put requires an O(n) scan or shift of that order list.",
    brute_code="""class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = {}
        self.order = []  # least-recent at index 0
    def get(self, key):
        if key not in self.data:
            return -1
        self.order.remove(key)      # O(n)
        self.order.append(key)
        return self.data[key]
    def put(self, key, value):
        if key in self.data:
            self.order.remove(key)  # O(n)
        elif len(self.data) >= self.cap:
            oldest = self.order.pop(0)  # O(n)
            del self.data[oldest]
        self.data[key] = value
        self.order.append(key)""",
    brute_time="O(n) per get/put", brute_space="O(n)",
    optimal_insight="A hash map gives O(1) lookup by key; a doubly linked list gives O(1) removal/insertion at any position (no shifting) to track recency order, moving a node to the front on every access.",
    optimal_code="""class Node:
    def __init__(self, k, v):
        self.key, self.val = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.left = Node(0, 0)   # least recent side
        self.right = Node(0, 0)  # most recent side
        self.left.next = self.right
        self.right.prev = self.left
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    def _insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = node
        self.right.prev = node
    def get(self, key):
        if key not in self.map:
            return -1
        self._remove(self.map[key]); self._insert(self.map[key])
        return self.map[key].val
    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._insert(node)
        if len(self.map) > self.cap:
            lru = self.left.next
            self._remove(lru); del self.map[lru.key]""",
    optimal_time="O(1) get/put", optimal_space="O(capacity)",
    edge_case="Updating an existing key's value — must remove the old node and reinsert (or move) it to the most-recent end, not just overwrite val in place.",
    memory_hook="\"Map for O(1) lookup, doubly linked list for O(1) reorder — evict from the far end.\"",
))

PROBLEMS.append(dict(
    title="Random Pick with Weight", lc_num="528", difficulty="MEDIUM", pattern="Prefix Sum + Binary Search",
    video_note=VNOTE("Random Pick with Weight | Bucket approach | Leetcode #528 | Binary search", "Techdose"),
    problem="Given an array of positive weights, design a structure that picks an index at random, where the probability of picking index i is proportional to weights[i].",
    trigger="\"pick randomly with weighted probability\" → Prefix Sum turns weights into ranges; Binary Search finds which range a random point falls into.",
    brute_idea="Build a 'bucket' array where each index appears weights[i] times, then pick a uniformly random element from that array directly.",
    brute_code="""import random

class Solution:
    def __init__(self, w):
        self.buckets = []
        for i, weight in enumerate(w):
            self.buckets.extend([i] * weight)  # O(total weight) space!
    def pick_index(self):
        return random.choice(self.buckets)""",
    brute_time="build O(sum(w)), pick O(1)", brute_space="O(sum(w))",
    optimal_insight="Build a prefix-sum array of weights (cumulative ranges). Pick a random number in [1, total], then binary search for the first prefix sum >= that number — that index's range contains the random point.",
    optimal_code="""import random, bisect

class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total
    def pick_index(self):
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)""",
    optimal_time="build O(n), pick O(log n)", optimal_space="O(n)",
    edge_case="A single weight of value 1 — prefix=[1], any random target (must be 1) maps to index 0 correctly.",
    memory_hook="\"Weights become ranges (prefix sums); binary search finds which range the dart landed in.\"",
))

PROBLEMS.append(dict(
    title="Rotting Oranges", lc_num="994", difficulty="MEDIUM", pattern="Multi-Source BFS",
    video_note=VNOTE("Rotting Oranges - Leetcode 994 - Python", "NeetCode"),
    problem="A grid has empty cells, fresh oranges, and rotten oranges. Every minute, rot spreads to adjacent fresh oranges. Return the minutes until no fresh orange remains, or -1 if impossible.",
    trigger="\"spreads simultaneously from multiple sources over discrete time steps\" → Multi-Source BFS (each BFS level = one minute).",
    brute_idea="Simulate minute by minute: rescan the WHOLE grid every minute to find newly-infected oranges.",
    brute_code="""def oranges_rotting_brute(grid):
    rows, cols = len(grid), len(grid[0])
    minutes = 0
    while True:
        fresh_left = False
        to_rot = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_left = True
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==2:
                            to_rot.append((r,c))
                            break
        if not to_rot:
            return -1 if fresh_left else minutes
        for r, c in to_rot:
            grid[r][c] = 2
        minutes += 1""",
    brute_time="O((rows*cols)²)", brute_space="O(rows*cols)",
    optimal_insight="Seed a BFS queue with EVERY rotten orange at once. Each full BFS level = exactly one minute of simultaneous spreading; no rescanning needed.",
    optimal_code="""from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r, c))
            elif grid[r][c] == 1: fresh += 1
    minutes = 0
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
    return minutes if fresh == 0 else -1""",
    optimal_time="O(rows * cols)", optimal_space="O(rows * cols)",
    edge_case="A fresh orange fully sealed off by walls/empty cells with no path to any rotten orange — fresh never reaches 0, correctly returns -1.",
    memory_hook="\"Seed BFS with every rotten orange at once — BFS levels ARE the minutes.\"",
))

PROBLEMS.append(dict(
    title="Maximum Subarray", lc_num="53", difficulty="MEDIUM", pattern="Dynamic Programming (Kadane's Algorithm)",
    video_note=VNOTE("Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python", "NeetCode"),
    problem="Given an integer array (possibly with negatives), find the contiguous subarray with the largest sum and return that sum.",
    trigger="\"contiguous subarray, maximum sum\" → Kadane's Algorithm (running sum, reset when it goes negative).",
    brute_idea="Check every possible subarray's sum directly (or extend a running sum per start index).",
    brute_code="""def max_subarray(nums):
    best = nums[0]
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            best = max(best, total)
    return best""",
    brute_time="O(n²)", brute_space="O(1)",
    optimal_insight="If the running sum ever goes negative, it can only hurt any future subarray — drop it and restart at the current element instead of carrying it forward.",
    optimal_code="""def max_subarray(nums):
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best""",
    optimal_time="O(n)", optimal_space="O(1)",
    edge_case="All-negative array, e.g. [-3,-1,-2] — current/best start at nums[0] (not 0), so the answer correctly becomes the least-negative single element, -1.",
    memory_hook="\"A negative running sum is dead weight — drop it and start fresh.\"",
))

PROBLEMS.append(dict(
    title="Top K Frequent Elements", lc_num="347", difficulty="MEDIUM", pattern="Bucket Sort (or Heap)",
    video_note=VNOTE("Top K Frequent Elements - Bucket Sort - Leetcode 347 - Python", "NeetCode"),
    problem="Given an integer array and an integer k, return the k most frequently occurring elements, in any order.",
    trigger="\"top k frequent / most common\" → count frequencies, then Bucket Sort by frequency for true O(n) (or a size-k heap for O(n log k)).",
    brute_idea="Count frequencies, then fully sort all distinct values by count and take the top k.",
    brute_code="""from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    sorted_items = sorted(counts.items(), key=lambda x: -x[1])
    return [val for val, cnt in sorted_items[:k]]""",
    brute_time="O(n log n)", brute_space="O(n)",
    optimal_insight="Frequency can never exceed n, so make 'buckets' indexed by frequency (0..n); put each value in its frequency's bucket, then read off values from the highest bucket down until k are collected — no comparison sort needed.",
    optimal_code="""from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for val, freq in counts.items():
        buckets[freq].append(val)
    result = []
    for freq in range(n, 0, -1):
        for val in buckets[freq]:
            result.append(val)
            if len(result) == k:
                return result
    return result""",
    optimal_time="O(n)", optimal_space="O(n)",
    edge_case="k equals the number of distinct elements — loop collects everything before returning, naturally covering that case.",
    memory_hook="\"Bucket index = frequency — no sorting needed, frequency is bounded by n.\"",
))
