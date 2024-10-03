- 如果一道题很难，我可以从test case开始列举答案，然后从列举中找到规律，我应该相信我自己脑内有自己的算法
- 从一开始先暴力破解并不是一个坏的想法
- 解决问题的目的并不是编码，而是发现解决问题的方案，不断的发现关键点
  - 一定要首先确认你要解决的问题！这是一切的前提！
- 利用对数据结构的理解，找到最适配你的问题的工具，和方案
- 更改数据结构来适配一个算法，或者更改一个算法来适配一个数据结构
- 如果可以找到一个解决方案，那么意味着可以分析现有方案，然后去寻找更好的方法，这在系统设计和普通的工作中都是相通的东西和思考方式
- *所以看似是在考你的代码能力，实际考察的是你的思考能力，这很重要*
- 编码点：分funcs，注释，命名
- 不只是编码，solution也是同样的解决问题的过程，从一个大致可行的方案，到不断优化的方案，甚至最后我们自己可以创造新的方案。每一个算法都是一种思考方式！数学的每一个原理也是一个思考方式。
- 相比较暴力破解，优化解法的目的在，用思考的力量战胜放弃思考。
- **性能优化**这件事是很常见的，在数据处理中也是，在SQL优化中也是，如果没有这种思想，那么就是不合格的工程师
- Pythonであれば、defaultdict、OrderedDict、Counter、deque、bisect、heap、map/reduce、内包(comprehension)表記、lambda式(ソートのkeyを書くのに便利)、with表記などできるだけしっかり覚えておくとよい。


## steps:

1. Ask Constraints

- Are the nums all positive?
- Are there any duplicates?
- edge case? []case? one element case? Does it have solution?
- What do I return when no solution? None?
- The solution is only one pair?

2. Write some test cases
3. Figure out a solution without code
4. Write out the solution code
5. Doule check for errors
6. Test the code with test cases: this is really explain the code step by step
7. Analyze space and time complexity: if it is exponential, it definitly can by improved
8. Optimize the solution

## Strategies:

1. **Break the problem down**: Start by thoroughly understanding the problem. Clarify any ambiguities, restate the problem in your own words, and break it into smaller parts. Interviewers often value how you approach a problem more than just finding the optimal solution right away.

2. **Pattern recognition**: Many problems in coding interviews are variations of common patterns (two pointers, sliding window, dynamic programming, divide and conquer, etc.). Try to map the problem to a pattern you're familiar with. Even if it’s new, it likely has some familiar structure.

3. **Start simple**: Don't worry about jumping to the optimal solution immediately. Start by explaining the brute-force approach or the most intuitive one. This shows you understand the problem, and you can then discuss how to optimize it.

4. **Think aloud**: Share your thought process openly during the interview. It helps you organize your thinking, and interviewers can give hints if they see you heading in the right direction.

5. **Ask for constraints**: Interviewers might not explicitly mention important constraints (e.g., size limits). Asking about them can help you avoid over-engineering or missing key insights.

6. **Practice flexibility**: Exposure to different problem types will improve your ability to adapt. As you practice more problems, you'll start seeing patterns that are common across a range of problems, improving your ability to adapt quickly in an interview.

Focusing on these strategies will help me approach unfamiliar problems with confidence!
