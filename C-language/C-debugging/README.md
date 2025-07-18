# 0x03. C - Debugging

**Debugging** is the process of finding and fixing errors in software that prevents it from running correctly.

Think of it like this:

+ You write a program.

+ Something doesn’t work — maybe it crashes, gives the wrong result, or behaves oddly.

+ You debug by:

  + Identifying where the problem is,

  + Understanding why it happens, and

  + Fixing it.

Common Debugging Steps:

1. Reproduce the problem

Make the bug happen consistently so you can study it.

2. Read the error message

Most programming languages show error messages — they often tell you where to look.

3. Use print statements or a debugger

Print values or step through your code line by line.

4. Isolate the issue

Test smaller parts of your code to narrow it down.

5. Fix the bug

Change your code — then test again to be sure it’s really fixed.

6. Think long-term

Ask yourself: Why did this happen? How can I prevent similar bugs later?

## RUBBER DUCKING

Rubber ducking (short for rubber duck debugging) is a technique where you explain your code or problem out loud, step by step, as if you're teaching or describing it to someone else — often a rubber duck 🐥 on your desk.

### Why It's Called That

The term comes from the book "The Pragmatic Programmer" where a developer kept a rubber duck on their desk and would explain their code to it when they got stuck.

Just by talking it through, they often figured out the problem on their own — without needing anyone else's help.

### How Rubber Ducking Works

1. Pretend the duck doesn’t know anything.

2. Start from the top of your code.

3. Explain what each part is supposed to do.

4. Keep going until either:

  + You spot the bug,

  + Or you realize your logic isn’t doing what you thought.

### Example

Let’s say your program is supposed to add two numbers but it gives the wrong result.

You say:

**"Okay duck, I'm calling add(5, 3). That should give 8. But I'm getting 2. Hmm... Let me look at the function. It says return a - b. Oh! I’m subtracting, not adding. There’s the problem!"**

The duck didn’t say a word, but just explaining it out loud helped you see the mistake.

### so rubber ducking is

| Term               | Meaning                                         |
| ------------------ | ----------------------------------------------- |
| **Rubber ducking** | Explaining your code out loud to catch mistakes |
| **Why it works**   | Forces you to slow down and think clearly       |
| **Who it helps**   | Everyone from beginners to expert programmers   |



