"""__author__ = 'anyu'
"""
"""
11.1
Find the mistake(s) in the following code:

unsigned int i;
for (i = 100; i <= 0; --i)
    printf(“%d\n”, i);
unsigned int i; //unsigned int类型，无符号整型，恒大于等于0
for (i = 100; i <= 0; --i) //错误，100<=0为假，循环一次也不执行。
                          //改为i>=0,错误，因为i恒>=0，无限循环
                          //改为i>0，正确，输出100到1的数。
    printf(“%d\n”, i);

上题还可以这样改：
int i;
for (i = 100; i >= 0; --i)
    printf(“%d\n”, i);
输出100到0的数。

11.2
You are given the source to an application which crashes when it is run. After running it ten times in a debugger, you find it never crashes in the same place. The application is single threaded, and uses only the C standard library. What programming errors could be causing this crash? How would you test each one?
这个问题很大程度上取决于应用程序的类型，当然了， 我们还是可以给出一些导致随机崩溃的常见的原因。
Random Variable
Uninitialized Voriable
Memory Leak
External Dependencies
随机的变量：应用程序使用了一些随机的变量或是数值， 由于每次执行这些数都不一样，导致崩溃的地方也不一样。比如：用户输入， 程序产生的随机数，当前系统时间等。
内存泄漏：由于内存泄漏导致程序最终将内存用尽而崩溃。 这个的随机性是由于程序运行时，系统中的进程数量不一样所导致的。 这也包含了堆的溢出或是栈中数据被破坏。
崩溃的原因还可能是由于程序依赖于其它应用程序或是外部模块所导致的。 比如应用程序依赖于系统的某些属性，而它们又被其它应用程序所修改， 那么就有可能导致程序的随机崩溃。与硬件交互得多的应用程序更可能产生这类错误。

在面试中，我们应该问面试官，这个程序是什么类型的，用途是什么？ 这些信息将帮助你找到问题所在(或是面试官所期望的答案)。比如说， web服务器崩溃的原因更可能是由于内存泄漏， 而底层应用程序崩溃的原因就更可能是由于系统依赖。

11.3
We have the following method used in a chess game: boolean canMoveTo(int x, int y) x and y are the coordinates of the chess board and it returns whether or not the piece can move to that position. Explain how you would test this method.
extreme case validation,bad input
 General Testing:The key to this problem is recognizing that we can't test every possible scenario
有两个基本的测试类型是我们要做的：验证输入输出的有效性及功能性测试。
1输入输出的有效性
我们需要验证输入输出以保证它们是有效的值，这意味着我们需要：
检查输入是否在棋盘内： 给函数传入负值。 给函数传入大于宽度的x值 给函数传入大于高度的y值 根据具体的实现，以上情况要么返回false，要么抛出异常。
检查输出是否合法（本题目不需要，因为输出是true或者false，无所谓合不合法。）
2功能性测试
理论上来说，我们应该去测试象棋棋盘的所有可能布局，但由于这个数量太大了， 这样做根本不现实。因此，我们只去测试这其中比较具有代表性的一些情况。 象棋中有6种棋子(国际象棋：王，后，车，象，马，兵)，我们按照以下算法做测试：
取出6种棋子中的一个a
    除了a的棋子中，取出一个b
        在方向集合中取出一个方向d
            用棋子a创建一个棋盘布局(放在棋盘所有可能的地方)
            将b放在方向d上的一个位置
            尝试移动，并检查返回值

11.4
How would you load test a webpage without using any test tools?
• Response time
• Throughput
• Resource utilization
• Maximum load that the systemcan bear.
负载测试的一些主要指标包括：
响应时间
吞吐量
资源利用率
系统承受的最大负载
题目说不能使用测试工具，那么我们可以自己写程序针对以上指标来模拟测试。 比如我们可以写一个多线程的程序来模拟成千上万的用户同时访问这个网页。 对于每个线程，我们再去单独测量网页的响应时间，数据IO等。
将程序模拟测试收集到的数据与可接受的数值进行对比，然后对结果进行分析。

11.5
How would you test a pen?
This problem is largely about understanding the constraints and approaching the problem in a structured manner.
To understand the constraints, you should ask a lot of questions to understand the "who, what, where, when, how and why" Remember that a good tester understands exactly what he is testing before starting the work.
The key here is structure,
• Fact check: Verify that the pen is felt tip and that the ink is one of the allowed colors.
• Intended use: Drawing. Does the pen write properly on clothing?
• Intended use: Washing. Does it wash off of clothing (even if it's been there for an extended period of time)? Does it wash off in hot, warm and cold water?
• Safety: Is the pen safe (non-toxic) for children?
• Unintended uses:
你怎么去测试一支笔？这个问题非常开放，越是开放的问题，我们就越应该给它加上限制。 于是你应该不断地问面试官问题来确定你到底要测试的是一只怎样的笔。 让我们通过以下的模拟对话来学习回答这类题目的技巧：
面试官：你怎么去测试一只笔？
面试者：这只笔的使用人群是？
面试官：可能是儿童
面试者：他们用这只笔来干嘛？写字？绘画？还是做其它的？
面试官：绘画
面试者：在什么东西上画？纸，布，还是墙上？
面试官：在布上
面试者：噢。那它是什么笔尖？毡尖？圆珠？它画出来东西能被洗掉吗？
面试官：要能被洗掉的 …许多问题过后…
面试者：嗯。我知道了，我们有一支笔。它的目标人群是5－10岁的儿童， 它是毡尖笔并且有红绿蓝黑等颜色，它可以画在布上并且可以洗掉，是这样吗？
这样一来，面试者就得到了一个与一开始的问题完全不同的问题了，更加的具体， 因而更容易入手。可以进行的测试有：
这支笔画出来的东西可以在什么水温中被洗掉，用热水，温水，冷水测试
画出的东西过了一段时间后还能被洗掉吗？刚画上去笔迹还是湿的时候就拿去洗会怎样？
对儿童是否安全(无毒)？

11.6
How would you test an ATM in a distributed banking system?
老样子，还是需要弄清楚问题的限制是什么。以下是你可以问的问题：
这台ATM机是给谁用的？答案可能是任何人，盲人(残疾人)或是其它
这台ATM机的用途是什么？取款，转账，查询余额，存款？
我们可以使用什么工具来测试？我们是否能看到系统源码，还是只能面对实体机器？
注意：一个好的测试人员会确保他了解测试对象的方方面面。
以下是一些测试取款功能的测试用例：
取款金额小于余额
取款金额大于余额
取款金额等于余额
同时在ATM机和网上取款
当与银行的网络连接断开后进行取款
同时从多台ATM机取款





"""